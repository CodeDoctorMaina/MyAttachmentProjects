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


from .ExtensionType import ExtensionType

class PyExtensionType(ExtensionType):
    """
    PyExtensionType(DataType storage_type)
    
        Concrete base class for Python-defined extension types based on pickle
        for (de)serialization.
    
        .. warning::
           This class is deprecated and its deserialization is disabled by default.
           :class:`ExtensionType` is recommended instead.
    
        Parameters
        ----------
        storage_type : DataType
            The storage type for which the extension is built.
    """
    @classmethod
    def set_auto_load(cls, type_cls, value): # real signature unknown; restored from __doc__
        """
        PyExtensionType.set_auto_load(type cls, value)
        
                Enable or disable auto-loading of serialized PyExtensionType instances.
        
                Parameters
                ----------
                value : bool
                    Whether to enable auto-loading.
        """
        pass

    @classmethod
    def __arrow_ext_deserialize__(cls, type_cls, storage_type, serialized): # real signature unknown; restored from __doc__
        """ PyExtensionType.__arrow_ext_deserialize__(type cls, storage_type, serialized) """
        pass

    def __arrow_ext_serialize__(self): # real signature unknown; restored from __doc__
        """ PyExtensionType.__arrow_ext_serialize__(self) """
        pass

    def __init__(self, DataType_storage_type): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ PyExtensionType.__reduce__(self) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000029E0467AB40>'


