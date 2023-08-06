#!/usr/bin/python

"""
partial_readonly provide a decorator for conveniently making some fields
read-only in dataclass. No dependencies other than the Python Standard
Library.

Require >= python 3.7.0

Homepage: http://github.com/book987/partial_readonly

Copyright (c) 2018, book987.
License: MIT (see LICENSE for details)
"""


__author__  = 'book987'
__version__ = '0.0.3'
__license__ = 'MIT'


__all__ = ['partial_readonly']

import ast
import inspect

from ast import (
    arg,
    arguments,
    FunctionDef,
    Attribute,
    Name,
    Load,
    Store,
    Return,
    Module,
)
from typing import Callable, ClassVar, List
from dataclasses import is_dataclass


def partial_readonly(cls: ClassVar) -> ClassVar:

    if not is_dataclass(cls):
        raise RuntimeError('partial_readonly only use in dataclass')
    return _process(cls)


def _process(cls: ClassVar) -> ClassVar:
    """Get arguments we want to control and make them read-only"""
    _get_readonly_args(cls)
    for data in cls.readonly_args:
        _make_readonly(cls, *data)
    return cls


def _get_readonly_args(cls: ClassVar) -> List:
    """Make field with one-underline prefix readonly

    Take field from annotation is more convenient, because
    `partial_readonly` only works for dataclass

    """
    vars_annotation = cls.__annotations__
    cls.readonly_args = []
    for var, annotation in vars_annotation.items():
        if not var.startswith('__') and var.startswith('_'):
            data = [var.lstrip('_')]
            if type(annotation) is str and \
               len(annotation.split()) > 1 and \
               annotation.split()[-1].startswith('alias='):
                data.append(annotation.split()[-1].replace('alias=', ''))
            cls.readonly_args.append(data)


def _make_readonly(cls: ClassVar, var: str, alias: str = None) -> None:
    """Set cls.var to be property with no setter

    Args:
        cls: class reference
        var: field name
    """
    setattr(cls, alias or var, property(_gen_getter(var), _ban_setter))


def _ban_setter(*args, **kwargs):
    raise AttributeError('Read-only property cannot be set')


def _gen_getter(var: str):
    """Generate a getter with named {var}_getter"""
    func_name = f'{var}_getter'
    self_arg = arg(arg='self', annotation=None)
    func_args = arguments(
        args=[self_arg],
        kwonlyargs=[],
        vararg=None,
        kwarg=None,
        defaults=[],
        kw_defaults=[],
    )
    var_value = Attribute(
        value=Name(
            id='self',
            ctx=Load()
        ),
        attr=f'_{var}',
        ctx=Load(),
    )
    ret_stmt = Return(
        value=var_value,
    )
    func = FunctionDef(
        name=func_name,
        args=func_args,
        body=[ret_stmt],
        decorator_list=[],
        returns=None,
    )
    wrap_func = Module(body=[func])
    return _ast_to_code(wrap_func, func_name)


def _ast_to_code(node: FunctionDef, name: str) -> str:
    """compile ast.FunctionDef node and return function name"""
    ast.fix_missing_locations(node)
    code = compile(node, __file__, 'exec')
    scope = {}
    exec(code, globals(), scope)
    return scope[name]

