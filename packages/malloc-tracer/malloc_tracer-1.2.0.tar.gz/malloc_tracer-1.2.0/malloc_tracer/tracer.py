#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import inspect
import ast
import math
import contextlib
import textwrap
import os
import linecache
from enum import Enum
from tracemalloc import start, take_snapshot, stop, Filter


__all__ = ['Tracer', 'RelatedTracesOutputMode']


DUMMY_SRC_NAME = '<tracer-src>'


def bytes_to_hrf(size):
    '''Convert bytes to human readable format.'''
    units = ('B', 'KiB', 'MiB', 'GiB', 'TiB')

    if size > 0:
        order = min(int(math.log(size) / math.log(1024)), len(units)-1)
    else:
        order = 0

    fmt = '6.0f' if order == 0 else '6.1f'
    return '{0:{1}} {2}'.format(size/(1024**order), fmt, units[order])


@contextlib.contextmanager
def apply_modules_temporarily(setup='pass', extras=None):
    '''Apply modules temporarily.'''
    if extras is None:
        temp = dict()
    else:
        temp = extras.copy()

    if setup != 'pass':
        code = compile(setup, DUMMY_SRC_NAME, 'exec')
        exec(code, globals(), temp)

    for key in list(temp):
        if key in globals().keys():
            temp.pop(key)

    globals().update(temp)

    try:
        yield
    finally:
        # Restore.
        for key in temp.keys():
            globals().pop(key, None)


class Transformer(ast.NodeTransformer):
    '''Add tracemalloc functions.'''
    def __init__(self, result_id):
        self._result_id = result_id

    def visit_FunctionDef(self, node):
        # Pre-hook.
        pre_hook_expr = ast.Expr(
            value=ast.Call(
                func=ast.Name(id='start', ctx=ast.Load()),
                args=[],
                keywords=[]
            )
        )
        # Post-hook.
        finalbody = [
            ast.Global(names=[self._result_id]),
            ast.Assign(
                targets=[ast.Name(id=self._result_id, ctx=ast.Store())],
                value=ast.Call(
                    func=ast.Name(id='take_snapshot', ctx=ast.Load()),
                    args=[],
                    keywords=[]
                )
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Name(id='stop', ctx=ast.Load()),
                    args=[],
                    keywords=[]
                )
            )
        ]

        body_elems = [pre_hook_expr]
        body_elems.extend([elem for elem in node.body])
        node.body.clear()
        node.body.append(
            ast.Try(
                body=body_elems,
                handlers=[],
                orelse=[],
                finalbody=finalbody
            )
        )

        return ast.fix_missing_locations(node)


class CodeBlockCollector(ast.NodeVisitor):
    '''Collect code blocks.'''
    def __init__(self):
        self.code_blocks = dict()

    def visit_FunctionDef(self, node):
        self.code_blocks[node.name] = (node.lineno, node.body[-1].lineno)


class DependencyCollector(ast.NodeVisitor):
    '''Collect dependencies.'''
    def __init__(self, module):
        self._dependencies = dict()
        self._module = module

    @property
    def dependencies(self):
        from types import MappingProxyType
        return MappingProxyType(self._dependencies)

    def visit_Name(self, node):
        key = node.id
        if key not in self._dependencies.keys():
            if key in self._module.__dict__.keys():
                self._dependencies[key] = self._module.__dict__.get(key)


def extract_dependencies(obj):
    '''Extract dependencies.'''
    module = inspect.getmodule(obj)
    collector = DependencyCollector(module=module)

    source = inspect.getsource(obj)
    source = textwrap.dedent(source)
    node = ast.parse(source)
    collector.visit(node)

    return collector.dependencies


class TraceRecord(object):

    def __init__(self, filepath, lineno, size):
        self._filepath = filepath
        self._lineno = lineno
        self._size = size

    @property
    def filepath(self):
        return self._filepath

    @property
    def short_filepath(self):
        return os.sep.join(self._filepath.split(os.sep)[-2:])

    @property
    def lineno(self):
        return self._lineno

    @property
    def size(self):
        return self._size

    @property
    def human_readable_size(self):
        return bytes_to_hrf(self._size)

    @property
    def line(self):
        line = linecache.getline(self._filepath, self._lineno).rstrip()
        # linecache.clearcache()
        return line


class RelatedTracesOutputMode(Enum):
    '''Output modes for Related traces.'''
    NONE = 0
    FOR_EACH_FILE = 1  #: Displays related traces for each file.
    IN_DESCENDING_ORDER = 2  #: Display related traces in descending order.


class Tracer(object):
    '''Tracing malloc that occurs inside a function or method.

    Args:
        function_or_method:
        enable_auto_resolve (bool):
        setup (str): Compile-time dependencies.
            This parameter is ignored if enable_auto_resolve is enabled.
    '''
    def __init__(
        self,
        function_or_method,
        enable_auto_resolve=True,
        setup='pass'
    ):
        if not (inspect.isfunction(function_or_method)
                or inspect.ismethod(function_or_method)):
            raise TypeError('The obj must be a function or a method.')

        if enable_auto_resolve:
            dependencies = extract_dependencies(function_or_method)
            setup = 'pass'
        else:
            dependencies = dict()

        with apply_modules_temporarily(setup=setup, extras=dependencies):
            source_lines, lineno = inspect.getsourcelines(function_or_method)
            source_text = ''.join(source_lines)
            source_text = textwrap.dedent(source_text)
            source_text = source_text.strip()

            node = ast.parse(source_text)
            node = Transformer(result_id='SNAPSHOT').visit(node)

            locals_ = dict()
            code = compile(node, DUMMY_SRC_NAME, 'exec')
            exec(code, globals(), locals_)

        new_obj = locals_[function_or_method.__name__]
        if hasattr(new_obj, '__func__'):
            # class method or static method.
            self._function_or_method = new_obj.__func__
        else:
            # function or method
            self._function_or_method = new_obj

        if hasattr(function_or_method, '__self__'):
            self._class_instance = function_or_method.__self__
        else:
            self._class_instance = None

        self._source_lines = source_lines
        self._lineno = lineno
        self._filepath = inspect.getfile(function_or_method)
        self._enable_auto_resolve = enable_auto_resolve
        self._dependencies = dependencies

    def _take_snapshot(
        self,
        target_args=None,
        setup='pass'
    ):
        '''Take the snapshot.

        Args:
            target_args (dict):
            setup (str): Run-time dependencies.
                This parameter is ignored if enable_auto_resolve is enabled.

        Returns:
            tracemalloc.Snapshot
        '''
        extras = {'SNAPSHOT': None}
        if self._enable_auto_resolve:
            extras.update(self._dependencies)
            setup = 'pass'

        with apply_modules_temporarily(setup=setup, extras=extras):
            global SNAPSHOT

            if target_args is None:
                target_args = dict()

            if self._class_instance is None:
                self._function_or_method(**target_args)
            else:
                self._function_or_method(self._class_instance, **target_args)

            return SNAPSHOT

    def trace(
        self,
        target_args=None,
        setup='pass',
        related_traces_output_mode=RelatedTracesOutputMode.NONE
    ):
        '''Display the trace result.

        Args:
            target_args (dict):
            setup (str): Run-time dependencies.
                This parameter is ignored if enable_auto_resolve is enabled.
            related_traces_output_mode (:class:`RelatedTracesOutputMode`):
        '''
        snapshot = self._take_snapshot(
            target_args=target_args,
            setup=setup
        )

        traces_records = dict()
        stats = snapshot.statistics('lineno')
        for stat in stats:
            frame = stat.traceback[0]
            key = frame.filename
            traces_record = traces_records.get(key)
            if traces_record is None:
                traces_records[key] = dict()
                traces_record = traces_records.get(key)

            traces_record[frame.lineno] = TraceRecord(
                filepath=frame.filename,
                lineno=frame.lineno,
                size=stat.size
            )

        # for DUMMY_SRC_NAME.
        print('<< Target traces >>')
        print('File "{}"'.format(self._filepath))
        print('Line #    Trace         Line Contents')
        print('=' * (24+80))

        traces_record = traces_records.get(DUMMY_SRC_NAME)
        source_text = ''.join(self._source_lines).rstrip()
        for lineno, line in enumerate(source_text.split(sep='\n'), 1):
            if traces_record is None:
                trace = ' ' * 10
            else:
                tr = traces_record.get(lineno)
                trace = ' ' * 10 if tr is None else tr.human_readable_size

            print('{lineno:6d}    {trace:10s}    {contents}'.format(
                lineno=self._lineno + lineno - 1,
                trace=trace,
                contents=line
            ))

        if traces_record is None:
            num_lines = 0
            total = 0
        else:
            num_lines = len(traces_record)
            total = sum(tr.size for tr in traces_record.values())

        print('-' * (24 + 80))
        print('{:6d}    {:10s} (raw {} B)'.format(
            num_lines,
            bytes_to_hrf(total),
            total
        ))

        # for others.
        if related_traces_output_mode == RelatedTracesOutputMode.NONE:
            print()
        elif related_traces_output_mode == RelatedTracesOutputMode.FOR_EACH_FILE:
            print()
            self._display_related_traces_for_each_file(traces_records)
        elif related_traces_output_mode == RelatedTracesOutputMode.IN_DESCENDING_ORDER:
            print()
            self._display_related_traces_in_descending_order(traces_records)

        # Total allocated size.
        total = sum(stat.size for stat in stats)
        print('Total allocated size: {} (raw {} B)'.format(
            bytes_to_hrf(total).lstrip(),
            total
        ))

    def _display_related_traces_for_each_file(self, traces_records):
        '''Displays related traces for each file.'''
        related_traces_records = {k: v for k, v in traces_records.items() if k != DUMMY_SRC_NAME}
        for filepath, traces_record in sorted(related_traces_records.items()):
            print('<< Related traces >>')
            print('File "{}"'.format(filepath))
            print('Line #    Trace         Line Contents')
            print('=' * (24 + 80))

            total = 0
            for lineno, tr in sorted(traces_record.items()):
                print('{lineno:6d}    {trace:10s}    {contents}'.format(
                    lineno=tr.lineno,
                    trace=tr.human_readable_size,
                    contents=tr.line
                ))
                total += tr.size

            print('-' * (24 + 80))
            print('{:6d}    {:10s} (raw {} B)\n'.format(
                len(traces_record),
                bytes_to_hrf(total),
                total
            ))

    def _display_related_traces_in_descending_order(self, traces_records):
        '''Display related traces in descending order.'''
        related_trace_records = list()
        for filepath, traces_record in traces_records.items():
            if filepath == DUMMY_SRC_NAME:
                continue

            for _, tr in traces_record.items():
                related_trace_records.append(tr)

        if not related_trace_records:
            return

        print('<< Related traces >>')
        print('Line #    Trace         Line Contents')
        print('=' * (24 + 80))

        related_trace_records.sort(key=lambda tr: tr.size, reverse=True)
        for index, related_trace_record in enumerate(related_trace_records, 1):
            print('#{} "{}": (raw {} B)'.format(
                index,
                related_trace_record.filepath,
                related_trace_record.size
            ))
            print('{lineno:6d}    {trace:10s}    {contents}\n'.format(
                lineno=related_trace_record.lineno,
                trace=related_trace_record.human_readable_size,
                contents=related_trace_record.line
            ))
