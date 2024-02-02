# encoding: utf-8
# module pyarrow.lib
# from C:\Users\hp\PycharmProjects\Text_Summarizer\venv\lib\site-packages\pyarrow\lib.cp38-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import datetime as datetime # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\datetime.py
import decimal as _pydecimal # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\decimal.py
import numpy as np # C:\Users\hp\PycharmProjects\Text_Summarizer\venv\lib\site-packages\numpy\__init__.py
import os as os # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\os.py
import sys as sys # <module 'sys' (built-in)>
import pickle as pickle # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\pickle.py
import signal as signal # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\signal.py
import threading as threading # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\threading.py
import warnings as warnings # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\warnings.py
import atexit as atexit # <module 'atexit' (built-in)>
import re as re # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\re.py
import collections as collections # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\collections\__init__.py
import codecs as codecs # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\codecs.py
import time as time # <module 'time' (built-in)>
from _queue import QueueEmpty

import collections.abc as __collections_abc
import enum as __enum
import importlib._bootstrap as __importlib__bootstrap
import io as __io
import _io as ___io


from .tuple import tuple

class BuildInfo(tuple):
    """ BuildInfo(version, version_info, so_version, full_so_version, compiler_id, compiler_version, compiler_flags, git_id, git_description, package_kind, build_type) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new dict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new BuildInfo object from a sequence or iterable """
        pass

    def _replace(self, **kwds): # reliably restored by inspect
        """ Return a new BuildInfo object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, version, version_info, so_version, full_so_version, compiler_id, compiler_version, compiler_flags, git_id, git_description, package_kind, build_type): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, version, version_info, so_version, full_so_version, compiler_id, compiler_version, compiler_flags, git_id, git_description, package_kind, build_type): # reliably restored by inspect
        """ Create new instance of BuildInfo(version, version_info, so_version, full_so_version, compiler_id, compiler_version, compiler_flags, git_id, git_description, package_kind, build_type) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    build_type = None # (!) real value is '<_collections._tuplegetter object at 0x0000029E0B058CA0>'
    compiler_flags = None # (!) real value is '<_collections._tuplegetter object at 0x0000029E0B058BB0>'
    compiler_id = None # (!) real value is '<_collections._tuplegetter object at 0x0000029E0B058B50>'
    compiler_version = None # (!) real value is '<_collections._tuplegetter object at 0x0000029E0B058B80>'
    full_so_version = None # (!) real value is '<_collections._tuplegetter object at 0x0000029E0B058AF0>'
    git_description = None # (!) real value is '<_collections._tuplegetter object at 0x0000029E0B058C40>'
    git_id = None # (!) real value is '<_collections._tuplegetter object at 0x0000029E0B058BE0>'
    package_kind = None # (!) real value is '<_collections._tuplegetter object at 0x0000029E0B058C70>'
    so_version = None # (!) real value is '<_collections._tuplegetter object at 0x0000029E0B058B20>'
    version = None # (!) real value is '<_collections._tuplegetter object at 0x0000029E0B058A30>'
    version_info = None # (!) real value is '<_collections._tuplegetter object at 0x0000029E0B058A90>'
    _fields = (
        'version',
        'version_info',
        'so_version',
        'full_so_version',
        'compiler_id',
        'compiler_version',
        'compiler_flags',
        'git_id',
        'git_description',
        'package_kind',
        'build_type',
    )
    _fields_defaults = {}
    _field_defaults = {}
    __slots__ = ()


