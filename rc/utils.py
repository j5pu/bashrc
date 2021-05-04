# -*- coding: utf-8 -*-
"""
Utils Module.

Examples:
    >>> from copy import deepcopy
    >>> import environs
    >>>
    >>> deepcopy(environs.Env()) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    RecursionError: maximum recursion depth exceeded
"""
__all__ = (
    'ABCMeta',
    'abstractmethod',
    'AST',
    'AsyncFor',
    'AsyncFunctionDef',
    'AsyncWith',
    'Await',
    'ClassDef',
    'FunctionDef',
    'get_source_segment',
    'Import',
    'ImportFrom',
    'NodeVisitor',
    'walk',
    'current_task',
    'get_running_loop',
    'iscoroutine',
    'ChainMap',
    'defaultdict',
    'namedtuple',
    'OrderedDict',
    'AsyncGenerator',
    'AsyncIterable',
    'AsyncIterator',
    'Awaitable',
    'ByteString',
    'Callable',
    'Collection',
    'Container',
    'Coroutine',
    'Generator',
    'Hashable',
    'ItemsView',
    'Iterable',
    'Iterator',
    'KeysView',
    'Mapping',
    'MappingView',
    'MutableMapping',
    'MutableSequence',
    'MutableSet',
    'Reversible',
    'Sequence',
    'Set',
    'Sized',
    'ValuesView',
    'ProcessPoolExecutor',
    'ThreadPoolExecutor',
    'suppress',
    'dataclass',
    'DataField',
    'datafield',
    'datafields',
    'InitVar',
    'auto',
    'Enum',
    'cached_property',
    'partial',
    'singledispatch',
    'singledispatchmethod',
    'wraps',
    'import_module',
    'classify_class_attrs',
    'FrameInfo',
    'getfile',
    'getsource',
    'getsourcefile',
    'getsourcelines',
    'isasyncgenfunction',
    'isawaitable',
    'iscoroutinefunction',
    'isgetsetdescriptor',
    'ismemberdescriptor',
    'ismethoddescriptor',
    'isroutine',
    'insstack',
    'BytesIO',
    'FileIO',
    'StringIO',
    'attrgetter',
    'PathLike',
    'PathLib',
    'pickle_dump',
    'pickle_dumps',
    'pickle_load',
    'pickle_loads',
    'PicklingError',
    'CompletedProcess',
    'CRLock',
    'Lock',
    'timeit',
    'AsyncGeneratorType',
    'BuiltinFunctionType',
    'ClassMethodDescriptorType',
    'CodeType',
    'CoroutineType',
    'FrameType',
    'FunctionType',
    'GeneratorType',
    'GenericAlias',
    'GetSetDescriptorType',
    'LambdaType',
    'MappingProxyType',
    'MemberDescriptorType',
    'MethodType',
    'MethodWrapperType',
    'ModuleType',
    'Simple',
    'TracebackType',
    'WrapperDescriptorType',
    'Alias',
    'catch_warnings',
    'filterwarnings',

    # Imports - PyPi
    'pickle_np',
    'np',
    'pd',
    'Exit',
    'dpathdelete',
    'dpathget',
    'dpathnew',
    'dpathset',
    'dpathsearch',
    'dpathvalues',
    'Environs',
    'GitRepo',
    'GitSymbolicReference',
    'Pickler',
    'Unpickler',
    'collapse',
    'consume',
    'first_true',
    'map_reduce',
    'side_effect',
    'nested_lookup',
    'Console',
    'pretty_install',
    'traceback_install',
    'var_name',

    # Imports - Protected
    'RunningLoop',
    'slotnames',
    'DATACLASS_FIELDS',
    'MISSING_TYPE',
    'POST_INIT_NAME',
    'CRLock',
    'Alias',

    # Typing
    'DictStrAny',
    'ExceptionUnion',
    'LST',
    'SeqNoStr',
    'SeqUnion',
    'TupleStr',
    'TupleType',

    # Constants
    'BUILTINS',
    'BUILTINS_CLASSES',
    'BUILTINS_FUNCTIONS',
    'BUILTINS_OTHER',
    'console',
    'cp',
    'DATACLASS_FIELDS',
    'debug',
    'fmic',
    'fmicc',
    'FRAME_SYS_INIT',
    'FUNCTION_MODULE',
    'ic',
    'icc',
    'IgnoreAttr',
    'IgnoreCopy',
    'IgnoreStr',
    'NEWLINE',
    'PICKLE_ATTRS',
    'print_exception',
    'PYTHON_SYS',
    'PYTHON_SITE',

    # NamedTuple
    'AccessEnumMembers',
    'Annotation',
    'Attribute',
    'CacheWrapperInfo',
    'GetEnumMembers',

    # Enums
    'EnumBase',
    'Access',
    'ChainRV',
    'Executor',
    'Kind',
    'GetBase',
    'Get',
    'ModuleBase',
    'Module',
    'NameBase',
    'Name',
    'PrivateBase',
    'Private',
    'ProtectedBase',
    'Protected',
    'PublicBase',
    'Public',

    # Enums - NamedTuple - Typing
    'AttrUnion',
    'EnumBaseAlias',

    # Functions
    'aioloop',
    'allin',
    'annotations',
    'annotations_init',
    'anyin',
    'cache',
    'cmd',
    'cmdname',
    'current_task_name',
    'delete',
    'delete_list',
    'dict_sort',
    'effect',
    'enumvalue',
    'get',
    'getset',
    'iseven',
    'in_dict',
    'join_newline',
    'map_reduce_even',
    'map_with_args',
    'newprop',
    'noexception',
    'prefixed',
    'repr_format',
    'runwarning',
    'split_sep',
    'startswith',
    'to_camel',
    'to_iter',
    'token_open',
    'varname',
    'yield_if',
    'yield_last',

    # Es
    'Es',

    # Exceptions
    'CmdError',
    'CmdAioError',

    # Types
    'AnnotationsType',
    'AsDictMethodType',
    'AsDictPropertyType',
    'DataType',
    'DictType',
    'GetAttrNoBuiltinType',
    'GetAttrType',
    'GetSupportType',
    'GetType',
    'NamedType',
    'NamedAnnotationsType',
    'SlotsType',

    # Classes
    'BoxKeys',
    'Chain',
    'pproperty',

    # Bases
    'BaseState',

    # States
    'StateEnv',

    # Aliases
    'EnumBaseAlias',

    # Echo
    'black',
    'blue',
    'cyan',
    'green',
    'magenta',
    'red',
    'white',
    'yellow',
    'bblack',
    'bblue',
    'bcyan',
    'bgreen',
    'bmagenta',
    'bred',
    'bwhite',
    'byellow',

    # Test
    'TestAsync',
)

import ast
import collections.abc
import copy
import functools
import re
import subprocess
import sys
import textwrap
import tokenize
import types
import typing
import warnings
from abc import ABCMeta as ABCMeta
from abc import abstractmethod as abstractmethod
from ast import AST as AST
from ast import AsyncFor as AsyncFor
from ast import AsyncFunctionDef as AsyncFunctionDef
from ast import AsyncWith as AsyncWith
from ast import Await as Await
from ast import ClassDef as ClassDef
from ast import FunctionDef as FunctionDef
from ast import get_source_segment as get_source_segment
from ast import Import as Import
from ast import ImportFrom as ImportFrom
from ast import NodeVisitor as NodeVisitor
from ast import walk as walk
from asyncio import current_task as current_task
from asyncio import get_running_loop as get_running_loop
from asyncio import iscoroutine as iscoroutine
from asyncio.events import _RunningLoop
from collections import ChainMap as ChainMap
from collections import defaultdict as defaultdict
from collections import namedtuple as namedtuple
from collections import OrderedDict as OrderedDict
from collections.abc import AsyncGenerator as AsyncGenerator
from collections.abc import AsyncIterable as AsyncIterable
from collections.abc import AsyncIterator as AsyncIterator
from collections.abc import Awaitable as Awaitable
from collections.abc import ByteString as ByteString
from collections.abc import Callable as Callable
from collections.abc import Collection as Collection
from collections.abc import Container as Container
from collections.abc import Coroutine as Coroutine
from collections.abc import Generator as Generator
from collections.abc import Hashable as Hashable
from collections.abc import ItemsView as ItemsView
from collections.abc import Iterable as Iterable
from collections.abc import Iterator as Iterator
from collections.abc import KeysView as KeysView
from collections.abc import Mapping as Mapping
from collections.abc import MappingView as MappingView
from collections.abc import MutableMapping as MutableMapping
from collections.abc import MutableSequence as MutableSequence
from collections.abc import MutableSet as MutableSet
from collections.abc import Reversible as Reversible
from collections.abc import Sequence as Sequence
from collections.abc import Set as Set
from collections.abc import Sized as Sized
from collections.abc import ValuesView as ValuesView
from concurrent.futures.process import ProcessPoolExecutor as ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor as ThreadPoolExecutor
from contextlib import suppress as suppress
from copyreg import _slotnames
from dataclasses import _FIELDS
from dataclasses import _MISSING_TYPE
from dataclasses import _POST_INIT_NAME
from dataclasses import dataclass as dataclass
from dataclasses import Field as DataField
from dataclasses import field as datafield
from dataclasses import fields as datafields
from dataclasses import InitVar as InitVar
from enum import auto as auto
from enum import Enum as Enum
from functools import cached_property as cached_property
from functools import partial as partial
from functools import singledispatch as singledispatch
from functools import singledispatchmethod as singledispatchmethod
from functools import wraps as wraps
from importlib import import_module as import_module
from inspect import classify_class_attrs as classify_class_attrs
from inspect import FrameInfo as FrameInfo
from inspect import getfile as getfile
from inspect import getsource as getsource
from inspect import getsourcefile as getsourcefile
from inspect import getsourcelines as getsourcelines
from inspect import isasyncgenfunction as isasyncgenfunction
from inspect import isawaitable as isawaitable
from inspect import iscoroutinefunction as iscoroutinefunction
from inspect import isgetsetdescriptor as isgetsetdescriptor
from inspect import ismemberdescriptor as ismemberdescriptor
from inspect import ismethoddescriptor as ismethoddescriptor
from inspect import isroutine as isroutine
from inspect import stack as insstack
from io import BytesIO as BytesIO
from io import FileIO as FileIO
from io import StringIO as StringIO
from operator import attrgetter as attrgetter
from os import PathLike as PathLike
from pathlib import Path as PathLib
from pickle import dump as pickle_dump
from pickle import dumps as pickle_dumps
from pickle import load as pickle_load
from pickle import loads as pickle_loads
from pickle import PicklingError as PicklingError
from subprocess import CompletedProcess as CompletedProcess
from threading import _CRLock
from threading import Lock as Lock
from timeit import timeit as timeit
from types import AsyncGeneratorType as AsyncGeneratorType
from types import BuiltinFunctionType as BuiltinFunctionType
from types import ClassMethodDescriptorType as ClassMethodDescriptorType
from types import CodeType as CodeType
from types import CoroutineType as CoroutineType
from types import DynamicClassAttribute as DynamicClassAttribute
from types import FrameType as FrameType
from types import FunctionType as FunctionType
from types import GeneratorType as GeneratorType
from types import GenericAlias as GenericAlias
from types import GetSetDescriptorType as GetSetDescriptorType
from types import LambdaType as LambdaType
from types import MappingProxyType as MappingProxyType
from types import MemberDescriptorType as MemberDescriptorType
from types import MethodType as MethodType
from types import MethodWrapperType as MethodWrapperType
from types import ModuleType as ModuleType
from types import SimpleNamespace as Simple
from types import TracebackType as TracebackType
from types import WrapperDescriptorType as WrapperDescriptorType
from typing import _alias
from typing import Any
from typing import ClassVar
from typing import Final
from typing import get_args
from typing import get_origin
from typing import get_type_hints
from typing import Literal
from typing import NamedTuple
from typing import Optional
from typing import Protocol
from typing import runtime_checkable
from typing import Union
from typing import Type
from warnings import catch_warnings as catch_warnings
from warnings import filterwarnings as filterwarnings

import jsonpickle.ext.numpy as pickle_np
import numpy as np
import pandas as pd
from box import Box as Box
from bson import ObjectId as ObjectId
from click import secho as secho
from click.exceptions import Exit as Exit
from decorator import decorator as decorator
from devtools import Debug as Debug
from dpath.util import delete as dpathdelete
from dpath.util import get as dpathget
from dpath.util import new as dpathnew
from dpath.util import search as dpathsearch
from dpath.util import set as dpathset
from dpath.util import values as dpathvalues
from environs import Env as Environs
from git import GitConfigParser as GitConfigParser
from git import Remote as Remote
from git import Repo as GitRepo
from git.refs import SymbolicReference as GitSymbolicReference
from icecream import IceCreamDebugger as IceCreamDebugger
from jsonpickle.pickler import Pickler as Pickler
from jsonpickle.unpickler import Unpickler as Unpickler
from jsonpickle.util import importable_name
from jsonpickle.util import is_collections
from jsonpickle.util import is_installed
from jsonpickle.util import is_module_function
from jsonpickle.util import is_noncomplex
from jsonpickle.util import is_object
from jsonpickle.util import is_primitive
from jsonpickle.util import is_reducible
from jsonpickle.util import is_reducible_sequence_subclass
from jsonpickle.util import is_unicode
from more_itertools import collapse as collapse
from more_itertools import consume as consume
from more_itertools import first_true as first_true
from more_itertools import map_reduce as map_reduce
from more_itertools import side_effect as side_effect
from nested_lookup.nested_lookup import _nested_lookup
from nested_lookup import nested_lookup as nested_lookup
from rich.console import Console as Console
from rich.pretty import install as pretty_install
from rich.traceback import install as traceback_install
from varname import varname as var_name

# <editor-fold desc="Protected">
RunningLoop = _RunningLoop
slotnames = _slotnames
DATACLASS_FIELDS = _FIELDS
MISSING_TYPE = _MISSING_TYPE
POST_INIT_NAME = _POST_INIT_NAME
CRLock = _CRLock
Alias = _alias


# </editor-fold>
# <editor-fold desc="Typing">
DictStrAny = dict[str, Any]
ExceptionUnion = Union[tuple[Type[Exception]], Type[Exception]]
LST = Union[typing.MutableSequence, typing.MutableSet, tuple]
SeqNoStr = Union[typing.Iterator, typing.KeysView, typing.MutableSequence, typing.MutableSet, tuple, typing.ValuesView]
SeqUnion = Union[typing.AnyStr, typing.ByteString, typing.Iterator, typing.KeysView, typing.MutableSequence,
                 typing.MutableSet, typing.Sequence, tuple, typing.ValuesView]
TupleStr = tuple[str, ...]
TupleType = tuple[Type, ...]


# </editor-fold>
# <editor-fold desc="Constants">
BUILTINS = (_bltns if isinstance(_bltns := globals()['__builtins__'], dict) else vars(_bltns)).copy()
BUILTINS_CLASSES = tuple(filter(lambda x: isinstance(x, type), BUILTINS.values()))
BUILTINS_FUNCTIONS = tuple(filter(lambda x: isinstance(x, (BuiltinFunctionType, FunctionType,)), BUILTINS.values()))
BUILTINS_OTHER = tuple(map(BUILTINS.get, ('__doc__', '__import__', '__spec__', 'copyright', 'credits', 'exit',
                                          'help', 'license', 'quit',)))
console = Console(color_system='256')
cp = console.print
debug = Debug(highlight=True)
fmic = IceCreamDebugger(prefix=str()).format
fmicc = IceCreamDebugger(prefix=str(), includeContext=True).format
FRAME_SYS_INIT = sys._getframe(0)
FUNCTION_MODULE = '<module>'
ic = IceCreamDebugger(prefix=str())
icc = IceCreamDebugger(prefix=str(), includeContext=True)
IgnoreAttr = Literal['asdict', 'attrs', 'defaults', 'keys', 'kwargs', 'kwargs_dict', 'public', 'values', 'values_dict']
"""Exclude instance attribute."""
IgnoreCopy = Union[CRLock, Environs, FrameType, GitConfigParser, GitSymbolicReference, Remote]
"""True or class for repr instead of nested asdict and deepcopy. No deepcopy (default: (:class:`rc.CRLock`,
:class:`rc.Environs`, :class:`types.FrameType`, :class:`git.GitConfigParser`, :class:`rc.GitSymbolicReference`,
:class:`git.Remote`, ))."""
IgnoreStr = Union[GitConfigParser, GitRepo, ObjectId, PathLib]
"""Use str value for object (default: (:class:`git.GitConfigParser`, :class:`rc.GitRepo`, :class:`bson.ObjectId`,
:class:`rc.PathLib`, ))."""
LockClass = type(Lock())
NEWLINE = '\n'
PICKLE_ATTRS = {
    Environs: ('__custom_parsers__', '_errors', '_fields', '_prefix', '_sealed', '_values', 'eager', 'expand_vars', ),
}
print_exception = console.print_exception
PYTHON_SYS = PathLib(sys.executable)
PYTHON_SITE = PathLib(PYTHON_SYS).resolve()


# </editor-fold>
# <editor-fold desc="NamedTuple">
AccessEnumMembers = namedtuple('AccessEnumMembers', 'all private protected public')
Annotation = namedtuple('Annotation', 'any args classvar cls default final hint initvar literal name optional '
                                      'origin union')
Attribute = namedtuple('Attribute', 'annotation default defining es field kind name object qual')
CacheWrapperInfo = namedtuple('CacheWrapperInfo', 'hit passed total')
GetEnumMembers = namedtuple('GetEnumMembers', 'all pickle private protected public')


# </editor-fold>
# <editor-fold desc="Enums">
class EnumBase(Enum):
    def _generate_next_value_(self, start, count, last_values):
        return self.lower()

    @classmethod
    def asdict(cls):
        return {key: value._value_ for key, value in cls.__members__.items()}

    @classmethod
    def attrs(cls):
        return list(cls.__members__)

    @classmethod
    def default(cls):
        return cls._member_map_[cls._member_names_[0]]

    @classmethod
    def default_attr(cls):
        return cls.attrs()[0]

    @classmethod
    def default_dict(cls):
        return {cls.default_attr(): cls.default_value()}

    @classmethod
    def default_value(cls):
        return cls[cls.default_attr()]

    @property
    def describe(self):
        """
        Returns:
            tuple:
        """
        # self is the member here
        return self.name, self.value

    @property
    def lower(self):
        return self.name.lower()

    @classmethod
    def values(cls):
        return list(cls.asdict().values())


class Access(EnumBase):
    """Access Attributes Enum Class."""
    ALL = re.compile('.')
    PRIVATE = re.compile('^__.*')
    PROTECTED = re.compile('^_(?!_).*$')
    PUBLIC = re.compile('^(?!_)..*$')

    @classmethod
    @functools.cache
    def classify(cls, *args, keys=False, **kwargs):
        """
        Classify args or kwargs based on data access.

        Examples:
            >>> a = Access.classify(**dict(map(lambda x: (x.name, x, ), classify_class_attrs(TestAsync))))
            >>> n = '__class__'
            >>> assert n in a.all and n in a.private and n not in a.protected and n not in a.public
            >>> n = TestAsync._staticmethod
            >>> assert n in a.all and n not in a.private and n in a.protected and n not in a.public
            >>> n = TestAsync.staticmethod.__name__
            >>> assert n in a.all and n not in a.private and n not in a.protected and n in a.public
            >>>
            >>> a = Access.classify(**dict(map(lambda x: (x.name, x, ), classify_class_attrs(TestAsync))), keys=True)
            >>> n = '__class__'
            >>> assert n in a.all and n in a.private and n not in a.protected and n not in a.public
            >>> assert a.private[n].name == n
            >>> n = TestAsync._staticmethod
            >>> assert n in a.all and n not in a.private and n in a.protected and n not in a.public
            >>> assert a.protected[n].name == n
            >>> n = TestAsync.staticmethod.__name__
            >>> assert n in a.all and n not in a.private and n not in a.protected and n in a.public
            >>> assert a.public[n].name == n

        Args:
            *args: str iterable.
            keys: include keys if kwargs so return dict or list with kwargs.values().
            **kwargs: dict with keys to check and values

        Raises:
            TypeError('args or kwargs not both')

        Returns:
            AccessEnumMembers.
        """
        if args and kwargs:
            raise TypeError('args or kwargs not both')
        rv: defaultdict[Access, Union[dict, list]] = defaultdict(dict if keys and kwargs else list, dict())
        for name in args or kwargs:
            if value := cls.val(name):
                rv[value].update({name: kwargs.get(name)}) if keys and kwargs else rv[value].append(name)
                rv[cls.ALL].update({name: kwargs.get(name)}) if keys and kwargs else rv[cls.ALL].append(name)
        return AccessEnumMembers(all=rv[cls.ALL], private=rv[cls.PRIVATE], protected=rv[cls.PROTECTED],
                                 public=rv[cls.PUBLIC])

    @functools.cache
    def es(self, name):
        """
        Is Access Attr?

        Examples:
            >>> pretty_install()
            >>> Access.ALL.es(str()), Access.PRIVATE.es(str()), Access.PROTECTED.es(str()), \
Access.PUBLIC.es(str())
            (False, False, False, False)
            >>> Access.ALL.es('__name__'), Access.PRIVATE.es('__name__'), Access.PROTECTED.es('__name__'), \
Access.PUBLIC.es('__name__')
            (True, True, False, False)
            >>> Access.ALL.es('_name__'), Access.PRIVATE.es('_name__'), Access.PROTECTED.es('_name__'), \
Access.PUBLIC.es('_name__')
            (True, False, True, False)
            >>> Access.ALL.es('name__'), Access.PRIVATE.es('name__'), Access.PROTECTED.es('name__'), \
Access.PUBLIC.es('name__')
            (True, False, False, True)

        Args:
            name: name.

        Returns:
            True if match.
        """
        return bool(self.value.search(name))

    @functools.cache
    def include(self, name):
        """
        Include Key.

        Examples:
            >>> pretty_install()
            >>> Access.ALL.include(str()), Access.PRIVATE.include(str()), Access.PROTECTED.include(str()), \
Access.PUBLIC.include(str())
            (None, None, None, None)
            >>> Access.ALL.include('__name__'), Access.PRIVATE.include('__name__'), \
            Access.PROTECTED.include('__name__'), Access.PUBLIC.include('__name__')
            (True, True, False, False)
            >>> Access.ALL.include('_name__'), Access.PRIVATE.include('_name__'), Access.PROTECTED.include('_name__'), \
Access.PUBLIC.include('_name__')
            (True, True, True, False)
            >>> Access.ALL.include('name__'), Access.PRIVATE.include('name__'), Access.PROTECTED.include('name__'), \
Access.PUBLIC.include('name__')
            (True, True, True, True)

        Args:
            name: name.

        Returns:
            True if key to be included.
        """
        Cls = type(self)
        if name:
            if self in (Cls.ALL, Cls.PRIVATE, ):
                return True
            elif self is Cls.PUBLIC:
                return self.es(name)
            elif self is Cls.PROTECTED:
                return self.es(name) or Cls.PUBLIC.es(name)

    @classmethod
    @functools.cache
    def val(cls, name: str):
        """
        Access Enum Instance for name.

        Examples:
            >>> pretty_install()
            >>> Access.val(str()), Access.val('__name__'), Access.val('_name__'), Access.val('name__')
            (
                None,
                <Access.PRIVATE: re.compile('^__.*')>,
                <Access.PROTECTED: re.compile('^_(?!_).*$')>,
                <Access.PUBLIC: re.compile('^(?!_)..*$')>
            )

        Args:
            name: name.

        Returns:
            Access Enum Instance.
        """
        if cls.PRIVATE.es(name):
            return cls.PRIVATE
        elif cls.PROTECTED.es(name):
            return cls.PROTECTED
        elif cls.PUBLIC.es(name):
            return cls.PUBLIC


class ChainRV(EnumBase):
    ALL = auto()
    FIRST = auto()
    UNIQUE = auto()


class Executor(EnumBase):
    PROCESS = ProcessPoolExecutor
    THREAD = ThreadPoolExecutor
    NONE = None

    async def run(self, func, *args, **kwargs):
        """
        Run in :lib:func:`loop.run_in_executor` with :class:`concurrent.futures.ThreadPoolExecutor`,
            :class:`concurrent.futures.ProcessPoolExecutor` or
            :lib:func:`asyncio.get_running_loop().loop.run_in_executor` or not poll.

        Args:
            func: func
            *args: args
            **kwargs: kwargs

        Raises:
            ValueError: ValueError

        Returns:
            Awaitable:
        """
        loop = get_running_loop()
        call = partial(func, *args, **kwargs)
        if not func:
            raise ValueError

        if self.value:
            with self.value() as p:
                return await loop.run_in_executor(p, call)
        return await loop.run_in_executor(self.value, call)


class GetBase(EnumBase):
    def _generate_next_value_(self, start, count, last_values):
        return f'__{self.lower()}__' if self.isupper() else self


class Get(GetBase):
    """
    MRO Helper Calls.

    Private in upper case and public in lower case.

    Examples:
        >>> Get.ALL.value_str, Get.Environs.value_str, Get._asdict.value_str, Get.name.value_str
        ('__all__', 'Env', '_asdict', 'name')

    """
    ALL = auto()
    ANNOTATIONS = auto()
    ARGS = auto()
    ASDICT = auto()
    BUILTINS = auto()
    CACHE_CLEAR = auto()
    CACHE_INFO = auto()
    CACHED = auto()
    CODE = auto()
    CONTAINS = auto()
    DATACLASS_FIELDS = auto()
    DATACLASS_PARAMS = auto()
    DELATTR = auto()
    DICT = auto()
    DIR = auto()
    DOC = auto()
    EQ = auto()
    FILE = auto()
    GET = auto()
    GETATTRIBUTE = auto()
    GETITEM = auto()
    HASH_EXCLUDE = auto()
    IGNORE_ATTR = ('__ignore_attr__', ('asdict', 'attrs', 'defaults', 'keys', 'kwargs', 'kwargs_dict',
                                       'public', 'values', 'values_dict', ))
    """Exclude instance attribute."""
    IGNORE_COPY = ('__ignore_copy__', IgnoreCopy.__args__)
    """True or class for repr instead of nested asdict and deepcopy. No deepcopy."""
    IGNORE_KWARG = auto()
    IGNORE_STR = ('__ignore_str__', IgnoreStr.__args__)
    """Use str value for object ."""
    INIT = auto()
    INIT_SUBCLASS = auto()
    LEN = auto()
    LOADER = auto()
    MEMBERS = auto()
    MODULE = auto()
    MRO = auto()
    NAME = auto()
    PACKAGE = auto()
    PICKLE = auto()
    POST_INIT = auto()
    QUALNAME = auto()
    REDUCE = auto()
    REDUCE_EX = auto()
    REPR = auto()
    REPR_EXCLUDE = auto()
    REPR_NEWLINE = auto()
    REPR_PPROPERTY = auto()
    SETATTR = auto()
    SLOTS = auto()
    SPEC = auto()
    STR = auto()
    SUBCLASSHOOK = auto()
    CRLock = CRLock, ('_block', '_count', '_owner', )
    Environs = Environs, PICKLE_ATTRS[Environs]
    FrameType = FrameType, ()
    GitConfigParser = GitConfigParser, ()
    GitRepo = GitRepo, ()
    GitSymbolicReference = GitSymbolicReference, ()
    LockClass = LockClass, ()
    ObjectId = ObjectId, ()
    PathLib = PathLib, ()
    Remote = Remote, ()
    _asdict = auto()
    _field_defaults = auto()
    _fields = auto()
    name = auto()
    value = auto()

    @classmethod
    @functools.cache
    def getenum_members(cls):
        """
        Enum Class Names and Values.

        Examples:
            >>> pretty_install()
            >>>
            >>> members = Get.getenum_members()
            >>> assert Get.ANNOTATIONS in members.all.values() and Get.ANNOTATIONS in members.private.values() \
            and Get.ANNOTATIONS not in members.protected.values()
            >>> assert Get.LockClass in members.pickle.values() \
            and Get.LockClass not in members.protected.values() and Get.LockClass in members.public.values()
            >>> assert Get._field_defaults in members.protected.values() \
            and Get._field_defaults not in members.public.values()
            >>> assert Get.name in members.public.values() and Get.name not in members.private.values()

        Returns:
            Enum Class Names and Values Dict.
        """
        m = cls.__members__
        access = Access.classify(keys=True, **{cls[k].value_str: v for k, v in m.items()})
        return GetEnumMembers(all=access.all, pickle={k: i for k, i in m.items() if cls[k].is_value_class},
                              private=access.private, protected=access.protected, public=access.public)

    @classmethod
    @functools.cache
    def getenum_pickle_classes(cls):
        """
        Get Pickle Classes.

        Examples:
            >>> pretty_install()
            >>> Get.getenum_pickle_classes()  # doctest: +ELLIPSIS
            (
                ...,
                <class 'environs.Env'>,
                ...
            )

        Returns:
            Tuple of Pickle Classes.
        """
        return tuple(map(lambda x: x.value_class, cls.getenum_members().pickle.values()))

    @classmethod
    @functools.cache
    def getenum_pickle_members_by_class(cls):
        """
        Get Pickle Members by Class.

        Examples:
            >>> pretty_install()
            >>> Get.getenum_pickle_members_by_class()  # doctest: +ELLIPSIS
            {
                ...,
                <class 'environs.Env'>: <Get.Environs: (<class 'environs.Env'>, (...))>,
                ...
            }

        Returns:
            Dict of Pickle Members by Class.
        """
        return dict(map(lambda x: (x.value_class, x), cls.getenum_members().pickle.values()))

    @property
    @functools.cache
    def is_value_class(self):
        return self.is_value_tuple and Es(self.value[0]).type

    @property
    @functools.cache
    def is_value_tuple(self): return Es(self.value).tuple

    @property
    @functools.cache
    def value_class(self): return self.value[0] if self.is_value_class else None

    @property
    @functools.cache
    def value_default(self): return self.value[1] if self.is_value_tuple else tuple()

    @property
    @functools.cache
    def value_str(self): return rv.__name__ if (rv := self.value_class) else self.value[0] \
        if self.is_value_tuple else self.value


class Kind(EnumBase):
    CLASS = 'class method'
    DATA = 'data'
    METHOD = 'method'
    PROPERTY = 'property'
    STATIC = 'static method'


class ModuleBase(EnumBase):
    @property
    @functools.cache
    def get(self): return globals().get(self.value)

    @property
    @functools.cache
    def load(self): return import_module(self.value)


class Module(ModuleBase):
    """Module Enum Class."""
    FUNCTOOLS = auto()
    TYPING = auto()


class NameBase(EnumBase):
    def _generate_next_value_(self, start, count, last_values):
        return f'__{self}' if self.endswith('__') else self.removesuffix('_')


class Name(NameBase):
    """Name Enum Class."""
    all__ = auto()
    class__ = auto()
    annotations__ = auto()
    builtins__ = auto()
    cached__ = auto()
    code__ = auto()
    contains__ = auto()
    dataclass_fields__ = auto()
    dataclass_params__ = auto()
    delattr__ = auto()
    dict__ = auto()
    dir__ = auto()
    doc__ = auto()
    eq__ = auto()
    file__ = auto()
    getattribute__ = auto()
    len__ = auto()
    loader__ = auto()
    members__ = auto()
    module__ = auto()
    mro__ = auto()
    name__ = auto()
    package__ = auto()
    qualname__ = auto()
    reduce__ = auto()
    repr__ = auto()
    setattr__ = auto()
    slots__ = auto()
    spec__ = auto()
    str__ = auto()
    _asdict = auto()
    add = auto()
    append = auto()
    asdict = auto()
    cls_ = auto()  # To avoid conflict with Name.cls
    clear = auto()
    co_name = auto()
    code_context = auto()
    copy = auto()
    count = auto()
    data = auto()
    endswith = auto()
    extend = auto()
    external = auto()
    f_back = auto()
    f_code = auto()
    f_globals = auto()
    f_lineno = auto()
    f_locals = auto()
    filename = auto()
    frame = auto()
    function = auto()
    get_ = auto()  # To avoid conflict with Name.get
    globals = auto()
    index = auto()
    item = auto()
    items = auto()
    keys = auto()
    kind = auto()
    lineno = auto()
    locals = auto()
    name_ = auto()  # To avoid conflict with Enum.name
    origin = auto()
    obj = auto()
    object = auto()
    REPO = auto()
    pop = auto()
    popitem = auto()
    PYPI = auto()
    remove = auto()
    reverse = auto()
    self_ = auto()  # To avoid conflict with Enum
    sort = auto()
    startswith = auto()
    tb_frame = auto()
    tb_lineno = auto()
    tb_next = auto()
    update = auto()
    value_ = auto()  # To avoid conflict with Enum.value
    values = auto()
    vars = auto()

    @classmethod
    @functools.cache
    def _attrs(cls):
        """
        Get map_reduce (dict) attrs lists converted to real names.

        Examples:
            >>> Name._attrs().keys()
            dict_keys([True, False])
            >>> Name._attrs().values()  # doctest: +ELLIPSIS
            dict_values([['__all__', ...], ['_asdict', ...])

        Returns:
            [True]: private attrs.
            [False[: public attrs.
        """
        return map_reduce(cls.__members__, lambda x: x.endswith('__'), lambda x: cls[x].value)

    @classmethod
    @functools.cache
    def attrs(cls):
        """
        Get attrs tuple with private converted to real names.

        Examples:
            >>> pretty_install()
            >>> Name.attrs()  # doctest: +ELLIPSIS
            (
                '__all__',
                ...,
                '_asdict',
                ...
            )

        Returns:
            Tuple of attributes and values.
        """
        return tuple(collapse(Name._attrs().values()))

    # TODO: Name.get()
    @singledispatchmethod
    def get(self, obj: MutableMapping, default=None):
        """
        Get value from GetType/MutableMapping.

        Examples:
            >>> from ast import unparse
            >>> from inspect import getmodulename
            >>>
            >>> pretty_install()
            >>> f = insstack()[0]
            >>> globs_locs = (f.frame.f_globals | f.frame.f_locals).copy()
            >>> Name.filename.get(f), Name.function.get(f), Name.code_context.get(f)[0], Name.source(f)
            (
                PosixPath('<doctest get[7]>'),
                '<module>',
                'f = insstack()[0]\\n',
                'f = insstack()[0]\\n'
            )
            >>> Name.file__.get(globs_locs)  # doctest: +ELLIPSIS
            PosixPath('/Users/jose/....py')
            >>> assert Name.file__.get(globs_locs) == PathLib(__file__) == PathLib(Name.spec__.get(globs_locs).origin)
            >>> assert Name.name__.get(globs_locs) == getmodulename(__file__) == Name.spec__.get(globs_locs).name
            >>> Name.source(globs_locs)  # doctest: +ELLIPSIS
            '# -*- coding: utf-8 -*-\\n...
            >>> Name.source(__file__)  # doctest: +ELLIPSIS
            '# -*- coding: utf-8 -*-\\n...
            >>> assert Name.source(globs_locs) == Name.source(__file__)
            >>> unparse(Name.node(globs_locs)) == unparse(Name.node(__file__))  # Unparse does not have encoding line
            True
            >>> Name.source(f) in unparse(Name.node(globs_locs))
            True
            >>> Name.source(f) in unparse(Name.node(__file__))
            True

        Args:
            obj: object
            default: None

        Returns:
            Value from get() method
        """
        if self is Name.file__:
            return self.path(obj)
        return obj.get(self.value, default)

    @get.register
    def get_getattrtype(self, obj: object, default=None):
        """
        Get value of attribute from GetAttrType.

        Examples:
            >>> from ast import unparse
            >>> from inspect import getmodulename
            >>> import rc.utils
            >>>
            >>> pretty_install()
            >>> f = insstack()[0]
            >>> globs_locs = (f.frame.f_globals | f.frame.f_locals).copy()

            # >>> Name.file__.get(globs_locs)  # doctest: +ELLIPSIS
            # PosixPath('/Users/jose/....py')
            # >>> Name.file__.get(rc.utils)  # doctest: +ELLIPSIS
            # PosixPath('/Users/jose/....py')

            >>> globs_locs.get('__spec__'), Name.spec__.get(globs_locs)

            # >>> PathLib(Name.spec__.get(globs_locs).origin)  # doctest: +ELLIPSIS
            # PosixPath('/Users/jose/....py')
            # >>> PathLib(Name.spec__.get(rc.utils).origin)  # doctest: +ELLIPSIS
            # PosixPath('/Users/jose/....py')
            # >>> Name.spec__.get(rc.utils).name == rc.utils.__name__
            # True
            # >>> Name.spec__.get(rc.utils).name.split('.')[0] == rc.utils.__package__
            # True
            # >>> Name.name__.get(rc.utils) == rc.utils.__name__
            # True
            # >>> Name.package__.get(rc.utils) == rc.utils.__package__
            # True

        Args:
            obj: object
            default: None

        Returns:
            Value from __getattribute__ method.
        """
        ic(obj, isinstance(obj, MutableMapping))
        if self is Name.file__:
            try:
                p = object.__getattribute__(obj, Name.file__.value)
                return PathLib(p)
            except AttributeError:
                return self.path(obj)
        try:
            ic(self.value)
            return object.__getattribute__(obj, self.value)
        except AttributeError:
            return default

    @get.register
    def get_frameinfo(self, obj: FrameInfo, default=None):
        """
        Get value of attribute from FrameInfo.

        Examples:
            >>> from ast import unparse
            >>>
            >>> f = insstack()[0]
            >>> assert f == FrameInfo(Name.frame.get(f), str(Name.filename.get(f)), Name.lineno.get(f),\
            Name.function.get(f), Name.code_context.get(f), Name.index.get(f))
            >>> assert Name.filename.get(f) == Name.file__.get(f)
            >>> Name.source(f)
            'f = insstack()[0]\\n'
            >>> unparse(Name.node(f))
            'f = insstack()[0]'
            >>> unparse(Name.node('pass'))
            'pass'
            >>> assert str(Name.file__.get(f)) == str(Name.filename.get(f))
            >>> assert Name.name__.get(f) == Name.co_name.get(f) == Name.function.get(f)
            >>> assert Name.lineno.get(f) == Name.f_lineno.get(f) == Name.tb_lineno.get(f)
            >>> assert Name.vars.get(f) == (f.frame.f_globals | f.frame.f_locals).copy()
            >>> assert Name.vars.get(f) == (Name.f_globals.get(f) | Name.f_locals.get(f)).copy()
            >>> assert Name.vars.get(f) == (Name.globals.get(f) | Name.locals.get(f)).copy()
            >>> assert unparse(Name.node(f)) in Name.code_context.get(f)[0]
            >>> assert Name.spec__.get(f).origin == __file__

        Args:
            obj: object
            default: None

        Returns:
            Value from FrameInfo method
        """
        if self in [Name.file__, Name.filename]:
            return PathLib(obj.filename)
        if self in [Name.name__, Name.co_name, Name.function]:
            return obj.function
        if self in [Name.lineno, Name.f_lineno, Name.tb_lineno]:
            return obj.lineno
        if self in [Name.f_globals, Name.globals]:
            return obj.frame.f_globals
        if self in [Name.f_locals, Name.locals]:
            return obj.frame.f_locals
        if self in [Name.frame, Name.tb_frame]:
            return obj.frame
        if self is Name.vars:
            return (obj.frame.f_globals | obj.frame.f_locals).copy()
        if self in [Name.code__, Name.f_code]:
            return obj.frame.f_code
        if self in [Name.f_back, Name.tb_next]:
            return obj.frame.f_back
        if self is Name.index:
            return obj.index
        if self is Name.code_context:
            return obj.code_context
        return self.get((obj.frame.f_globals | obj.frame.f_locals).copy(), default=default)

    @get.register
    @functools.cache
    def get_frametype(self, obj: FrameType, default=None):
        """
        Get value of attribute from FrameType.

        Examples:
            >>> from ast import unparse
            >>>
            >>> frameinfo = insstack()[0]
            >>> f = frameinfo.frame
            >>> assert Name.filename.get(f) == Name.filename.get(frameinfo)
            >>> assert Name.frame.get(f) == Name.frame.get(frameinfo)
            >>> assert Name.lineno.get(f) == Name.lineno.get(frameinfo)
            >>> assert Name.function.get(f) == Name.function.get(frameinfo)
            >>> assert frameinfo == FrameInfo(Name.frame.get(f), str(Name.filename.get(f)), Name.lineno.get(f),\
            Name.function.get(f), frameinfo.code_context, frameinfo.index)
            >>> assert Name.filename.get(f) == Name.file__.get(f)
            >>> Name.source(f)
            'frameinfo = insstack()[0]\\n'
            >>> unparse(Name.node(f))
            'frameinfo = insstack()[0]'
            >>> unparse(Name.node('pass'))
            'pass'
            >>> assert str(Name.file__.get(f)) == str(Name.filename.get(f))
            >>> assert Name.name__.get(f) == Name.co_name.get(f) == Name.function.get(f)
            >>> assert Name.lineno.get(f) == Name.f_lineno.get(f) == Name.tb_lineno.get(f)
            >>> assert Name.vars.get(f) == (f.f_globals | f.f_locals).copy()
            >>> assert Name.vars.get(f) == (Name.f_globals.get(f) | Name.f_locals.get(f)).copy()
            >>> assert Name.vars.get(f) == (Name.globals.get(f) | Name.locals.get(f)).copy()
            >>> assert unparse(Name.node(f)) in Name.code_context.get(frameinfo)[0]
            >>> assert Name.spec__.get(f).origin == __file__

        Args:
            obj: object
            default: None

        Returns:
            Value from FrameType method
        """
        if self in [Name.file__, Name.filename]:
            return self.path(obj)
        if self in [Name.name__, Name.co_name, Name.function]:
            return obj.f_code.co_name
        if self in [Name.lineno, Name.f_lineno, Name.tb_lineno]:
            return obj.f_lineno
        if self in [Name.f_globals, Name.globals]:
            return obj.f_globals
        if self in [Name.f_locals, Name.locals]:
            return obj.f_locals
        if self in [Name.frame, Name.tb_frame]:
            return obj
        if self is Name.vars:
            return (obj.f_globals | obj.f_locals).copy()
        if self in [Name.code__, Name.f_code]:
            return obj.f_code
        if self in [Name.f_back, Name.tb_next]:
            return obj.f_back
        return self.get((obj.f_globals | obj.f_locals).copy(), default=default)

    @get.register
    @functools.cache
    def get_tracebacktype(self, obj: TracebackType, default=None):
        """
        Get value of attribute from TracebackType.

        Args:
            obj: object
            default: None

        Returns:
            Value from TracebackType method
        """
        if self in [Name.file__, Name.filename]:
            return self.path(obj)
        if self in [Name.name__, Name.co_name, Name.function]:
            return obj.tb_frame.f_code.co_name
        if self in [Name.lineno, Name.f_lineno, Name.tb_lineno]:
            return obj.tb_lineno
        if self in [Name.f_globals, Name.globals]:
            return obj.tb_frame.f_globals
        if self in [Name.f_locals, Name.locals]:
            return obj.tb_frame.f_locals
        if self in [Name.frame, Name.tb_frame]:
            return obj.tb_frame
        if self is Name.vars:
            return (obj.tb_frame.f_globals | obj.tb_frame.f_locals).copy()
        if self in [Name.code__, Name.f_code]:
            return obj.tb_frame.f_code
        if self in [Name.f_back, Name.tb_next]:
            return obj.tb_next
        return self.get((obj.tb_frame.f_globals | obj.tb_frame.f_locals).copy(), default=default)

    @property
    def getter(self):
        """
        Attr getter with real name for private and public which conflicts with Enum.

        Examples:
            >>> import rc.utils
            >>>
            >>> Name.module__.getter(tuple)
            'builtins'
            >>> Name.name__.getter(tuple)
            'tuple'
            >>> Name.file__.getter(rc.utils)  # doctest: +ELLIPSIS
            '/Users/jose/....py'

        Returns:
            Attr getter with real name for private and public which conflicts with Enum.
        """
        return attrgetter(self.value)

    def has(self, obj):
        """
        Checks if has attr with real name for private and public which conflicts with Enum.

        Examples:
            >>> import rc.utils
            >>>
            >>> Name.module__.has(tuple)
            True
            >>> Name.name__.has(tuple)
            True
            >>> Name.file__.has(tuple)
            False
            >>> Name.file__.has(rc.utils)
            True

        Returns:
            Checks if has attr with real name for private and public which conflicts with Enum.
        """
        return hasattr(obj, self.value)

    @classmethod
    def node(cls, obj, complete=False, line=False):
        """
        Get node of object.

        Examples:
            >>> from ast import unparse
            >>> from inspect import getmodulename
            >>>
            >>> pretty_install()
            >>> f = insstack()[0]
            >>> globs_locs = (f.frame.f_globals | f.frame.f_locals).copy()
            >>> Name.filename.get(f), Name.function.get(f), Name.code_context.get(f)[0], Name.source(f) \
             # doctest: +ELLIPSIS
            (
                PosixPath('<doctest ...node[...]>'),
                '<module>',
                'f = insstack()[0]\\n',
                'f = insstack()[0]\\n'
            )
            >>> Name.file__.get(globs_locs)  # doctest: +ELLIPSIS
            PosixPath('/Users/jose/....py')
            >>> assert Name.file__.get(globs_locs) == PathLib(__file__) == PathLib(Name.spec__.get(globs_locs).origin)
            >>> assert Name.name__.get(globs_locs) == getmodulename(__file__) == Name.spec__.get(globs_locs).name
            >>> Name.source(globs_locs)  # doctest: +ELLIPSIS
            '# -*- coding: utf-8 -*-\\n...
            >>> Name.source(__file__)  # doctest: +ELLIPSIS
            '# -*- coding: utf-8 -*-\\n...
            >>> assert Name.source(globs_locs) == Name.source(__file__)
            >>> unparse(Name.node(globs_locs)) == unparse(Name.node(__file__))  # Unparse does not have encoding line
            True
            >>> Name.source(f) in unparse(Name.node(globs_locs))
            True
            >>> Name.source(f) in unparse(Name.node(__file__))
            True

        Args:
            obj: object.
            complete: return complete node for file (always for module and frame corresponding to module)
                or object node (default=False)
            line: return line

        Returns:
            Node.
        """
        return ast.parse(cls.source(obj, complete, line) or str(obj))

    @classmethod
    def path(cls, obj):
        """
        Get path of object.

        Examples:
            >>> from ast import unparse
            >>> from inspect import getmodulename
            >>>
            >>> pretty_install()
            >>> frameinfo = insstack()[0]
            >>> globs_locs = (frameinfo.frame.f_globals | frameinfo.frame.f_locals).copy()
            >>> Name.path(Name.path)  # doctest: +ELLIPSIS
            PosixPath('/Users/jose/....py')
            >>> Name.path(__file__)  # doctest: +ELLIPSIS
            PosixPath('/Users/jose/....py')
            >>> Name.path(allin)  # doctest: +ELLIPSIS
            PosixPath('/Users/jose/....py')
            >>> Name.path(dict(a=1))
            PosixPath("{'a': 1}")

        Args:
            obj: object.

        Returns:
            Path.
        """
        es = Es(obj)
        if es.mm:
            f = obj.get(Name.file__.value)
        elif es.frameinfo:
            f = obj.filename
        else:
            try:
                f = getsourcefile(obj) or getfile(obj)
            except TypeError:
                f = None
        return PathLib(f or str(obj))

    @classmethod
    @functools.cache
    def private(cls):
        """
        Get private attrs tuple converted to real names.

        Examples:
            >>> pretty_install()
            >>> Name.private()  # doctest: +ELLIPSIS
            (
                '__all__',
                ...
            )

        Returns:
            Tuple of private attrs converted to real names.
        """
        return tuple(cls._attrs()[True])

    @classmethod
    @functools.cache
    def public(cls):
        """
        Get public attrs tuple.

        Examples:
            >>> pretty_install()
            >>> Name.public()  # doctest: +ELLIPSIS
            (
                '_asdict',
                ...
            )

        Returns:
            Tuple of public attrs.
        """
        return tuple(cls._attrs()[False])

    @classmethod
    def _source(cls, obj, line=False):
        f = cls.file__.get(obj) or obj
        if (p := PathLib(f)).is_file():
            if s := token_open(p):
                if line:
                    return s, 1
                return s

    @classmethod
    def source(cls, obj, complete=False, line=False):
        """
        Get source of object.

        Examples:
            >>> from ast import unparse
            >>> from inspect import getmodulename
            >>> import rc.utils
            >>>
            >>> pretty_install()
            >>>
            >>> Name.source(__file__)  # doctest: +ELLIPSIS
            '# -*- coding: utf-8 -*-\\n...
            >>> Name.source(__file__, complete=True)  # doctest: +ELLIPSIS
            '# -*- coding: utf-8 -*-\\n...
            >>>
            >>> Name.source(Name.source)  # doctest: +ELLIPSIS
            '    @classmethod\\n    def source(cls, obj, complete=False, line=False):\\n...'
            >>> Name.source(Name.source, complete=True)  # doctest: +ELLIPSIS
            '# -*- coding: utf-8 -*-\\n...
            >>> Name.source(Name.source).splitlines()[1] in Name.source(Name.source, complete=True)
            True
            >>>
            >>> Name.source(allin)  # doctest: +ELLIPSIS
            'def allin(origin, destination):\\n...'
            >>> Name.source(allin, line=True)  # doctest: +ELLIPSIS
            (
                'def allin(origin, destination):\\n...',
                ...
            )
            >>> Name.source(allin, complete=True)  # doctest: +ELLIPSIS
            '# -*- coding: utf-8 -*-\\n...
            >>> Name.source(allin, complete=True, line=True)  # doctest: +ELLIPSIS
            (
                '# -*- coding: utf-8 -*-\\n...,
                ...
            )
            >>> Name.source(allin).splitlines()[0] in Name.source(allin, complete=True)
            True
            >>>
            >>> Name.source(dict(a=1))
            "{'a': 1}"
            >>> Name.source(dict(a=1), complete=True)
            "{'a': 1}"
            >>>
            >>> Name.source(rc.utils)  # doctest: +ELLIPSIS
            '# -*- coding: utf-8 -*-\\n...
            >>> Name.source(rc.utils, complete=True)  # doctest: +ELLIPSIS
            '# -*- coding: utf-8 -*-\\n...
            >>>
            >>> frameinfo = insstack()[0]
            >>> Name.source(frameinfo), frameinfo.function
            ('frameinfo = insstack()[0]\\n', '<module>')
            >>> Name.source(frameinfo, complete=True), frameinfo.function
            ('frameinfo = insstack()[0]\\n', '<module>')
            >>>
            >>> frametype = frameinfo.frame
            >>> Name.source(frametype), frametype.f_code.co_name
            ('frameinfo = insstack()[0]\\n', '<module>')
            >>> Name.source(frameinfo, complete=True), frametype.f_code.co_name
            ('frameinfo = insstack()[0]\\n', '<module>')
            >>>
            >>> Name.source(None)
            'None'

        Args:
            obj: object.
            complete: return complete source file (always for module and frame corresponding to module)
                or object source (default=False)
            line: return line

        Returns:
            Source.
        """
        es = Es(obj)
        if any([es.moduletype, (es.frameinfo and obj.function == FUNCTION_MODULE),
                (es.frametype and obj.f_code.co_name == FUNCTION_MODULE) or
                (es.tracebacktype and obj.tb_frame.f_code.co_name == FUNCTION_MODULE) or
                complete]):
            if source := cls._source(obj, line):
                return source

        try:
            if line:
                lines, lnum = getsourcelines(obj.frame if es.frameinfo else obj)
                return ''.join(lines), lnum
            return getsource(obj.frame if es.frameinfo else obj)
        except (OSError, TypeError):
            if source := cls._source(obj, line):
                return source
            if line:
                return str(obj), 1
            return str(obj)


class PrivateBase(EnumBase):
    """Access Types Base Enum Class."""

    def _generate_next_value_(self, start, count, last_values):
        return f'__{self.lower()}__'

    def _get(self, obj, default=None):
        return obj.get(self.value, default)

    def getattr(self, obj, default=None):
        return obj.get(self.value, default)
    def get(self, obj, default=None):
        es = Es(obj)
        if es.mm:
            if self is Private.FILE

    @property
    @functools.cache
    def getter(self):
        """Attr Getter."""
        return attrgetter(self.value)

    def has(self, obj):
        """
        Checks if Object has attr.

        Examples:
            >>> from rc import Es, Private, pretty_install
            >>> pretty_install()
            >>>
            >>> class Test:
            ...     __repr_newline__ = True
            >>>
            >>> Private.REPR_NEWLINE.has(Test())
            True
            >>> Private.REPR_EXCLUDE.has(Test())
            False

        Args:
            obj: object.

        Returns:
            True if object has attribute.
        """
        return Es(obj).has(self)

    def mro_first_data(self, obj):
        """
        First value of attr found in mro and instance if obj is instance.

        Examples:
            >>> pretty_install()
            >>>
            >>> class Test:
            ...     __repr_newline__ = True
            >>>
            >>> test = Test()
            >>> class Test2(Test):
            ...     def __init__(self):
            ...         self.__repr_newline__ = False
            >>>
            >>> Private.REPR_NEWLINE.mro_first_data(Test())
            True
            >>> Private.REPR_NEWLINE.mro_first_data(Test2())
            False
            >>> Private.REPR_NEWLINE.mro_first_data(int())
            >>> Private.REPR_PPROPERTY.mro_first_data(Test())

        Returns:
            First value of attr found in mro and instance if obj is instance.
        """
        return Es(obj).mro_first_data(self)

    def mro_first_dict(self, obj):
        """
        First value of attr in obj.__class__.__dict__ found in mro.

        Examples:
            >>> pretty_install()
            >>>
            >>> class Test:
            ...     __repr_newline__ = False
            >>>
            >>> test = Test()
            >>> class Test2(Test):
            ...     def __init__(self):
            ...         self.__repr_newline__ = False
            >>>
            >>> Private.REPR_NEWLINE.mro_first_dict(Test())
            False
            >>> Private.REPR_NEWLINE.mro_first_dict(Test2())
            False
            >>> Private.REPR_NEWLINE.mro_first_dict(int())
            NotImplemented
            >>> Private.REPR_PPROPERTY.mro_first_dict(Test())
            NotImplemented
            >>> A = namedtuple('A', 'a')
            >>> Private.SLOTS.mro_first_dict(A)
            ()

        Returns:
            First value of attr in obj.__class__.__dict__ found in mro.
        """
        return Es(obj).mro_first_dict(self)

    def mro_first_dict_no_object(self, obj):
        """
        First value of attr in obj.__class__.__dict__ found in mro excluding object.

        Examples:
            >>> pretty_install()
            >>>
            >>> class Test:
            ...     __repr_newline__ = False
            >>>
            >>> test = Test()
            >>> class Test2(Test):
            ...     def __init__(self):
            ...         self.__repr_newline__ = False
            >>>
            >>> Private.REPR_NEWLINE.mro_first_dict_no_object(Test())
            False
            >>> Private.REPR_NEWLINE.mro_first_dict_no_object(Test2())
            False
            >>> Private.REPR_NEWLINE.mro_first_dict_no_object(int())
            NotImplemented
            >>> Private.REPR_PPROPERTY.mro_first_dict_no_object(Test())
            NotImplemented
            >>> A = namedtuple('A', 'a')
            >>> Private.SLOTS.mro_first_dict_no_object(A)
            ()
            >>> Private.SLOTS.mro_first_dict_no_object(dict)
            NotImplemented
            >>> Private.SLOTS.mro_first_dict_no_object(dict())
            NotImplemented

        Returns:
            First value of attr in obj.__class__.__dict__ found in mro excluding object.
        """
        return Es(obj).mro_first_dict_no_object(self)

    def mro_values(self, obj):
        """
        All/accumulated values of attr in mro and obj if instance.

        Examples:
            >>> pretty_install()
            >>>
            >>> class First:
            ...     __slots__ = ('_hash', '_repr')
            ...     __ignore_copy__ = (tuple, )
            ...     __repr_exclude__ = ('_repr', )
            >>>
            >>> class Test(First):
            ...     __slots__ = ('_prop', '_slot', )
            ...     __hash_exclude__ = ('_slot', )
            ...     __ignore_attr__ = ('attr', )
            ...     __ignore_kwarg__ = ('kwarg', )
            ...     __ignore_str__ = (tuple, )
            >>>
            >>> test = Test()
            >>> Private.HASH_EXCLUDE.mro_values(test)
            ('_slot',)
            >>> Private.IGNORE_ATTR.mro_values(test)  # doctest: +ELLIPSIS
            (
                'asdict',
                'attr',
                ...
            )
            >>> set(Private.IGNORE_COPY.mro_values(test)).difference(Private.IGNORE_COPY.mro_values_default(test))
            {<class 'tuple'>}
            >>> Private.IGNORE_KWARG.mro_values(test)
            ('kwarg',)
            >>> set(Private.IGNORE_STR.mro_values(test)).difference(Private.IGNORE_STR.mro_values_default(test))
            {<class 'tuple'>}
            >>> Private.REPR_EXCLUDE.mro_values(test)
            ('_repr',)
            >>> Private.SLOTS.mro_values(test)
            ('_hash', '_prop', '_repr', '_slot')
            >>> assert sorted(Private.PICKLE.mro_values(Environs())) == sorted(PICKLE_ATTRS[Environs])

        Returns:
            All/accumulated values of attr in mro and obj if instance.
        """
        return Es(obj).mro_values(self)

    @functools.cache
    def mro_values_default(self, obj):
        """
        Default values for attr in mro and instance.

        Examples:
            >>> from rc import Es, pretty_install
            >>> pretty_install()
            >>>
            >>> class First:
            ...     __slots__ = ('_hash', '_repr')
            ...     __ignore_copy__ = (tuple, )
            ...     __repr_exclude__ = ('_repr', )
            >>>
            >>> class Test(First):
            ...     __slots__ = ('_prop', '_slot', )
            ...     __hash_exclude__ = ('_slot', )
            ...     __ignore_attr__ = ('attr', )
            ...     __ignore_kwarg__ = ('kwarg', )
            ...     __ignore_str__ = (tuple, )
            >>>
            >>> test = Test()
            >>> assert Private.HASH_EXCLUDE.mro_values_default(test) == tuple()
            >>> assert Private.IGNORE_ATTR.mro_values_default(test) == IgnoreAttr.__args__
            >>> assert Private.IGNORE_COPY.mro_values_default(test) == IgnoreCopy.__args__
            >>> assert Private.IGNORE_KWARG.mro_values_default(test) == tuple()
            >>> assert Private.IGNORE_STR.mro_values_default(test) == IgnoreStr.__args__
            >>> assert Private.REPR_EXCLUDE.mro_values_default(test) == tuple()
            >>> assert Private.SLOTS.mro_values_default(test) == tuple()
            >>> assert sorted(Private.PICKLE.mro_values_default(Environs())) == sorted(PICKLE_ATTRS[Environs])

        Returns:
           Default values for attr in mro and instance.
        """
        return Es(obj).mro_values_default(self)

    def slot(self, obj):
        """
        Is attribute in slots?

        Examples:
            >>> pretty_install()
            >>>
            >>> class First:
            ...     __slots__ = ('_data', )
            >>>
            >>> class Test(First):
            ...     __slots__ = ('_id', )
            >>>
            >>> Protected.DATA.slot(Test())
            True
            >>> Protected.ID.slot(Test())
            True
            >>> Public.IP.slot(Test())
            False

        Args:
            obj: object.

        Returns:
            True if attribute in slots
        """
        return Es(obj).slot(self)

    def slots_include(self, obj):
        """
        Accumulated values from slots - Accumulated values from mro attr name.

        Examples:
            >>> pretty_install()
            >>>
            >>> class First:
            ...     __slots__ = ('_hash', )
            >>>
            >>> class Test(First):
            ...     __slots__ = ('_prop', '_repr', '_slot', )
            ...     __hash_exclude__ = ('_slot', )
            ...     __repr_exclude__ = ('_repr', )
            >>>
            >>> test = Test()
            >>> slots = Private.SLOTS.mro_values(test)
            >>> slots
            ('_hash', '_prop', '_repr', '_slot')
            >>> hash_attrs = Private.HASH_EXCLUDE.slots_include(test)
            >>> hash_attrs
            ('_hash', '_prop', '_repr')
            >>> sorted(hash_attrs + Private.HASH_EXCLUDE.mro_values(test)) == sorted(slots)
            True
            >>> repr_attrs = Private.REPR_EXCLUDE.slots_include(test)
            >>> repr_attrs
            ('_hash', '_prop', '_slot')
            >>> sorted(repr_attrs + Private.REPR_EXCLUDE.mro_values(test)) == sorted(slots)
            True

        Returns:
            Accumulated values from slots - Accumulated values from mro attr name.
        """
        return Es(obj).slots_include(self)


class Private(PrivateBase):
    """Private Access Attributes Enum Class.."""
    ALL = auto()
    ANNOTATIONS = auto()
    ARGS = auto()
    ASDICT = auto()
    BUILTINS = auto()
    CACHE_CLEAR = auto()
    CACHE_INFO = auto()
    CACHED = auto()
    CODE = auto()
    CONTAINS = auto()
    DATACLASS_FIELDS = auto()
    DATACLASS_PARAMS = auto()
    DELATTR = auto()
    DICT = auto()
    DIR = auto()
    DOC = auto()
    EQ = auto()
    FILE = auto()
    GET = auto()
    GETATTRIBUTE = auto()
    GETITEM = auto()
    GETSTATE = auto()
    HASH_EXCLUDE = auto()
    IGNORE_ATTR = auto()
    IGNORE_COPY = auto()
    IGNORE_KWARG = auto()
    IGNORE_STR = auto()
    INIT = auto()
    INIT_SUBCLASS = auto()
    LEN = auto()
    LOADER = auto()
    MEMBERS = auto()
    MODULE = auto()
    MRO = auto()
    NAME = auto()
    PACKAGE = auto()
    PICKLE = auto()
    POST_INIT = auto()
    QUALNAME = auto()
    REDUCE = auto()
    REDUCE_EX = auto()
    REPR = auto()
    REPR_EXCLUDE = auto()
    REPR_NEWLINE = auto()
    REPR_PPROPERTY = auto()
    SETATTR = auto()
    SETSTATE = auto()
    SLOTS = auto()
    SPEC = auto()
    STR = auto()
    SUBCLASSHOOK = auto()


class ProtectedBase(PrivateBase):
    def _generate_next_value_(self, start, count, last_values):
        return f'_{self.lower()}'


class Protected(ProtectedBase):
    """Protected Access Attributes Enum Class."""
    ASDICT = auto()
    CLS = auto()
    COPY = auto()
    COUNT = auto()
    DATA = auto()
    EXTEND = auto()
    EXTERNAL = auto()
    FIELD_DEFAULTS = auto()
    FIELDS = auto()
    FILE = auto()
    FILENAME = auto()
    FRAME = auto()
    FUNC = auto()
    FUNCTION = auto()
    GET = auto()
    GLOBALS = auto()
    ID = auto()
    INDEX = auto()
    IP = auto()
    ITEM = auto()
    ITEMS = auto()
    KEY = auto()
    KEYS = auto()
    KIND = auto()
    LOCALS = auto()
    NAME = auto()
    ORIGIN = auto()
    OBJ = auto()
    OBJECT = auto()
    PATH = auto()
    REPO = auto()
    RV = auto()
    PYPI = auto()
    REMOVE = auto()
    REVERSE = auto()
    SORT = auto()
    UPDATE = auto()
    VALUE = auto()
    VALUES = auto()
    VARS = auto()


class PublicBase(PrivateBase):
    def _generate_next_value_(self, start, count, last_values):
        return self.lower()


class Public(PublicBase):
    """Public Access Attributes Enum Class."""
    ADD = auto()
    APPEND = auto()
    ASDICT = auto()
    CLS = auto()
    CLEAR = auto()
    CO_NAME = auto()
    CODE_CONTEXT = auto()
    COPY = auto()
    COUNT = auto()
    DATA = auto()
    ENDSWITH = auto()
    EXTEND = auto()
    EXTERNAL = auto()
    F_BACK = auto()
    F_CODE = auto()
    F_GLOBALS = auto()
    F_LINENO = auto()
    F_LOCALS = auto()
    FILE = auto()
    FILENAME = auto()
    FRAME = auto()
    FUNC = auto()
    FUNCTION = auto()
    GET = auto()
    GLOBALS = auto()
    ID = auto()
    INDEX = auto()
    IP = auto()
    ITEM = auto()
    ITEMS = auto()
    KEY = auto()
    KEYS = auto()
    KIND = auto()
    LINENO = auto()
    LOCALS = auto()
    NAME = auto()
    ORIGIN = auto()
    OBJ = auto()
    OBJECT = auto()
    PATH = auto()
    REPO = auto()
    RV = auto()
    POP = auto()
    POPITEM = auto()
    PYPI = auto()
    REMOVE = auto()
    REVERSE = auto()
    SELF = auto()
    SORT = auto()
    STARTSWITH = auto()
    TB_FRAME = auto()
    TB_LINENO = auto()
    TB_NEXT = auto()
    UPDATE = auto()
    VALUE = auto()
    VALUES = auto()
    VARS = auto()


# </editor-fold>
# <editor-fold desc="Enums - Typing">
AttrUnion = Union[str, Private, Protected, Public]
EnumBaseAlias = Alias(EnumBase, 1, name=EnumBase.__name__)


# </editor-fold>
# <editor-fold desc="Functions">
def aioloop(): return noexception(RuntimeError, get_running_loop)


def allin(origin, destination):
    """
    Checks all items in origin are in destination iterable.

    Examples:
        >>> class Int(int):
        ...     pass
        >>> allin(tuple.__mro__, BUILTINS_CLASSES)
        True
        >>> allin(Int.__mro__, BUILTINS_CLASSES)
        False
        >>> allin('tuple int', 'bool dict int')
        False
        >>> allin('bool int', ['bool', 'dict', 'int'])
        True
        >>> allin(['bool', 'int'], ['bool', 'dict', 'int'])
        True

    Args:
        origin: origin iterable.
        destination: destination iterable to check if origin items are in.

    Returns:
        True if all items in origin are in destination.
    """
    origin = to_iter(origin)
    destination = to_iter(destination)
    return all(map(lambda x: x in destination, origin))


def annotations(obj, stack=1, sequence=False):
    """
    Formats obj annotations.

    Examples:
        >>> from dataclasses import dataclass
        >>>
        >>> pretty_install()
        >>>
        >>> @dataclass
        ... class Test:
        ...     any: Any = 'any'
        ...     classvar: ClassVar[str] = 'classvar'
        ...     classvar_optional: ClassVar[Optional[str]] = 'classvar_optional'
        ...     classvar_optional_union: ClassVar[Optional[Union[str, int]]] = 'classvar_optional_union'
        ...     classvar_union: ClassVar[Union[str, int]] = 'classvar_union'
        ...     final: Final= 'final'
        ...     final_str: Final[str] = 'final_str'
        ...     integer: int = 1
        ...     initvar: InitVar[str] = 'initvar'
        ...     initvar_optional: InitVar[Optional[str]] = 'initvar_optional'
        ...     literal: Literal['literal', 'literal2'] = 'literal2'
        ...     literal_optional: Optional[Literal['literal_optional', 'literal_optional2']] = 'literal_optional2'
        ...     optional: Optional[str] = 'optional'
        ...     union: Union[str, int] = 1
        ...     optional_union: Optional[Union[str, bool]] = True
        ...     def __post_init__(self, initvar: int, initvar_optional: Optional[int]):
        ...         self.a = initvar
        >>>
        >>> ann = annotations(Test, sequence=False)
        >>> ann['any'].any, ann['any'].cls, ann['any'].default
        (True, typing.Any, None)
        >>> ann['classvar'].classvar, ann['classvar'].cls, ann['classvar'].default
        (True, <class 'str'>, '')
        >>> ann['classvar_optional'].classvar, ann['classvar_optional'].cls, ann['classvar_optional'].default
        (True, <class 'str'>, '')
        >>> ann['classvar_optional_union'].classvar, ann['classvar_optional_union'].cls, \
        ann['classvar_optional_union'].default
        (True, <class 'str'>, '')
        >>> ann['classvar_union'].classvar, ann['classvar_union'].cls, ann['classvar_union'].default
        (True, <class 'str'>, '')
        >>> ann['final'].final, ann['final'].cls, ann['final'].default  # TODO: 'final'
        (True, typing.Final, None)
        >>> ann['final_str'].final, ann['final_str'].cls, ann['final_str'].default  # TODO: 'final_str'
        (True, <class 'str'>, '')
        >>> ann['integer'].cls, ann['integer'].default
        (<class 'int'>, 0)
        >>> ann['initvar'].initvar, ann['initvar'].cls, ann['initvar'].default
        (True, <class 'str'>, '')
        >>> ann['initvar_optional'].initvar, ann['initvar_optional'].cls, ann['initvar_optional'].default
        (True, <class 'str'>, '')
        >>> ann['literal'].literal, ann['literal'].cls, ann['literal'].default
        (True, <class 'str'>, 'literal')
        >>> ann['literal_optional'].literal, ann['literal_optional'].cls, ann['literal_optional'].default
        (True, <class 'str'>, 'literal_optional')
        >>> ann['optional'].optional, ann['optional'].cls, ann['optional'].default
        (True, <class 'str'>, '')
        >>> ann['union'].union, ann['union'].cls, ann['union'].default
        (True, <class 'str'>, '')
        >>> ann['optional_union'].optional, ann['optional_union'].union, ann['optional_union'].cls, \
        ann['optional_union'].default
        (True, True, <class 'str'>, '')

    Args:
        obj: object.
        stack: stack index to extract globals and locals (default: 1) or frame.
        sequence: return sequence instead of dict (default: False).

    Returns:
        Annotation: obj annotations. Default are filled with annotation not with class default.
    """

    def value(_cls):
        # TODO: 1) default from annotations, 2) value from kwargs or class defaults.
        return noexception(_cls)

    def inner(_hint):
        cls = _hint
        default = None
        args = list(get_args(_hint))
        _annotations = list()
        origin = get_origin(_hint)
        literal = origin == Literal
        final = origin == Final or _hint == Final
        _any = _hint == Any
        union = origin == Union
        classvar = origin == ClassVar
        # TODO: Look because origin must be InitVar and then  ...
        initvar = Es(cls).initvar
        optional = type(None) in args
        if initvar:
            if isinstance(_hint.type, type):
                cls = _hint.type
                default = value(cls)
            else:
                _hint = _hint.type
                _a = inner(_hint)
                _annotations.append(_a)
                default = _a.default
                cls = _a.cls
        elif origin is None:
            cls = _hint
            # TODO: final (now: None) -> default: 'final'  # hint == Final and origin is None
            default = None if _any or final else value(cls)
        elif literal and args:
            default = args[0]  # TODO: o default or kwarg or None if Optional(?)
            cls = type(default)
        elif final and args:  # origin == Final
            cls = args[0]
            # TODO: final (now: '') -> default: 'final_str'
            default = cls()
        elif args:
            literal = Literal._name in repr(_hint)
            for arg in args:
                if Es(arg).none:
                    _annotations.append(None)
                else:
                    _a = inner(arg)
                    _annotations.append(_a)
            data = _annotations[1] if _annotations[0] is None else _annotations[0]
            default = data.default
            cls = data.cls
        return Annotation(any=_any, args=_annotations or args, classvar=classvar, cls=cls, default=default,
                          final=final, hint=_hint, initvar=initvar, literal=literal, name=name,
                          optional=optional, origin=origin, union=union)

    frame = stack if Es(stack).frametype else insstack()[stack].frame
    rv = dict()
    if a := noexception(get_type_hints, obj, globalns=frame.f_globals, localns=frame.f_locals):
        for name, hint in a.items():
            rv |= {name: inner(hint)}
    rv = dict_sort(rv)
    return list(rv.values()) if sequence else rv


def annotations_init(cls, stack=2, optional=True, **kwargs):
    """
    Init with defaults or kwargs an annotated class.

    Examples:
        >>> NoInitValue = NamedTuple('NoInitValue', var=str)

        >>> A = NamedTuple('A', module=str, path=Optional[PathLib], test=Optional[NoInitValue])
        >>> annotations_init(A, optional=False)
        A(module='', path=None, test=None)
        >>> annotations_init(A)
        A(module='', path=PosixPath('.'), test=None)
        >>> annotations_init(A, test=NoInitValue('test'))
        A(module='', path=PosixPath('.'), test=NoInitValue(var='test'))
        >>> annotations_init(A, optional=False, test=NoInitValue('test'))
        A(module='', path=None, test=NoInitValue(var='test'))

    Args:
        cls: NamedTuple cls.
        stack: stack index to extract globals and locals (default: 2) or frame.
        optional: True to use args[0] instead of None as default for Optional fallback to None if exception.
        **kwargs:

    Returns:
        cls: cls instance with default values.
    """
    values = dict()
    for name, a in annotations(cls, stack=stack, sequence=False).items():
        if v := kwargs.get(name):
            value = v
        elif a.origin == Union and not optional:
            value = None
        else:
            value = a.default
        values[name] = value
    # for name, a in annotations(cls).items():
    #     value = None
    #     if v := kwargs.get(name):
    #         value = v
    #     elif a.origin == Literal:
    #         value = a.args[0]
    #     elif a.origin == Union and not optional:
    #         pass
    #     else:
    #         with suppress(Exception):
    #             value = (a.cls if a.origin is None else a.args[1] if a.args[0] is None else a.args[0])()
    #     rv[name] = value
    with suppress(Exception):
        return cls(**values)


def anyin(origin, destination):
    """
    Checks any item in origin are in destination iterable and return the first found.

    Examples:
        >>> class Int(int):
        ...     pass
        >>> anyin(tuple.__mro__, BUILTINS_CLASSES)
        <class 'tuple'>
        >>> assert anyin('tuple int', BUILTINS_CLASSES) is None
        >>> anyin('tuple int', 'bool dict int')
        'int'
        >>> anyin('tuple int', ['bool', 'dict', 'int'])
        'int'
        >>> anyin(['tuple', 'int'], ['bool', 'dict', 'int'])
        'int'

    Args:
        origin: origin iterable.
        destination: destination iterable to check if any of origin items are in.

    Returns:
        First found if any item in origin are in destination.
    """
    origin = to_iter(origin)
    destination = to_iter(destination)
    return first_true(origin, pred=lambda x: x in destination)


def cache(func):
    """
    Caches previous calls to the function if object is pickable.

    Examples:
        >>>
    """
    cache.enabled = True
    cache.memo = dict()
    if func not in cache.memo:
        cache.memo[func] = dict()

    def cache_info():
        """
        Cache Wrapper Info.

        Returns:
            Cache Wrapper Info.
        """
        return CacheWrapperInfo(wrapper.cache_hit, wrapper.cache_passed, wrapper.cache_total)

    def cache_clear():
        """Clear Cache."""
        wrapper.cache_hit = 0
        wrapper.cache_passed = 0
        wrapper.cache_total = 0
        del cache.memo[func]
        cache.memo[func] = dict()

    @wraps(func)
    def wrapper(*args, **kwargs):
        """Cache Wrapper."""
        wrapper.cache_total += 1
        if cache.enabled:
            try:
                key = Es((args, kwargs, )).pickles
                if key not in cache.memo[func]:
                    wrapper.cache_hit += 1
                    cache.memo[func][key] = func(*args, **kwargs)
                else:
                    wrapper.cache_passed += 1
                value = cache.memo[func][key]
            except Exception as exception:
                red(f'{func=}({args}, {kwargs}) not cached: {exception}')
                wrapper.cache_hit += 1
                value = func(*args, **kwargs)
        else:
            wrapper.cache_hit += 1
            value = func(*args, **kwargs)
        return value

    wrapper.cache_hit = 0
    wrapper.cache_passed = 0
    wrapper.cache_total = 0
    wrapper.cache_clear = cache_clear
    wrapper.cache_info = cache_info

    return wrapper


def cmd(command, exc=False, lines=True, shell=True, py=False, pysite=True):
    """
    Runs a cmd.

    Examples:
        >>> cmd('ls a')
        CompletedProcess(args='ls a', returncode=1, stdout=[], stderr=['ls: a: No such file or directory'])
        >>> assert 'Requirement already satisfied' in cmd('pip install pip', py=True).stdout[0]
        >>> cmd('ls a', shell=False, lines=False)  # Extra '\' added to avoid docstring error.
        CompletedProcess(args=['ls', 'a'], returncode=1, stdout='', stderr='ls: a: No such file or directory\\n')
        >>> cmd('echo a', lines=False)  # Extra '\' added to avoid docstring error.
        CompletedProcess(args='echo a', returncode=0, stdout='a\\n', stderr='')

    Args:
        command: command.
        exc: raise exception.
        lines: split lines so ``\\n`` is removed from all lines (extra '\' added to avoid docstring error).
        py: runs with python executable.
        shell: expands shell variables and one line (shell True expands variables in shell).
        pysite: run on site python if running on a VENV.

    Returns:
        Union[CompletedProcess, int, list, str]: Completed process output.

    Raises:
        CmdError:
   """
    if py:
        m = '-m'
        if isinstance(command, str) and command.startswith('/'):
            m = str()
        command = f'{str(PYTHON_SITE) if pysite else str(PYTHON_SYS)} {m} {command}'
    elif not shell:
        command = to_iter(command)

    if lines:
        text = False
    else:
        text = True

    proc = subprocess.run(command, shell=shell, capture_output=True, text=text)

    def std(out=True):
        if out:
            if lines:
                return proc.stdout.decode("utf-8").splitlines()
            else:
                # return proc.stdout.rstrip('.\n')
                return proc.stdout
        else:
            if lines:
                return proc.stderr.decode("utf-8").splitlines()
            else:
                # return proc.stderr.decode("utf-8").rstrip('.\n')
                return proc.stderr

    rv = CompletedProcess(proc.args, proc.returncode, std(), std(False))
    if rv.returncode != 0 and exc:
        raise CmdError(rv)
    return rv


def cmdname(func, sep='_'): return func.__name__.split(**split_sep(sep))[0]


def current_task_name(): return current_task().get_name() if aioloop() else str()


@singledispatch
def delete(data: MutableMapping, key=('self', 'cls',)):
    """
    Deletes item in dict based on key.

    Args:
        data: MutableMapping.
        key: key.

    Returns:
        data: dict with key deleted or the same if key not found.
    """
    key = to_iter(key)
    for item in key:
        with suppress(KeyError):
            del data[item]
    return data


@delete.register
def delete_list(data: list, key=('self', 'cls',)):
    """
    Deletes value in list.

    Args:
        data: MutableMapping.
        key: key.

    Returns:
        data: list with value deleted or the same if key not found.
    """
    key = to_iter(key)
    for item in key:
        with suppress(ValueError):
            data.remove(item)
    return data


def dict_sort(data, ordered=False, reverse=False):
    """
    Order a dict based on keys.

    Args:
        data: dict to be ordered.
        ordered: OrderedDict.
        reverse: reverse.

    Returns:
        Union[dict, collections.OrderedDict]: Dict sorted
    """
    rv = {key: data[key] for key in sorted(data.keys(), reverse=reverse)}
    if ordered:
        return OrderedDict(rv)
    return rv.copy()


def effect(apply, data):
    """
    Perform function on iterable.

    Examples:
        >>> pretty_install()
        >>>
        >>> simple = Simple()
        >>> effect(lambda x: simple.__setattr__(x, dict()), 'a b')
        >>> simple.a, simple.b
        ({}, {})

    Args:
        apply: Function to apply.
        data: Iterable to perform function.

    Returns:
        No Return.
    """
    consume(side_effect(apply, to_iter(data)))


def enumvalue(data):
    """
    Returns Enum Value if Enum Instance or Data.

    Examples:
        >>> pretty_install()
        >>>
        >>> enumvalue(Private.ANNOTATIONS)
        '__annotations__'
        >>> enumvalue(None)

    Args:
        data: object.

    Returns:
        Enum Value or Data.
    """
    return data.value if Es(data).enum else data


def get(data, *args, default=None, one=True, recursive=False, with_keys=False):
    """
    Get value of name in Mutabble Mapping/GetType or object

    Examples:
        >>> get(dict(a=1), 'a')
        1
        >>> get(dict(a=1), 'b')
        >>> get(dict(a=1), 'b', default=2)
        2
        >>> get(dict, '__module__')
        'builtins'
        >>> get(dict, '__file__')

    Args:
        data: MutabbleMapping/GetType to get value.
        *args: keys (default: ('name')).
        default: default value (default: None).
        with_keys: return dict names and values or values (default: False).
        one: return [0] if len == 1 and one instead of list (default: True).
        recursive: recursivily for MutableMapping (default: False).

    Returns:
        Value for key.
    """
    def rv(items):
        if recursive and with_keys:
            items = {key: value[0] if len(value) == 1 and one else value for key, value in items}
        if with_keys:
            return items
        return list(r)[0] if len(r := items.values()) == 1 and one else list(r)

    args = args or ('name', )
    es = Es(data)
    if recursive and not es.mm:
        # TODO: to_vars() empty
        # data = to_vars()
        pass
    if es.mm and recursive:
        return rv(defaultdict(list, {k: v for arg in args for k, v in _nested_lookup(arg, data,
                                                                                     with_keys=with_keys)}))
    elif es.mm:
        return rv({arg: data.get(arg, default) for arg in args})

    return rv({attr: getattr(data, attr, default) for attr in args})


def getset(data, name, default=None, setvalue=True):
    """
    Sets attribute with default if it does not exists and returns value.

    Examples:
        >>> class Dict: pass
        >>> class Slots: __slots__ = ('a', )
        >>>
        >>> d = Dict()
        >>> s = Slots()
        >>> getset(d, 'a')
        >>> # noinspection PyUnresolvedReferences
        >>> d.a
        >>> getset(s, 'a')
        >>> s.a
        >>>
        >>> d = Dict()
        >>> s = Slots()
        >>> getset(d, 'a', 2)
        2
        >>> # noinspection PyUnresolvedReferences
        >>> d.a
        2
        >>> getset(s, 'a', 2)
        2
        >>> s.a
        2
        >>>
        >>> class Dict: a = 1
        >>> class Slots:
        ...     __slots__ = ('a', )
        ...     def __init__(self):
        ...         self.a = 1
        >>> d = Dict()
        >>> s = Slots()
        >>> getset(d, 'a')
        1
        >>> getset(s, 'a')
        1
        >>> getset(d, 'a', 2)
        1
        >>> getset(s, 'a', 2)
        1

    Args:
        data: object.
        name: attr name.
        default: default value (default: None)
        setvalue: setattr in object if AttributeError (default: True).

    Returns:
        Attribute value or sets default value and returns.
    """
    try:
        return object.__getattribute__(data, name)
    except AttributeError:
        if setvalue:
            object.__setattr__(data, name, default)
            return object.__getattribute__(data, name)
        return default


def iseven(number): return Es(number).even


def in_dict(data, items=None, **kwargs):
    """
    Is Item in Dict?.

    Examples:
        >>> in_dict(globals(), {'True': True, 'False': False})
        True
        >>> in_dict(globals()['__builtins__'], {'True': True, 'False': False}, __name__='builtins')
        True
        >>> in_dict(globals(), {'True': True, 'False': False}, __name__='builtins')
        True
        >>> Es(BUILTINS).builtin
        True
        >>> Es(dict(__name__='builtins')).builtin
        True

    Args:
        data: Dict
        items: Dict with key and values for not str keys (default: None)
        **kwargs: keys and values.

    Returns:
        True if items in Dict.
    """
    if Es(data).mm:
        for key, value in ((items if items else dict()) | kwargs).items():
            values = nested_lookup(key, data)
            if not values or value not in values:
                return False
        return True
    return False


def join_newline(data): return NEWLINE.join(data)


def map_reduce_even(iterable): return map_reduce(iterable, keyfunc=iseven)


def map_with_args(data, func, /, *args, pred=lambda x: True if x else False, split=' ', **kwargs):
    """
    Apply pred/filter to data and map with args and kwargs.

    Examples:
        >>> pretty_install()
        >>> # noinspection PyUnresolvedReferences
        >>> def f(i, *ar, **kw):
        ...     return f'{i}: {[a(i) for a in ar]}, {", ".join([f"{k}: {v(i)}" for k, v in kw.items()])}'
        >>> map_with_args('0.1.2', f, int, list, pred=lambda x: x != '0', split='.', int=int, str=str)
        ["1: [1, ['1']], int: 1, str: 1", "2: [2, ['2']], int: 2, str: 2"]

    Args:
        data: data.
        func: final function to map.
        *args: args to final map function.
        pred: pred to filter data before map.
        split: split for data str.
        **kwargs: kwargs to final map function.

    Returns:
        List with results.
    """
    return [func(item, *args, **kwargs) for item in yield_if(data, pred=pred, split=split)]


def newprop(name=None, default=None, pprop=False):
    """
    Get a new property with getter, setter and deleter.

    Examples:
        >>> class Test:
        ...     prop = newprop()
        ...     callable = newprop(default=str)
        >>>
        >>> test = Test()
        >>> '_prop' not in vars(test)
        True
        >>> test.prop
        >>> '_prop' in vars(test)
        True
        >>> test.prop
        >>> test.prop = 2
        >>> test.prop
        2
        >>> del test.prop
        >>> '_prop' in vars(test)
        False
        >>> test.prop
        >>> '_callable' not in vars(test)
        True
        >>> test.callable  # doctest: +ELLIPSIS
        '....Test object at 0x...>'
        >>> '_callable' in vars(test)
        True
        >>> test.callable  # doctest: +ELLIPSIS
        '....Test object at 0x...>'
        >>> test.callable = 2
        >>> test.callable
        2
        >>> del test.callable
        >>> '_callable' in vars(test)
        False
        >>> test.callable  # doctest: +ELLIPSIS
        '....Test object at 0x...>'

    Args:
        name: property name (attribute name: _name). :func:' varname`is used if no name (default: varname())
        default: default for getter if attribute is not defined.
            Could be a callable/partial that will be called with self (default: None)
        pprop: pproperty or property (default: False)

    Returns:
        Property.
    """
    func = pproperty if pprop else property
    name = f'_{name if name else varname()}'
    return func(
        lambda self:
        getset(self, name, default=default(self) if Es(default).instance(Callable, partial) else default),
        lambda self, value: self.__setattr__(name, value),
        lambda self: self.__delattr__(name)
    )


def noexception(func, *args, default_=None, exc_=Exception, **kwargs):
    """
    Execute function suppressing exceptions.

    Examples:
        >>> noexception(dict(a=1).pop, 'b', default_=2, exc_=KeyError)
        2

    Args:
        func: callable.
        *args: args.
        default_: default value if exception is raised.
        exc_: exception or exceptions.
        **kwargs: kwargs.

    Returns:
        Any: Function return.
    """
    with suppress(exc_):
        return func(*args, **kwargs)
    return default_


def prefixed(name: str) -> str:
    try:
        return f'{name.upper()}_'
    except AttributeError:
        pass


def repr_format(obj, attrs, clear=True, newline=False):
    cls = obj.__class__
    if clear:
        for item in dir(cls):
            if (attr := getattr(cls, item, None)) and (c := getattr(attr, 'cache_clear', None)):
                # noinspection PyUnboundLocalVariable
                c()
    new = NEWLINE if newline else str()
    msg = f',{new if newline else " "}'.join([f"{arg}: {repr(getattr(obj, arg))}" for arg in to_iter(attrs)])
    return f'{cls.__name__}({new}{msg}{new})'


@decorator
def runwarning(func, *args, **kwargs):
    with catch_warnings(record=False):
        filterwarnings('ignore', category=RuntimeWarning)
        warnings.showwarning = lambda *_args, **_kwargs: None
        rv = func(*args, **kwargs)
        return rv


def split_sep(sep='_'): return dict(sep=sep) if sep else dict()


def startswith(name: str, builtins=True): return name.startswith('__') if builtins else name.startswith('_')


def to_camel(text, replace=True):
    """
    Convert to Camel

    Examples:
        >>> to_camel(Private.IGNORE_ATTR.name)
        'IgnoreAttr'
        >>> to_camel(Private.IGNORE_ATTR.name, replace=False)
        'Ignore_Attr'
        >>> to_camel(Private.IGNORE_ATTR.value, replace=False)
        '__Ignore_Attr__'

    Args:
        text: text to convert.
        replace: remove '_'  (default: True)

    Returns:
        Camel text.
    """
    rv = ''.join(map(str.title, to_iter(text, '_')))
    return rv.replace('_', '') if replace else rv


def to_iter(data, always=False, split=' '):
    """
    To iter.

    Examples:
        >>> pretty_install()
        >>> to_iter('test1')
        ['test1']
        >>> to_iter('test1 test2')
        ['test1', 'test2']
        >>> to_iter(dict(a=1))
        {'a': 1}
        >>> to_iter(dict(a=1), always=True)
        [{'a': 1}]
        >>> to_iter('test1.test2')
        ['test1.test2']
        >>> to_iter('test1.test2', split='.')
        ['test1', 'test2']

    Args:
        data: data.
        always: return any iterable into a list.
        split: split for str.

    Returns:
        Iterable.
    """
    es = Es(data)
    if es.str:
        data = data.split(split)
    elif not es.iterable or always:
        data = [data]
    return data


def to_vars():
    """
    Object to dict with no copy or deepcopy.

    To be used for:
        - get recursivily
        - repr

    Returns:
        Dict.
    """
    pass


def token_open(file):
    """
    Read file with tokenize to use in nested classes ast node.

    Args:
        file: filename

    Returns:
        Source
    """
    with tokenize.open(str(file)) as f:
        return f.read()


def varname(index: int = 2, lower=True, sep: str = '_') -> Optional[str]:
    """
    Caller var name.

    Examples:

        .. code-block:: python

            class A:

                def __init__(self):

                    self.instance = varname()

            a = A()

            var = varname(1)

    Args:
        index: index.
        lower: lower.
        sep: split.

    Returns:
        Optional[str]: Var name.
    """
    with suppress(IndexError, KeyError):
        _stack = insstack()
        func = _stack[index - 1].function
        index = index + 1 if func == POST_INIT_NAME else index
        if line := textwrap.dedent(_stack[index].code_context[0]):
            if var := re.sub(f'(.| ){func}.*', str(), line.split(' = ')[0].replace('assert ', str()).split(' ')[0]):
                return (var.lower() if lower else var).split(**split_sep(sep))[0]


def yield_if(data, pred=lambda x: True if x else False, split=' ', apply=None):
    """
    Yield value if condition is met and apply function if predicate.

    Examples:
        >>> pretty_install()
        >>> list(yield_if([True, None]))
        [True]
        >>> list(yield_if('test1.test2', pred=lambda x: x.endswith('2'), split='.'))
        ['test2']
        >>> list(yield_if('test1.test2', pred=lambda x: x.endswith('2'), split='.', \
        apply=lambda x: x.removeprefix('test')))
        ['2']
        >>> list(yield_if('test1.test2', pred=lambda x: x.endswith('2'), split='.', \
        apply=(lambda x: x.removeprefix('test'), lambda x: int(x))))
        [2]

    Args:
        data: data
        pred: predicate (default: if value)
        split: split char for str.
        apply: functions to apply if predicate is met.

    Returns:
        Yield values if condition is met and apply functions if provided.
    """
    for item in to_iter(data, split=split):
        if pred(item):
            if apply:
                for func in to_iter(apply):
                    item = func(item)
            yield item


def yield_last(data, split=' '):
    """
    Yield value if condition is met and apply function if predicate.

    Examples:
        >>> pretty_install()
        >>> list(yield_last([True, None]))
        [(False, True, None), (True, None, None)]
        >>> list(yield_last('first last'))
        [(False, 'first', None), (True, 'last', None)]
        >>> list(yield_last('first.last', split='.'))
        [(False, 'first', None), (True, 'last', None)]
        >>> list(yield_last(dict(first=1, last=2)))
        [(False, 'first', 1), (True, 'last', 2)]

    Args:
        data: data.
        split: split char for str.

    Returns:
        Yield value and True when is the last item on iterable
    """
    data = to_iter(data, split=split)
    mm = Es(data).mm
    total = len(data)
    count = 0
    for i in data:
        count += 1
        yield count == total, *(i, data.get(i) if mm else None,)


# </editor-fold>
# <editor-fold desc="Es">
class Es:
    # noinspection PyUnresolvedReferences
    """
        Is Instance, Subclass, etc. Helper Class

        Examples:
            >>> pretty_install()
            >>>
            >>> es = Es(2)
            >>> es.int
            True
            >>> es.bool
            False
            >>> es.instance(dict, tuple)
            False
            >>> es(dict, tuple)
            False
            >>> def func(): pass
            >>> Es(func).coro
            False
            >>> async def async_func(): pass
            >>> es = Es(async_func)
            >>> es.coro, es.coroutinefunction, es.asyncgen, es.asyncgenfunction, es.awaitable, es.coroutine
            (True, True, False, False, False, False)
            >>> es = {i.name: Es(i.object) for i in classify_class_attrs(TestAsync)}
            >>> es['async_classmethod'].coro, es['async_classmethod'].coroutinefunction, \
            es['async_classmethod'].asyncgen, es['async_classmethod'].asyncgenfunction, \
            es['async_classmethod'].awaitable, es['async_classmethod'].coroutine
            (True, True, False, False, False, False)
            >>> es['async_method'].coro, es['async_method'].coroutinefunction, \
            es['async_method'].asyncgen, es['async_method'].asyncgenfunction, \
            es['async_method'].awaitable, es['async_method'].coroutine
            (True, True, False, False, False, False)
            >>> es['async_pprop'].coro, es['async_pprop'].coroutinefunction, \
            es['async_pprop'].asyncgen, es['async_pprop'].asyncgenfunction, \
            es['async_pprop'].awaitable, es['async_pprop'].coroutine
            (True, True, False, False, False, False)
            >>> es['async_prop'].coro, es['async_prop'].coroutinefunction, \
            es['async_prop'].asyncgen, es['async_prop'].asyncgenfunction, \
            es['async_prop'].awaitable, es['async_prop'].coroutine
            (True, True, False, False, False, False)
            >>> es['async_staticmethod'].coro, es['async_staticmethod'].coroutinefunction, \
            es['async_staticmethod'].asyncgen, es['async_staticmethod'].asyncgenfunction, \
            es['async_staticmethod'].awaitable, es['async_staticmethod'].coroutine
            (True, True, False, False, False, False)
            >>> assert es['classmethod'].coro == False
            >>> assert es['cprop'].coro == False
            >>> assert es['method'].coro == False
            >>> assert es['pprop'].coro == False
            >>> assert es['prop'].coro == False
            >>> assert es['staticmethod'].coro == False

        Attributes:
        -----------
        data: Any
            object to provide information (default: None)
        """
    __slots__ = ('data', )
    def __init__(self, data=None): self.data = data
    def __call__(self, *args): return isinstance(self.data, args)
    def __getstate__(self): return dict(data=self.data)
    def __hash__(self): return hash((type(self.data), self.__str__()))
    def __reduce__(self): return self.__class__, tuple(self.data)
    def __reduce_ex__(self, *args, **kwargs): return self.__class__, tuple(self.data)
    def __repr__(self): return f'{self.__class__.__name__}({self.data})'
    def __setstate__(self, state): self.data = state['data']
    def __str__(self): return str(self.data)

    # <editor-fold desc="Es - Protected">
    @property
    @functools.cache
    def _func(self): return self.data.fget if self.prop else self.data.__func__ \
        if self(classmethod, staticmethod) else self.data

    @property
    @functools.cache
    def _function(self): return insstack()[1].function
    # </editor-fold>

    # <editor-fold desc="Es - Bool">
    @property
    @functools.cache
    def annotation(self): return self(Annotation)

    @property
    @functools.cache
    def annotationstype(self): return self(AnnotationsType)

    @property
    @functools.cache
    def annotationstype_both(self): return self.annotationstype or self.es_cls.annotationstype_sub

    @property
    @functools.cache
    def annotationstype_sub(self): return self.subclass(AnnotationsType)

    @property
    @functools.cache
    def asdictmethod(self): return self(AsDictMethodType)

    @property
    @functools.cache
    def asdictmethod_sub(self): return self.subclass(AsDictMethodType)

    @property
    @functools.cache
    def asdictproperty(self): return self(AsDictPropertyType)

    @property
    @functools.cache
    def asdictproperty_sub(self): return self.subclass(AsDictPropertyType)

    @property
    @functools.cache
    def ast(self): return self(AST)

    @property
    @functools.cache
    def asyncfor(self): return isinstance(self._func, AsyncFor)

    @property
    @functools.cache
    def asyncfunctiondef(self): return isinstance(self._func, AsyncFunctionDef)

    @property
    @functools.cache
    def asyncgen(self): return isinstance(self._func, AsyncGeneratorType)

    @property
    @functools.cache
    def asyncgenfunction(self): return isasyncgenfunction(self._func)

    @property
    @functools.cache
    def asyncwith(self): return isinstance(self._func, AsyncWith)

    @property
    @functools.cache
    def attribute(self): return self(Attribute)

    @property
    @functools.cache
    def await_ast(self): return isinstance(self._func, Await)

    @property
    @functools.cache
    def awaitable(self): return isawaitable(self._func)

    @property
    @functools.cache
    def basestate(self): return self(BaseState)

    @property
    @functools.cache
    def bool(self): return self(int) and self(bool)

    @property
    @functools.cache
    def builtin(self): return any([in_dict(BUILTINS, self.data), self.builtinclass, self.builtinfunction])

    @property
    @functools.cache
    def builtinclass(self): return self.data in BUILTINS_CLASSES

    @property
    @functools.cache
    def builtinfunction(self): return self.data in BUILTINS_FUNCTIONS

    @property
    @functools.cache
    def builtinfunctiontype(self): return self(BuiltinFunctionType)

    @property
    @functools.cache
    def bytesio(self): return self(BytesIO)  # :class:`typing.BinaryIO`

    @property
    @functools.cache
    def cache_clear(self): return self.has(self._function) and self.modname == Module.functools.value

    @property
    @functools.cache
    def cached_property(self): return self(cached_property)

    @property
    @functools.cache
    def callable(self): return self(Callable)

    @property
    @functools.cache
    def chain(self): return self(Chain)

    @property
    @functools.cache
    def chainmap(self): return self(ChainMap)

    @property
    @functools.cache
    def classdef(self): return self(ClassDef)

    @property
    @functools.cache
    def classmethoddescriptortype(self): return self(ClassMethodDescriptorType)

    @property
    @functools.cache
    def classvar(self): return (self.datafield and get_origin(self.data.type) == ClassVar) or get_origin(
        self.data) == ClassVar

    @property
    @functools.cache
    def clsmethod(self): return self(classmethod)

    @property
    @functools.cache
    def codetype(self): return self(CodeType)

    @property
    @functools.cache
    def collections(self): return is_collections(self.data)

    @property
    @functools.cache
    def container(self): return self(Container)

    @property
    @functools.cache
    def coro(self): return any(
        [self.asyncfor, self.asyncfunctiondef, self.asyncwith, self.await_ast] if self.ast else
        [self.asyncgen, self.asyncgenfunction, self.awaitable, self.coroutine, self.coroutinefunction])

    @property
    @functools.cache
    def coroutine(self): return iscoroutine(self._func) or isinstance(self._func, CoroutineType)

    @property
    @functools.cache
    def coroutinefunction(self): return iscoroutinefunction(self._func)

    @property
    @functools.cache
    def default_factory(self): return self.datafield and Es(self.data.default).missing and self.has(self._function)

    @property
    @functools.cache
    def datafield(self): return self(DataField)

    @property
    @functools.cache
    def datatype(self): return self(DataType)

    @property
    @functools.cache
    def datatype_both(self): return self.datatype or self.es_cls.datatype_sub

    @property
    @functools.cache
    def datatype_sub(self): return self.subclass(DataType)

    @property
    @functools.cache
    def defaultdict(self): return self(defaultdict)

    @property
    @functools.cache
    def deleter(self): return self.property_any and self.data.fdel is not None

    @property
    @functools.cache
    def dict(self): return self(dict)

    @property
    @functools.cache
    def dicttype(self): return self(DictType)

    @property
    @functools.cache
    def dicttype_sub(self): return self.subclass(DictType)

    @property
    @functools.cache
    def dynamicclassattribute(self): return self(DynamicClassAttribute)

    @property
    @functools.cache
    def dlst(self): return self(dict, list, set, tuple)

    @property
    @functools.cache
    def enum(self): return self(Enum)

    @property
    @functools.cache
    def enum_sub(self): return self.subclass(Enum)

    @property
    @functools.cache
    def enumbase(self): return self(EnumBase)

    @property
    @functools.cache
    def enumbase_sub(self): return self.subclass(EnumBase)

    @property
    @functools.cache
    def even(self): return not self.data % 2

    @property
    @functools.cache
    def fileio(self): return self(FileIO)

    @property
    @functools.cache
    def float(self): return self(float)

    @property
    @functools.cache
    def frameinfo(self): return self(FrameInfo)

    @property
    @functools.cache
    def frametype(self): return self(FrameType)

    @property
    @functools.cache
    def functiondef(self): return self(FunctionDef)

    @property
    @functools.cache
    def functiontype(self): return self(FunctionType)

    @property
    @functools.cache
    def generator(self): return self(Generator)

    @property
    @functools.cache
    def generatortype(self): return self(GeneratorType)

    @property
    @functools.cache
    def genericalias(self): return self(types.GenericAlias)

    @property
    @functools.cache
    def getattrnobuiltintype(self): return self(GetAttrNoBuiltinType)

    @property
    @functools.cache
    def getattrnobuiltintype_sub(self): return self.subclass(GetAttrNoBuiltinType)

    @property
    @functools.cache
    def getattrtype(self): return self(GetAttrType)

    @property
    @functools.cache
    def getattrtype_sub(self): return self.subclass(GetAttrType)

    def getsetdescriptor(self, n=None): return isgetsetdescriptor(self.es_cls.get(n) if n else self.data)

    @property
    @functools.cache
    def getsetdescriptortype(self): return self(GetSetDescriptorType)

    @property
    @functools.cache
    def gettype(self): return self(GetType)

    @property
    @functools.cache
    def gettype_sub(self): return self.subclass(GetType)

    @functools.cache
    def has(self, name):
        """
        Checks if Object has attr.

        Examples:
            >>> from rc import Es, Private, pretty_install
            >>> pretty_install()
            >>>
            >>> class Test:
            ...     __repr_newline__ = True
            >>>
            >>> Es(Test()).has(Private.REPR_NEWLINE)
            True
            >>> Es(Test()).has(Private.REPR_EXCLUDE)
            False

        Args:
            name: attribute name.
        Returns:
            True if object has attribute.
        """
        return hasattr(self.data, enumvalue(name))

    @property
    @functools.cache
    def hashable(self): return bool(noexception(TypeError, hash, self.data))

    @property
    @functools.cache
    def import_ast(self): return self(Import)

    @property
    @functools.cache
    def importfrom(self): return self(ImportFrom)

    @property
    @functools.cache
    def initvar(self): return (self.datafield and isinstance(self.data.type, InitVar)) or self(InitVar)

    @property
    @functools.cache
    def installed(self): return is_installed(self.data)

    @functools.cache
    def instance(self, *args): return isinstance(self.data, args)

    @property
    @functools.cache
    def int(self): return self(int)

    @property
    @functools.cache
    def io(self): return self.bytesio and self.stringio  # :class:`typing.IO`

    @property
    @functools.cache
    def iterable(self): return self(Iterable)

    @property
    @functools.cache
    def iterator(self): return self(Iterator)

    @property
    @functools.cache
    def lambdatype(self): return self(LambdaType)

    @property
    @functools.cache
    def list(self): return self(list)

    @property
    @functools.cache
    def lst(self): return self.list or self.set or self.tuple

    @property
    @functools.cache
    def mappingproxytype(self): return self(MappingProxyType)

    @property
    @functools.cache
    def mappingproxytype_sub(self): return self.subclass(MappingProxyType)

    @property
    @functools.cache
    def memberdescriptor(self): return ismemberdescriptor(self.data)

    @property
    @functools.cache
    def memberdescriptortype(self): return self(MemberDescriptorType)

    @property
    @functools.cache
    def meta(self): return  # TODO: meta

    @property
    @functools.cache
    def meta_sub(self): return  # TODO: meta_sub

    @property
    @functools.cache
    def metatype(self): return  # TODO: metatype

    @property
    @functools.cache
    def metatype_sub(self): return  # TODO: metatype_sub

    @property
    @functools.cache
    def method(self): return self.methodtype and not self(classmethod, property, staticmethod)

    @property
    @functools.cache
    def methoddescriptor(self): return ismethoddescriptor(self.data)

    @property
    @functools.cache
    def methoddescriptortype(self): return self(types.MethodDescriptorType)

    @property
    @functools.cache
    def methodtype(self): return self(MethodType)  # True if it is an instance method!.

    @property
    @functools.cache
    def methodwrappertype(self): return self(MethodWrapperType)

    @property
    @functools.cache
    def methodwrappertype_sub(self): return self.subclass(MethodWrapperType)

    @property
    @functools.cache
    def missing(self): return self(MISSING_TYPE)

    @property
    @functools.cache
    def mlst(self): return self.mm or self.list or self.set or self.tuple

    @property
    @functools.cache
    def mm(self): return self(MutableMapping)

    @property
    @functools.cache
    def moduletype(self): return self(ModuleType)

    @property
    @functools.cache
    def module_function(self): return is_module_function(self.data)

    @property
    @functools.cache
    def noncomplex(self): return is_noncomplex(self.data)

    @property
    @functools.cache
    def namedtype(self): return self(NamedType)

    @property
    @functools.cache
    def namedtype_sub(self): return self.subclass(NamedType)

    @property
    @functools.cache
    def named_annotationstype(self): return self(NamedAnnotationsType)

    @property
    @functools.cache
    def named_annotationstype_sub(self): return self.subclass(NamedAnnotationsType)

    @property
    @functools.cache
    def none(self): return self(type(None))

    @property
    @functools.cache
    def object(self): return is_object(self.data)

    @property
    @functools.cache
    def pathlib(self): return self(PathLib)

    @property
    @functools.cache
    def picklable(self): return True if noexception(pickle_dumps, self.data) else False

    @property
    @functools.cache
    def primitive(self): return is_primitive(self.data)

    @property
    @functools.cache
    def pproperty(self): return self(pproperty)

    @property
    @functools.cache
    def prop(self): return self(property)

    @property
    @functools.cache
    def property_any(self): return self.prop or self.cached_property

    @functools.cache
    def readonly(self, name='__readonly__'):
        """
        Is readonly object?

        Examples:
            >>> from rc import Es, pretty_install
            >>> pretty_install()
            >>>
            >>> class First:
            ...     __slots__ = ('_data', )
            >>>
            >>> class Test(First):
            ...     __slots__ = ('_id', )
            >>>
            >>> Es(Test()).readonly()
            AttributeError("'Test' object has no attribute '__readonly__'")

        Returns:
            True if readonly.
        """
        name = enumvalue(name)
        value = None
        try:
            if self.has(name):
                value = object.__getattribute__(self.data, name)
            object.__setattr__(self.data, name, value)
        except Exception as exception:
            return exception
        if value is not None:
            object.__delattr__(self.data, name)
        return False

    @property
    @functools.cache
    def reducible(self): return is_reducible(self.data)

    @property
    @functools.cache
    def reducible_sequence_subclass(self): return is_reducible_sequence_subclass(self.data)

    @property
    @functools.cache
    def routine(self): return isroutine(self.data)

    @property
    @functools.cache
    def sequence(self): return self(Sequence)

    @property
    @functools.cache
    def sequence_sub(self): return self.subclass(Sequence)

    @property
    @functools.cache
    def set(self): return self(set)

    @property
    @functools.cache
    def setter(self): return self.prop and self.data.fset is not None

    @property
    @functools.cache
    def simple(self): return self(Simple)

    @property
    @functools.cache
    def sized(self): return self(Sized)

    @property
    @functools.cache
    def slist(self): return  # TODO: slist

    @functools.cache
    def slot(self, name):
        """
        Is attribute in slots?

        Examples:
            >>> pretty_install()
            >>>
            >>> class First:
            ...     __slots__ = ('_data', )
            >>>
            >>> class Test(First):
            ...     __slots__ = ('_id', )
            >>>
            >>> Es(Test()).slot(Protected.DATA)
            True
            >>> Es(Test()).slot(Protected.ID)
            True
            >>> Es(Test()).slot(Protected.IP)
            False

        Returns:
            True if attribute in slots
        """
        name = enumvalue(name)
        return name in self.slots

    @property
    @functools.cache
    def slotstype(self): return self(SlotsType)

    @property
    @functools.cache
    def slotstype_sub(self): return self.subclass(SlotsType)

    @property
    @functools.cache
    def static(self): return self(staticmethod)

    @property
    @functools.cache
    def str(self): return self(str)

    @property
    @functools.cache
    def stuple(self): return  # TODO: stuple

    @functools.cache
    def subclass(self, *args):
        return self.type and issubclass(self.data, args)

    @property
    @functools.cache
    def stringio(self): return self(StringIO)  # :class:`typing.TextIO`

    @property
    @functools.cache
    def tracebacktype(self): return self(TracebackType)

    @property
    @functools.cache
    def tuple(self): return self(tuple)

    @property
    @functools.cache
    def type(self): return self(type)

    @property
    @functools.cache
    def unicode(self): return is_unicode(self.data)

    @property
    @functools.cache
    def wrapperdescriptortype(self): return self(WrapperDescriptorType)

    @functools.cache
    def writeable(self, name):
        # noinspection PyUnresolvedReferences
        """
        Checks if an attr is writeable in object.

        Examples:
            >>> from rc import Es, pretty_install
            >>> pretty_install()
            >>>
            >>> class First:
            ...     __slots__ = ('_data', )
            >>>
            >>> class Test(First):
            ...     __slots__ = ('_id', )
            >>>
            >>> test = Test()
            >>> es = Es(test)
            >>> es.writeable('_id')
            True
            >>> es.writeable('test')
            False
            >>> Es(test.__class__).writeable('test')
            True
            >>> test.__class__.test = 2
            >>> assert test.test == 2
            >>> Es(test.__class__).writeable('cls')
            True
            >>> object.__setattr__(test.__class__, 'cls', 2) # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            TypeError: can't apply this __setattr__ to type object

        Args:
            name: attribute name.

        Returns:
            True if can be written.
        """
        return self.dicttype or self.slotstype and self.slot(name) or not self.readonly(name)
    # </editor-fold>

    # <editor-fold desc="Es - Inspect">
    @functools.cache
    def annotations(self, stack=2): return annotations(self.data, stack=stack) if self.annotationstype_sub else dict()

    @functools.cache
    def attributes(self, stack=2):
        # TODO: Examples and classify attrs props etc. defaults, backup/infocls1.py
        """
        Attribute Information for Object Class or Class.

        Examples:
            >>> pretty_install()
            >>>
            >>> test = Es(TestDataDictSlotMix)
            >>> attr = test.attributes()['_TestData__dataclass_default_factory']
            >>> attr.default, attr.defining, attr.field.default_factory, attr.object, \
            attr.field.data.type == attr.annotation.hint, attr.object == attr.annotation.default  # doctest: +ELLIPSIS
            (NotImplemented, <class '....TestData'>, True, {}, True, True)
            >>> attr.object, attr.annotation.default
            ({}, {})

        Args:
            stack: stack index to extract globals and locals (default: 1) or frame.

        Returns:
            Dict Attribute Information for Object Class or Class.
        """
        fields = self.fields.copy()
        annotation = annotations(self.data, stack=stack) if self.annotationstype_both else dict()
        attribute = dict()
        for item in classify_class_attrs(self.cls):
            e = type(self)(item.object)
            attribute.update({item.name: Attribute(
                    annotation=annotation.get(item.name),
                    default=item.object if item.name not in fields or fields[item.name].init else NotImplemented,
                    defining=item.defining_class, es=e, field=type(self)(fields.pop(item.name, None)),
                    kind=Kind[item.kind.split(' ')[0].upper()], name=item.name,
                    object=item.object, qual=type(self)(e._func).get(Private.QUALNAME, default=item.name))})
        for k, value in fields.items():
            defining_cls = self.cls
            for C in self.mro:
                c = type(self)(C)
                if not c.datatype_sub or (c.datatype_sub and k not in c.fields):
                    break
                defining_cls = C
            f = type(self)(value)
            obj = value.default_factory() if f.default_factory else type(self)(defining_cls).get(k)
            attribute.update({k: Attribute(annotation=annotation.get(k), default=obj if value.init else NotImplemented,
                                           defining=defining_cls, es=type(self)(obj), field=f, kind=Kind.DATA, name=k,
                                           object=obj, qual=k)})
        return attribute

    @property
    @functools.cache
    def cls(self): return self.data if self.type else self.data.__class__

    @property
    @functools.cache
    def clsname(self): return self.cls.__name__

    @property
    @functools.cache
    def clsqual(self): return self.cls.__qualname__

    @property
    @functools.cache
    def es_cls(self): return type(self)(self.cls)

    @property
    @functools.cache
    def fields(self): return self.data.__dataclass_fields__ if self.datatype_both else {}

    @property
    @functools.cache
    def first_builtin(self): return anyin(self.mro, BUILTINS_CLASSES)

    @functools.cache
    def get(self, item, default=None):
        # TODO: get - annotations and Examples.
        if self.mm and self.container and item in self.data:
            return self.data.get(item, default)
        elif type(self)(name := enumvalue(item)).str and self.has(name):
            try:
                return object.__getattribute__(self.data, name)
            except AttributeError:
                pass
        return default

    @property
    @functools.cache
    def importable_name_cls(self): return noexception(importable_name, self.cls)

    @property
    @functools.cache
    def importable_name_data(self): return noexception(importable_name, self.data)

    @property
    @functools.cache
    def modname(self):
        return self.__name__ if self.moduletype else self.__module__ if self.has(Private.MODULE) else None

    @property
    @functools.cache
    def mro(self): return self.cls.__mro__

    @property
    @functools.cache
    def mro_and_data(self):
        """
        Tuple with Class MRO and instance (self.data).

        Examples:
            >>> from rc import Es, pretty_install
            >>> pretty_install()
            >>>
            >>> Es(dict(a=1)).mro_and_data
            ({'a': 1}, <class 'dict'>, <class 'object'>)

        Returns:
            Tuple with Class MRO and instance (self.data).
        """
        return (() if self.type else (self.data, )) + self.mro

    def mro_first_data(self, name):
        """
        First value of attr found in mro and instance if obj is instance.

        Examples:
            >>> from rc import Es, Private, pretty_install
            >>> pretty_install()
            >>>
            >>> class Test:
            ...     __repr_newline__ = True
            >>>
            >>> test = Test()
            >>> class Test2(Test):
            ...     def __init__(self):
            ...         self.__repr_newline__ = False
            >>>
            >>> Es(Test()).mro_first_data(Private.REPR_NEWLINE)
            True
            >>> Es(Test2()).mro_first_data(Private.REPR_NEWLINE)
            False
            >>> Es(int()).mro_first_data(Private.REPR_NEWLINE)
            >>> Es(Test()).mro_first_data(Private.REPR_PPROPERTY)

        Returns:
            First value of attr found in mro and instance if obj is instance.
        """
        name = enumvalue(name)
        for item in self.mro_and_data:
            if type(self)(item).has(name):
                return object.__getattribute__(item, name)

    @functools.cache
    def mro_first_dict(self, name, mro=None):
        """
        First value of attr in obj.__class__.__dict__ found in mro.

        Examples:
            >>> from rc import Es, Private, pretty_install
            >>> pretty_install()
            >>>
            >>> class Test:
            ...     __repr_newline__ = False
            >>>
            >>> test = Test()
            >>> class Test2(Test):
            ...     def __init__(self):
            ...         self.__repr_newline__ = False
            >>>
            >>> Es(Test()).mro_first_dict(Private.REPR_NEWLINE)
            False
            >>> Es(Test2()).mro_first_dict(Private.REPR_NEWLINE)
            False
            >>> Es(int()).mro_first_dict(Private.REPR_NEWLINE)
            NotImplemented
            >>> Es(Test()).mro_first_dict(Private.REPR_PPROPERTY)
            NotImplemented
            >>> A = namedtuple('A', 'a')
            >>> Es(A).mro_first_dict(Private.SLOTS)
            ()

        Args:
            name: attribute name.
            mro: mro o search in dict (default: self.mro)
        Returns:
            First value of attr in obj.__class__.__dict__ found in mro.
        """
        name = enumvalue(name)
        for C in mro or self.mro:
            if name in C.__dict__:
                return C.__dict__[name]
        return NotImplemented

    @functools.cache
    def mro_first_dict_no_object(self, name):
        """
        First value of attr in obj.__class__.__dict__ found in mro excluding object.

        Examples:
            >>> from rc import Es, Private, pretty_install
            >>> pretty_install()
            >>>
            >>> class Test:
            ...     __repr_newline__ = False
            >>>
            >>> test = Test()
            >>> class Test2(Test):
            ...     def __init__(self):
            ...         self.__repr_newline__ = False
            >>>
            >>> Es(Test()).mro_first_dict_no_object(Private.REPR_NEWLINE)
            False
            >>> Es(Test2()).mro_first_dict_no_object(Private.REPR_NEWLINE)
            False
            >>> Es(int()).mro_first_dict_no_object(Private.REPR_NEWLINE)
            NotImplemented
            >>> Es(Test()).mro_first_dict_no_object(Private.REPR_PPROPERTY)
            NotImplemented
            >>> A = namedtuple('A', 'a')
            >>> Es(A).mro_first_dict_no_object(Private.SLOTS)
            ()
            >>> Es(dict).mro_first_dict_no_object(Private.SLOTS)
            NotImplemented
            >>> Es(dict()).mro_first_dict_no_object(Private.SLOTS)
            NotImplemented

        Returns:
            First value of attr in obj.__class__.__dict__ found in mro excluding object.
        """
        mro = list(self.mro)
        mro.remove(object)
        return self.mro_first_dict(enumvalue(name), tuple(mro))

    @functools.cache
    def mro_values(self, name):
        """
        All/accumulated values of attr in mro and obj if instance.

        Examples:
            >>> from rc import Es, pretty_install
            >>> pretty_install()
            >>>
            >>> class First:
            ...     __slots__ = ('_hash', '_repr')
            ...     __ignore_copy__ = (tuple, )
            ...     __repr_exclude__ = ('_repr', )
            >>>
            >>> class Test(First):
            ...     __slots__ = ('_prop', '_slot', )
            ...     __hash_exclude__ = ('_slot', )
            ...     __ignore_attr__ = ('attr', )
            ...     __ignore_kwarg__ = ('kwarg', )
            ...     __ignore_str__ = (tuple, )
            >>>
            >>> test = Test()
            >>> Es(test).mro_values(Private.HASH_EXCLUDE)
            ('_slot',)
            >>> Es(test).mro_values(Private.IGNORE_ATTR)  # doctest: +ELLIPSIS
            (
                'asdict',
                'attr',
                ...
            )
            >>> set(Es(test).mro_values(Private.IGNORE_COPY)).difference(Es().mro_values_default(\
Private.IGNORE_COPY))
            {<class 'tuple'>}
            >>> Es(test).mro_values(Private.IGNORE_KWARG)
            ('kwarg',)
            >>> set(Es(test).mro_values(Private.IGNORE_STR)).difference(Es().mro_values_default(\
Private.IGNORE_STR))
            {<class 'tuple'>}
            >>> Es(test).mro_values(Private.REPR_EXCLUDE)
            ('_repr',)
            >>> Es(test).mro_values(Private.SLOTS)
            ('_hash', '_prop', '_repr', '_slot')
            >>> assert sorted(Es(Environs()).mro_values(Private.PICKLE)) == sorted(PICKLE_ATTRS[Environs])

        Returns:
            All/accumulated values of attr in mro and obj if instance.
        """
        name = enumvalue(name)
        values = tuple({*(value for item in self.mro_and_data
                          for value in type(self)(item).get(name, default=tuple())), *self.mro_values_default(name)})
        return tuple(sorted(values)) if values and not type(self)(tuple(values)[0]).type else values

    @functools.cache
    def mro_values_default(self, name):
        """
        Default values for attr in mro and instance.

        Examples:
            >>> from rc import Es, pretty_install
            >>> pretty_install()
            >>>
            >>> class First:
            ...     __slots__ = ('_hash', '_repr')
            ...     __ignore_copy__ = (tuple, )
            ...     __repr_exclude__ = ('_repr', )
            >>>
            >>> class Test(First):
            ...     __slots__ = ('_prop', '_slot', )
            ...     __hash_exclude__ = ('_slot', )
            ...     __ignore_attr__ = ('attr', )
            ...     __ignore_kwarg__ = ('kwarg', )
            ...     __ignore_str__ = (tuple, )
            >>>
            >>> test = Test()
            >>> assert Es(test).mro_values_default(Private.HASH_EXCLUDE) == tuple()
            >>> assert Es(test).mro_values_default(Private.IGNORE_ATTR) == IgnoreAttr.__args__
            >>> assert Es(test).mro_values_default(Private.IGNORE_COPY) == IgnoreCopy.__args__
            >>> assert Es(test).mro_values_default(Private.IGNORE_KWARG) == tuple()
            >>> assert Es(test).mro_values_default(Private.IGNORE_STR) == IgnoreStr.__args__
            >>> assert Es(test).mro_values_default(Private.REPR_EXCLUDE) == tuple()
            >>> assert Es(test).mro_values_default(Private.SLOTS) == tuple()
            >>> assert sorted(Es(Environs()).mro_values_default(Private.PICKLE)) == sorted(PICKLE_ATTRS[Environs])

        Returns:
           Default values for attr in mro and instance.
        """
        if enumvalue(name) == Private.PICKLE.value:
            default = set()
            for C in self.mro:
                if C in PICKLE_ATTRS:
                    default.update(PICKLE_ATTRS[C])
        else:
            es = Es(name)
            default = rv.__args__ if (rv := globals().get(to_camel(name.name if es.enum else name))) else tuple()
        return tuple(sorted(default)) if default and not type(self)(tuple(default)[0]).type else tuple(default)

    @property
    @functools.cache
    def name(self): return self.data.__name__ if self.has(Private.NAME) else None

    @classmethod
    @functools.cache
    def prop_getter(cls, prop):
        es = cls(prop)
        if all([es.property_any, (func := es._func), (name := cls(func).name), name in es.cls.__dict__]):
            return attrgetter(name)
        return NotImplemented

    @property
    @functools.cache
    def slots(self):
        """
        Slots values in mro.

        Examples:
            >>> from rc import Es, pretty_install
            >>> pretty_install()
            >>>
            >>> class First:
            ...     __slots__ = ('_data', )
            >>>
            >>> class Test(First):
            ...     __slots__ = ('_id', )
            >>>
            >>> assert Es(Test()).slots == First.__slots__ + Test.__slots__

        Returns:
            Slots values in mro Tuple.
        """
        return self.mro_values(Private.SLOTS)

    @functools.cache
    def slots_include(self, name):
        """
        Accumulated values from slots - Accumulated values from mro attr name.

        Examples:
            >>> pretty_install()
            >>>
            >>> class First:
            ...     __slots__ = ('_hash', )
            >>>
            >>> class Test(First):
            ...     __slots__ = ('_prop', '_repr', '_slot', )
            ...     __hash_exclude__ = ('_slot', )
            ...     __repr_exclude__ = ('_repr', )
            >>>
            >>> es = Es(Test())
            >>> es.slots
            ('_hash', '_prop', '_repr', '_slot')
            >>> hash_attrs = es.slots_include(Private.HASH_EXCLUDE)
            >>> hash_attrs
            ('_hash', '_prop', '_repr')
            >>> sorted(hash_attrs + es.mro_values(Private.HASH_EXCLUDE)) == sorted(es.slots)
            True
            >>> repr_attrs = es.slots_include(Private.REPR_EXCLUDE)
            >>> repr_attrs
            ('_hash', '_prop', '_slot')
            >>> sorted(repr_attrs + es.mro_values(Private.REPR_EXCLUDE)) == sorted(es.slots)
            True

        Returns:
            Accumulated values from slots - Accumulated values from mro attr name.
        """
        return tuple(sorted(set(self.slots).difference(self.mro_values(name))))

    @property
    @functools.cache
    def super(self): return self.mro[1]
    # </editor-fold>

    # <editor-fold desc="Es - Utils">
    @property
    @functools.cache
    def deepcopy(self):
        """
        Deep copy object

        Tries again after calling :class:`rc.Es.state_methods` in case of PicklingError RecursionError.

        Examples:
            >>> from copy import deepcopy
            >>> from rc import Environs, Es
            >>>
            >>> deepcopy(Environs()) # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            RecursionError: maximum recursion depth exceeded
            >>> env = Environs()
            >>> term = env('TERM')
            >>> env
            <Env {'TERM': 'xterm-256color'}>
            >>> env_copy = env
            >>> assert id(env_copy) == id(env)
            >>> env_deepcopy = Es(env).deepcopy
            >>> env_deepcopy
            <Env {'TERM': 'xterm-256color'}>
            >>> assert id(env_deepcopy) != id(env)
            >>> assert id(env_deepcopy._values) != id(env._values)

        Returns:
            Deep copied object.
        """
        try:
            return copy.deepcopy(self.data)
        except (PicklingError, RecursionError):
            return copy.deepcopy(self.state_methods)

    @property
    @functools.cache
    def pickles(self):
        """
        Pickles object (dumps).

        Tries again after calling :class:`rc.Es.state_methods` in case of PicklingError RecursionError.

        Returns:
            Pickle object (bytes) or None if methods added to self.data so it can be called again.
        """
        try:
            return pickle_dumps(self.data)
        except (PicklingError, RecursionError):
            return pickle_dumps(self.state_methods)

    def state(self, data=None):
        """
        Values for :class:`rc.BaseState` methods:
            - :meth:`rc.BaseState.__getstate__`: (pickle) when state=None.
            - :meth:`rc.BaseState.__setstate__`: (unpickle) when state.

        Examples:
            >>> class Test:
            ...     __pickle__ = ('attribute', )
            ...     __slots__ = ('attribute', )
            >>>
            >>> test = Test()
            >>> e = Es(test)
            >>> e.slots + e.mro_values(Private.PICKLE)
            ('attribute', 'attribute')
            >>> status = e.state()
            >>> status
            {}
            >>> reconstruct = e.state(status)
            >>> reconstruct  # doctest: +ELLIPSIS
            <utils.Test object at 0x...>
            >>> reconstruct == e.state(status)
            True
            >>>
            >>> test.attribute = 1
            >>> new = Es(test)
            >>> status = new.state()
            >>> status
            {'attribute': 1}
            >>> reconstruct == new.state(status)
            True
            >>> reconstruct.attribute
            1

        Args:
            data: dict to restore object.

        Returns:
            State dict (pickle) or restored object from state dict (unpickle).
        """
        if data is None:
            return {attr: object.__getattribute__(self.data, attr) for attr in self.mro_values(Private.PICKLE.value)
                    if self.has(attr)}
        for key, value in data.items():
            object.__setattr__(self.data, key, value)
        return self.data

    @property
    @functools.cache
    def state_methods(self):
        """
        Add :class:`rc.BaseState` methods to object if PicklingError or RecursionError if class in mro is
        in :data `rc.PICKLE_ATTRS`:
            - :meth:`rc.BaseState.__getstate__`: (pickle) when state=None.
            - :meth:`rc.BaseState.__setstate__`: (unpickle) when state.

        Raises:
            PicklingError: Object has one or both state methods.
            AttributeError: Read-only.
            NotImplementedError: No mro items in PICKLE_ATTRS.

        Returns:
            Object with __getstate__ and __setstate__ methods added.
        """

        def _state(*args):
            if args and len(args) == 1:
                return type(self)(args[0]).state()
            elif args and len(args) == 2:
                type(self)(args[0]).state(args[1])

        setstate = None
        if (getstate := self.has(Private.GETSTATE)) or (setstate := self.has(Private.SETSTATE)):
            raise PicklingError(f'Object {self.data}, has one or both state methods: {getstate=}, {setstate=}')
        found = False
        for C in self.mro:
            if C in PICKLE_ATTRS:
                for attr in (Private.GETSTATE.value, Private.SETSTATE.value, ):
                    es = type(self)(self.__class__)
                    if not es.writeable(attr):
                        exc = es.readonly(attr)
                        raise AttributeError(f'Read-only: {self.data=}') from exc
                self.data.__class__.__getstate__ = _state
                self.data.__class__.__setstate__ = _state
                found = True
        if found:
            ic(self.data.__getstate__)
            return self.data
        else:
            raise NotImplementedError(f'No mro: {self.mro} items in {PICKLE_ATTRS.keys()=} for {self.data=}')

    @property
    @functools.cache
    def unpickles(self):
        """Unpickles object (loads)."""
        return pickle_loads(self.data)

    # </editor-fold>

    # TODO: asdict_props
    # asdict = property(lambda self: dict(data=self.data) | asdict_props(self))

    __class_getitem__ = classmethod(GenericAlias)


# </editor-fold>
# <editor-fold desc="Exceptions">
class CmdError(Exception):
    """Thrown if execution of cmd command fails with non-zero status code."""

    def __init__(self, rv):
        command = rv.args
        rc = rv.returncode
        stderr = rv.stderr
        stdout = rv.stdout
        super().__init__(f'{command=}', f'{rc=}', f'{stderr=}', f'{stdout=}')


class CmdAioError(CmdError):
    """Thrown if execution of aiocmd command fails with non-zero status code."""

    def __init__(self, rv):
        super().__init__(rv)


# </editor-fold>
# <editor-fold desc="Types">
class AnnotationsType(metaclass=ABCMeta):
    """
    Annotations Type.

    Examples:
        >>> named = namedtuple('named', 'a', defaults=('a', ))
        >>> Named = NamedTuple('Named', a=str)
        >>>
        >>> Es(named).annotationstype_sub
        False
        >>> Es(named()).annotationstype
        False
        >>>
        >>> Es(Named).annotationstype_sub
        True
        >>> Es(Named(a='a')).annotationstype
        True
    """

    @classmethod
    def __subclasshook__(cls, C):
        if cls is AnnotationsType:
            return Private.ANNOTATIONS.mro_first_dict(C) is not NotImplemented
        return NotImplemented


class AsDictMethodType(metaclass=ABCMeta):
    """
    AsDict Method Support (Class, Static and Method).

    Examples:
        >>> class AsDictClass: asdict = classmethod(lambda cls, *args, **kwargs: dict())
        >>> class AsDictM: asdict = lambda self, *args, **kwargs: dict()
        >>> class AsDictP: asdict = property(lambda self: dict())
        >>> class AsDictStatic: asdict = staticmethod(lambda cls, *args, **kwargs: dict())
        >>>
        >>> c = AsDictClass()
        >>> m = AsDictM()
        >>> p = AsDictP()
        >>> s = AsDictStatic()
        >>>
        >>> Es(AsDictClass).asdictmethod_sub
        True
        >>> Es(c).asdictmethod
        True
        >>>
        >>> Es(AsDictM).asdictmethod_sub
        True
        >>> Es(m).asdictmethod
        True
        >>>
        >>> Es(AsDictP).asdictmethod_sub
        False
        >>> Es(p).asdictmethod
        False
        >>>
        >>> Es(AsDictStatic).asdictmethod_sub
        True
        >>> Es(s).asdictmethod
        True
    """

    # noinspection PyUnusedLocal
    @abstractmethod
    def asdict(self, *args, **kwargs):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is AsDictMethodType:
            value = Public.ASDICT.mro_first_dict(C)
            es = Es(value)
            return value is not NotImplemented and any(
                [es.clsmethod, es.lambdatype, es.method, es.static]) and not es.prop
        return NotImplemented


class AsDictPropertyType(metaclass=ABCMeta):
    """
    AsDict Property Type.

    Examples:
        >>> class AsDictClass: asdict = classmethod(lambda cls, *args, **kwargs: dict())
        >>> class AsDictM: asdict = lambda self, *args, **kwargs: dict()
        >>> class AsDictP: asdict = property(lambda self: dict())
        >>> class AsDictStatic: asdict = staticmethod(lambda cls, *args, **kwargs: dict())
        >>>
        >>> c = AsDictClass()
        >>> m = AsDictM()
        >>> p = AsDictP()
        >>> s = AsDictStatic()
        >>>
        >>> Es(AsDictClass).asdictproperty_sub
        False
        >>> Es(c).asdictproperty
        False
        >>>
        >>> Es(AsDictM).asdictproperty_sub
        False
        >>> Es(m).asdictproperty
        False
        >>>
        >>> Es(AsDictP).asdictproperty_sub
        True
        >>> Es(p).asdictproperty
        True
        >>>
        >>> Es(AsDictStatic).asdictproperty_sub
        False
        >>> Es(s).asdictproperty
        False
    """

    @property
    @abstractmethod
    def asdict(self):
        return dict()

    @classmethod
    def __subclasshook__(cls, C):
        if cls is AsDictPropertyType:
            return (value := Public.ASDICT.mro_first_dict(C)) is not NotImplemented \
                   and Es(value).prop
        return NotImplemented


class DataType(metaclass=ABCMeta):
    """
    Data Type.

    Examples:
        >>> from dataclasses import make_dataclass
        >>>
        >>> Data = make_dataclass('C', [('a', int, datafield(default=1))])
        >>> class Dict: a = 1
        >>>
        >>> data = Data()
        >>> d = Dict()
        >>>
        >>> Es(Data).datatype_sub
        True
        >>> Es(data).datatype
        True
        >>> Es(Data).datatype
        False
        >>>
        >>> Es(Dict).datatype_sub
        False
        >>> Es(d).datatype
        False
    """
    __annotations__ = dict()
    __dataclass_fields__ = dict()

    @abstractmethod
    def __repr__(self) -> str:
        return str(self)

    @classmethod
    def __subclasshook__(cls, C):
        if cls is DataType:
            return Private.ANNOTATIONS.mro_first_dict(C) is not NotImplemented \
                   and Private.DATACLASS_FIELDS.mro_first_dict(C) is not NotImplemented \
                   and Private.REPR.mro_first_dict(C) is not NotImplemented
        return NotImplemented


class DictType(metaclass=ABCMeta):
    """
    Dict Type.

    Examples:
        >>> class Dict: a = 1
        >>> class Slots: a = 1; __slots__ = tuple()
        >>>
        >>> d = Dict()
        >>> s = Slots()
        >>>
        >>> Es(Dict).dicttype_sub
        True
        >>> Es(d).dicttype
        True
        >>>
        >>> Es(Slots).dicttype_sub
        False
        >>> Es(s).dicttype
        False
    """
    __dict__ = dict()

    @classmethod
    def __subclasshook__(cls, C):
        if cls is DictType:
            return Private.DICT.mro_first_dict(C) is not NotImplemented
        return NotImplemented


class GetAttrNoBuiltinType(metaclass=ABCMeta):
    """
    Get Attr Type (Everything but builtins, except: object and errors)

    Examples:
        >>> class Dict: a = 1
        >>> class G: a = 1; get = lambda self, item: self.__getattribute__(item)
        >>> Named = namedtuple('Named', 'a')
        >>>
        >>> d = Dict()
        >>> dct = dict(a=1)
        >>> g = G()
        >>> n = Named('a')
        >>> t = tuple()
        >>>
        >>> Es(Dict).getattrnobuiltintype_sub
        True
        >>> Es(d).getattrnobuiltintype
        True
        >>>
        >>> Es(G).getattrnobuiltintype_sub
        False
        >>> Es(g).getattrnobuiltintype
        False
        >>>
        >>> Es(dict).getattrnobuiltintype_sub
        False
        >>> Es(dct).getattrnobuiltintype
        False
        >>>
        >>> Es(tuple).getattrnobuiltintype_sub
        False
        >>> Es(t).getattrnobuiltintype
        False
        >>>
        >>> Es(list).getattrnobuiltintype_sub
        False
        >>> Es(list()).getattrnobuiltintype
        False
        >>>
        >>> Es(Named).getattrnobuiltintype_sub
        True
        >>> Es(n).getattrnobuiltintype
        True
        """

    @abstractmethod
    def __getattribute__(self, n):
        return object.__getattribute__(self, n)

    @classmethod
    def __subclasshook__(cls, C):
        if cls is GetAttrNoBuiltinType:
            g = Public.GET.mro_first_dict(C)
            return any([Protected.FIELD_DEFAULTS.mro_first_dict(C) is not NotImplemented,
                        not allin(C.__mro__, BUILTINS_CLASSES) and g is NotImplemented or
                        (g is not NotImplemented and not callable(g))])
        return NotImplemented


class GetAttrType(metaclass=ABCMeta):
    """
    Get Attr Type (Everything but GetType)

    Examples:
        >>> class Dict: a = 1
        >>> class G: a = 1; get = lambda self, item: self.__getattribute__(item)
        >>> Named = namedtuple('Named', 'a')
        >>>
        >>> d = Dict()
        >>> dct = dict(a=1)
        >>> g = G()
        >>> n = Named('a')
        >>> t = tuple()
        >>>
        >>> Es(Dict).getattrtype_sub
        True
        >>> Es(d).getattrtype
        True
        >>>
        >>> Es(G).getattrtype_sub
        False
        >>> Es(g).getattrtype
        False
        >>>
        >>> Es(dict).getattrtype_sub
        False
        >>> Es(dct).getattrtype
        False
        >>>
        >>> Es(tuple).getattrtype_sub
        True
        >>> Es(t).getattrtype
        True
        >>>
        >>> Es(list).getattrtype_sub
        True
        >>> Es(list()).getattrtype
        True
        >>>
        >>> Es(Named).getattrtype_sub
        True
        >>> Es(n).getattrtype
        True
        """

    @abstractmethod
    def __getattribute__(self, n):
        return object.__getattribute__(self, n)

    @classmethod
    def __subclasshook__(cls, C):
        if cls is GetAttrType:
            g = Public.GET.mro_first_dict(C)
            return any([Protected.FIELD_DEFAULTS.mro_first_dict(C) is not NotImplemented,
                        g is NotImplemented or (g is not NotImplemented and not callable(g))])
        return NotImplemented


@runtime_checkable
class GetItemSupportType(Protocol):
    """Supports __getitem__."""
    __slots__ = tuple()

    @abstractmethod
    def __getitem__(self, index):
        return self[index]


@runtime_checkable
class GetSupportType(Protocol):
    """Supports get method."""
    __slots__ = tuple()

    @abstractmethod
    def get(self, name, default=None):
        return self, name, default


@runtime_checkable
class GetType(Protocol):
    """
    Get Type.

    Examples:
        >>> class Dict: a = 1
        >>> class G: a = 1; get = lambda self, item: self.__getattribute__(item)
        >>> class Slots: a = 1; __slots__ = tuple()
        >>>
        >>> d = Dict()
        >>> dct = dict(a=1)
        >>> g = G()
        >>>
        >>> dct.get('a')
        1
        >>> g.get('a')
        1
        >>>
        >>> Es(Dict).gettype_sub
        False
        >>> Es(d).gettype
        False
        >>>
        >>> Es(G).gettype_sub
        True
        >>> Es(g).gettype
        True
        >>>
        >>> Es(dict).gettype_sub
        True
        >>> Es(dct).gettype
        True
    """

    @abstractmethod
    def get(self, name, default=None):
        pass


class NamedType(metaclass=ABCMeta):
    """
    named Type.

    Examples:
        >>> named = namedtuple('named', 'a', defaults=('a', ))
        >>>
        >>> Es(named()).namedtype
        True
        >>> Es(named).namedtype_sub
        True
        >>>
        >>> Es(named()).tuple
        True
        >>> issubclass(named, tuple)
        True
    """
    _fields = tuple()
    _field_defaults = dict()

    @abstractmethod
    def _asdict(self):
        return dict()

    @classmethod
    def __subclasshook__(cls, C):
        if cls is NamedType:
            _asdict = Protected.ASDICT.mro_first_dict(C)
            rv = Protected.FIELD_DEFAULTS.mro_first_dict(C) is not NotImplemented and (
                    _asdict is not NotImplemented and callable(_asdict)) and Protected.FIELDS.mro_first_dict(
                C) is not NotImplemented
            return rv
        return NotImplemented


class NamedAnnotationsType(metaclass=ABCMeta):
    """
    named Type.

    Examples:
        >>> named = namedtuple('named', 'a', defaults=('a', ))
        >>> Named = NamedTuple('Named', a=str)
        >>>
        >>> Es(named()).named_annotationstype
        False
        >>> Es(named).named_annotationstype_sub
        False
        >>>
        >>> Es(Named('a')).named_annotationstype
        True
        >>> Es(Named).named_annotationstype_sub
        True
        >>>
        >>> Es(named()).tuple
        True
        >>> issubclass(named, tuple)
        True
    """
    __annotations__ = dict()
    _fields = tuple()
    _field_defaults = dict()

    @abstractmethod
    def _asdict(self):
        return dict()

    @classmethod
    def __subclasshook__(cls, C):
        if cls is NamedAnnotationsType:
            _asdict = Protected.ASDICT.mro_first_dict(C)
            _a = _asdict is not NotImplemented and callable(_asdict)
            value = Private.ANNOTATIONS.mro_first_dict(C)
            return value is not NotImplemented and Protected.FIELD_DEFAULTS.mro_first_dict(
                C) is not NotImplemented and _a and Protected.FIELDS.mro_first_dict(C) is not NotImplemented
        return NotImplemented


class SlotsType(metaclass=ABCMeta):
    """
    Slots Type.

    Examples:
        >>> class Dict: a = 1
        >>> class Slots: a = 1; __slots__ = tuple()
        >>>
        >>> d = Dict()
        >>> s = Slots()
        >>>
        >>> Es(Dict).slotstype_sub
        False
        >>> Es(d).slotstype
        False
        >>>
        >>> Es(Slots).slotstype_sub
        True
        >>> Es(s).slotstype
        True
    """

    @classmethod
    def __subclasshook__(cls, C):
        if cls is SlotsType:
            return Private.SLOTS.mro_first_dict_no_object(C) is not NotImplemented
        return NotImplemented


# </editor-fold>
# <editor-fold desc="Classes">
class BoxKeys(Box):
    """
    Creates a Box with values from keys.
    """
    def __init__(self, keys, value='lower'):
        """
        Creates Box instance.

        Examples:
            >>> pretty_install()
            >>>
            >>> BoxKeys('a b', value=None)
            <Box: {'a': 'a', 'b': 'b'}>
            >>> BoxKeys('A B')
            <Box: {'A': 'a', 'B': 'b'}>
            >>> BoxKeys('A B', value=list)
            <Box: {'A': [], 'B': []}>

        Args:
            keys: keys to use for keys and values.
            value: Type or function to use to init the Box.

        Returns:
            Initialize box from keys.
        """
        es = Es(value)
        super().__init__({item: getattr(item, value)() if es.str else item if es.none else value()
                          for item in to_iter(keys)})


class Chain(ChainMap):
    """Variant of chain that allows direct updates to inner scopes and returns more than one value,
    not the first one."""
    rv = ChainRV.UNIQUE
    default = None
    maps = list()

    def __init__(self, *maps, rv=ChainRV.UNIQUE, default=None):
        super().__init__(*maps)
        self.rv = rv
        self.default = default

    def __getitem__(self, key):
        rv = []
        for mapping in self.maps:
            if Es(mapping).namedtype:
                mapping = mapping._asdict()
            elif hasattr(mapping, 'asdict'):
                to_dict = getattr(mapping.__class__, 'asdict')
                if isinstance(to_dict, property):
                    mapping = mapping.asdict
                elif callable(to_dict):
                    mapping = mapping.asdict()
            if hasattr(mapping, '__getitem__'):
                try:
                    value = mapping[key]
                    if self.rv is ChainRV.FIRST:
                        return value
                    if (self.rv is ChainRV.UNIQUE and value not in rv) or self.rv is ChainRV.ALL:
                        rv.append(value)
                except KeyError:
                    pass
            elif hasattr(mapping, '__getattribute__') and isinstance(key, str) and \
                    not isinstance(mapping, (tuple, bool, int, str, bytes)):
                try:
                    value = getattr(mapping, key)
                    if self.rv is ChainRV.FIRST:
                        return value
                    if (self.rv is ChainRV.UNIQUE and value not in rv) or self.rv is ChainRV.ALL:
                        rv.append(value)
                except AttributeError:
                    pass
        return self.default if self.rv is ChainRV.FIRST else rv

    def __delitem__(self, key):
        index = 0
        deleted = []
        found = False
        for mapping in self.maps:
            if mapping:
                if not isinstance(mapping, (tuple, bool, int, str, bytes)):
                    if hasattr(mapping, '__delitem__'):
                        if key in mapping:
                            del mapping[key]
                            if self.rv is ChainRV.FIRST:
                                found = True
                    elif hasattr(mapping, '__delattr__') and hasattr(mapping, key) and isinstance(key, str):
                        delattr(mapping.__class__, key) if key in dir(mapping.__class__) else delattr(mapping, key)
                        if self.rv is ChainRV.FIRST:
                            found = True
                if not mapping:
                    deleted.append(index)
                if found:
                    break
            index += 1
        for index in reversed(deleted):
            del self.maps[index]
        return self

    def delete(self, key):
        del self[key]
        return self

    def __setitem__(self, key, value):
        found = False
        for mapping in self.maps:
            if mapping:
                if not isinstance(mapping, (tuple, bool, int, str, bytes)):
                    if hasattr(mapping, '__setitem__'):
                        if key in mapping:
                            mapping[key] = value
                            if self.rv is ChainRV.FIRST:
                                found = True
                    elif hasattr(mapping, '__setattr__') and hasattr(mapping, key) and isinstance(key, str):
                        setattr(mapping, key, value)
                        if self.rv is ChainRV.FIRST:
                            found = True
                if found:
                    break
        if not found and not isinstance(self.maps[0], (tuple, bool, int, str, bytes)):
            if hasattr(self.maps[0], '__setitem__'):
                self.maps[0][key] = value
            elif hasattr(self.maps[0], '__setattr__') and isinstance(key, str):
                setattr(self.maps[0], key, value)
        return self

    def set(self, key, value):
        return self.__setitem__(key, value)


class pproperty(property):
    """
    Print property.

    Examples:
        >>> pretty_install()
        >>> class Test:
        ...     _pp = 0
        ...     @pproperty
        ...     def pp(self):
        ...         self._pp += 1
        ...         prop = Es(self.__class__.__dict__['pp']).prop
        ...         pprop = Es(self.__class__.__dict__['pp']).pproperty
        ...         return self._pp, prop, pprop
        >>> test = Test()
        >>> test.pp
        (1, True, True)
        >>> test.pp
        (2, True, True)
    """

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        super().__init__(fget=fget, fset=fset, fdel=fdel, doc=doc)


# </editor-fold>
# <editor-fold desc="Bases">
class BaseState:
    """
    Deepcopy and Pickle State Base Class.

    Examples:
        >>> from copy import deepcopy
        >>>
        >>> class Test(BaseState):
        ...     __pickle__ = ('attribute', )
        ...     __slots__ = ('attribute', )
        ...     def __init__(self): self.attribute = dict(a=1)
        >>>
        >>> test = Test()
        >>> test_copy = test
        >>> test_deepcopy = deepcopy(test)
        >>> assert id(test) == id(test_copy)
        >>> assert id(test) != id(test_deepcopy)
        >>> test.attribute['a'] = 2
        >>> assert id(test.attribute) == id(test_copy.attribute)
        >>> assert id(test.attribute) != id(test_deepcopy.attribute)
        >>> assert test_copy.attribute['a'] == 2
        >>> assert test_deepcopy.attribute['a'] == 1
    """
    __pickle__ = ()
    __slots__ = ()
    def __getstate__(self): return Es(self).state()
    def __setstate__(self, state): Es(self).state(state)


# </editor-fold>
# <editor-fold desc="States">
class StateEnv(Environs, BaseState):
    """
    Env Class with Deepcopy and Pickle.

    Examples:
        >>> from copy import deepcopy
        >>> from rc import StateEnv
        >>> import environs
        >>>
        >>> env = StateEnv()
        >>> term = env('TERM')
        >>> env
        <StateEnv {'TERM': 'xterm-256color'}>
        >>> state = env.__getstate__()
        >>> env_deepcopy = deepcopy(env)
        >>> env_deepcopy
        <StateEnv {'TERM': 'xterm-256color'}>
        >>> assert id(env_deepcopy) != id(env)
        >>> assert id(env_deepcopy._values) != id(env._values)
    """
    def __init__(self, *, eager=True, expand_vars=False):
        super().__init__(eager=eager, expand_vars=expand_vars)


# </editor-fold>
# <editor-fold desc="Echo">
def black(msg, bold=False, nl=True, underline=False,
          blink=False, err=False, reset=True, rc=None) -> None:
    """
    Black.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='black', err=err, reset=reset)
    if rc is not None:
        Exit(rc)


def blue(msg, bold=False, nl=True, underline=False,
         blink=False, err=False, reset=True, rc=None) -> None:
    """
    Blue.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='blue', err=err, reset=reset)
    if rc is not None:
        Exit(rc)


def cyan(msg, bold=False, nl=True, underline=False,
         blink=False, err=False, reset=True, rc=None) -> None:
    """
    Cyan.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='cyan', err=err, reset=reset)
    if rc is not None:
        Exit(rc)


def green(msg, bold=False, nl=True, underline=False,
          blink=False, err=False, reset=True, rc=None) -> None:
    """
    Green.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='green', err=err, reset=reset)
    if rc is not None:
        Exit(rc)


def magenta(msg, bold=False, nl=True, underline=False,
            blink=False, err=False, reset=True, rc=None) -> None:
    """
    Magenta.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='magenta', err=err, reset=reset)
    if rc is not None:
        Exit(rc)


def red(msg, bold=False, nl=True, underline=False,
        blink=False, err=True, reset=True, rc=None) -> None:
    """
    Red.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='red', err=err, reset=reset)
    if rc is not None:
        Exit(rc)


def white(msg, bold=False, nl=True, underline=False,
          blink=False, err=False, reset=True, rc=None) -> None:
    """
    White.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='white', err=err, reset=reset)
    if rc is not None:
        Exit(rc)


def yellow(msg, bold=False, nl=True, underline=False,
           blink=False, err=True, reset=True, rc=None) -> None:
    """
    Yellow.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='yellow', err=err, reset=reset)
    if rc is not None:
        Exit(rc)


def bblack(msg, bold=False, nl=True, underline=False,
           blink=False, err=False, reset=True, rc=None) -> None:
    """
    Black.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='bright_black', err=err,
          reset=reset)
    if rc is not None:
        Exit(rc)


def bblue(msg, bold=False, nl=True, underline=False,
          blink=False, err=False, reset=True, rc=None) -> None:
    """
    Bblue.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='bright_blue', err=err,
          reset=reset)
    if rc is not None:
        Exit(rc)


def bcyan(msg, bold=False, nl=True, underline=False,
          blink=False, err=False, reset=True, rc=None) -> None:
    """
    Bcyan.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='bright_cyan', err=err,
          reset=reset)
    if rc is not None:
        Exit(rc)


def bgreen(msg, bold=False, nl=True, underline=False,
           blink=False, err=False, reset=True, rc=None) -> None:
    """
    Bgreen.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='bright_green', err=err,
          reset=reset)
    if rc is not None:
        Exit(rc)


def bmagenta(msg, bold=False, nl=True, underline=False,
             blink=False, err=False, reset=True, rc=None) -> None:
    """
    Bmagenta.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='bright_magenta', err=err,
          reset=reset)
    if rc is not None:
        Exit(rc)


def bred(msg, bold=False, nl=True, underline=False,
         blink=False, err=False, reset=True, rc=None) -> None:
    """
    Bred.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='bright_red', err=err,
          reset=reset)
    if rc is not None:
        Exit(rc)


def bwhite(msg, bold=False, nl=True, underline=False,
           blink=False, err=False, reset=True, rc=None) -> None:
    """
    Bwhite.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='bright_white', err=err,
          reset=reset)
    if rc is not None:
        Exit(rc)


def byellow(msg, bold=False, nl=True, underline=False,
            blink=False, err=False, reset=True, rc=None) -> None:
    """
    Byellow.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='bright_yellow', err=err,
          reset=reset)
    if rc is not None:
        Exit(rc)


# </editor-fold>
# <editor-fold desc="Test">
class TestAsync:
    _async_classmethod = varname(1, sep=str())
    _classmethod = varname(1, sep=str())
    _async_method = varname(1, sep=str())
    _method = varname(1, sep=str())
    _cprop = varname(1, sep=str())
    _async_pprop = varname(1, sep=str())
    _pprop = varname(1, sep=str())
    _async_prop = varname(1, sep=str())
    _prop = varname(1, sep=str())
    _async_staticmethod = varname(1, sep=str())
    _staticmethod = varname(1, sep=str())

    @classmethod
    async def async_classmethod(cls): return cls._async_classmethod

    @classmethod
    def classmethod(cls): return cls._classmethod

    async def async_method(self): return self._async_method

    def method(self): return self._method

    @cached_property
    def cprop(self): return self._cprop

    @pproperty
    async def async_pprop(self): return self._async_pprop

    @pproperty
    def pprop(self): return self._pprop

    @property
    async def async_prop(self): return self._async_prop

    @property
    def prop(self): return self._prop

    @staticmethod
    async def async_staticmethod(): return TestAsync._async_staticmethod

    @staticmethod
    def staticmethod(): return TestAsync._staticmethod


@dataclass
class TestData:
    __data = varname(1)
    __dataclass_classvar__: ClassVar[str] = '__dataclass_classvar__'
    __dataclass_classvar: ClassVar[str] = '__dataclass_classvar'
    __dataclass_default_factory: Union[dict, str] = datafield(default_factory=dict, init=False)
    __dataclass_default_factory_init: Union[dict, str] = datafield(default_factory=dict)
    dataclass_classvar: ClassVar[str] = 'dataclass_classvar'
    dataclass_default_factory: Union[dict, str] = datafield(default_factory=dict, init=False)
    dataclass_default_factory_init: Union[dict, str] = datafield(default_factory=dict)
    dataclass_default: str = datafield(default='dataclass_default', init=False)
    dataclass_default_init: str = datafield(default='dataclass_default_init')
    dataclass_initvar: InitVar[str] = 'dataclass_initvar'
    dataclass_str: str = 'dataclass_integer'

    def __post_init__(self, dataclass_initvar): pass

    __class_getitem__ = classmethod(GenericAlias)


class TestDataDictMix(TestData):
    subclass_annotated_str: str = 'subclass_annotated_str'
    subclass_classvar: ClassVar[str] = 'subclass_classvar'
    subclass_str = 'subclass_str'

    def __init__(self, dataclass_initvar='dataclass_initvar_1', subclass_dynamic='subclass_dynamic'):
        super().__init__()
        super().__post_init__(dataclass_initvar=dataclass_initvar)
        self.subclass_dynamic = subclass_dynamic


class TestDataDictSlotMix(TestDataDictMix):
    __slots__ = ('_slot_property', 'slot',)

    # Add init=True dataclass attrs if it subclassed and not @dataclass
    def __init__(self, dataclass_initvar='dataclass_initvar_2', slot_property='slot_property', slot='slot'):
        super().__init__()
        super().__post_init__(dataclass_initvar=dataclass_initvar)
        self._slot_property = slot_property
        self.slot = slot

    @pproperty
    def slot_property(self):
        return self._slot_property


# </editor-fold>
# <editor-fold desc="Start">
pretty_install(console=console, expand_all=True)
# rich.traceback.install(console=console, extra_lines=5, show_locals=True)
pickle_np.register_handlers()


# </editor-fold>
