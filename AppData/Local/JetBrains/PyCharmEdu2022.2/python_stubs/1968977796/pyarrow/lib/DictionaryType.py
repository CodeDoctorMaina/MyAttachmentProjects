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

class DictionaryType(DataType):
    """
    Concrete class for dictionary data types.
    
        Examples
        --------
        Create an instance of dictionary type:
    
        >>> import pyarrow as pa
        >>> pa.dictionary(pa.int64(), pa.utf8())
        DictionaryType(dictionary<values=string, indices=int64, ordered=0>)
    """
    def __init__(self, dictionary, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ DictionaryType.__reduce__(self) """
        pass

    index_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The data type of dictionary indices (a signed integer type).

        Examples
        --------
        >>> import pyarrow as pa
        >>> pa.dictionary(pa.int16(), pa.utf8()).index_type
        DataType(int16)
        """

    ordered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Whether the dictionary is ordered, i.e. whether the ordering of values
        in the dictionary is important.

        Examples
        --------
        >>> import pyarrow as pa
        >>> pa.dictionary(pa.int64(), pa.utf8()).ordered
        False
        """

    value_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The dictionary value type.

        The dictionary values are found in an instance of DictionaryArray.

        Examples
        --------
        >>> import pyarrow as pa
        >>> pa.dictionary(pa.int16(), pa.utf8()).value_type
        DataType(string)
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000029E0467A6C0>'


