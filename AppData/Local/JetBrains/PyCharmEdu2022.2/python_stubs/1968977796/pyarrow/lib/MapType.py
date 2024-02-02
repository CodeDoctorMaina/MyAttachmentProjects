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


from .DataType import DataType

class MapType(DataType):
    """
    Concrete class for map data types.
    
        Examples
        --------
        Create an instance of MapType:
    
        >>> import pyarrow as pa
        >>> pa.map_(pa.string(), pa.int32())
        MapType(map<string, int32>)
        >>> pa.map_(pa.string(), pa.int32(), keys_sorted=True)
        MapType(map<string, int32, keys_sorted>)
    """
    def __init__(self, map, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ MapType.__reduce__(self) """
        pass

    item_field = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The field for items in the map entries.

        Examples
        --------
        >>> import pyarrow as pa
        >>> pa.map_(pa.string(), pa.int32()).item_field
        pyarrow.Field<value: int32>
        """

    item_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The data type of items in the map entries.

        Examples
        --------
        >>> import pyarrow as pa
        >>> pa.map_(pa.string(), pa.int32()).item_type
        DataType(int32)
        """

    keys_sorted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Should the entries be sorted according to keys.

        Examples
        --------
        >>> import pyarrow as pa
        >>> pa.map_(pa.string(), pa.int32(), keys_sorted=True).keys_sorted
        True
        """

    key_field = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The field for keys in the map entries.

        Examples
        --------
        >>> import pyarrow as pa
        >>> pa.map_(pa.string(), pa.int32()).key_field
        pyarrow.Field<key: string not null>
        """

    key_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The data type of keys in the map entries.

        Examples
        --------
        >>> import pyarrow as pa
        >>> pa.map_(pa.string(), pa.int32()).key_type
        DataType(string)
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000029E0467A570>'


