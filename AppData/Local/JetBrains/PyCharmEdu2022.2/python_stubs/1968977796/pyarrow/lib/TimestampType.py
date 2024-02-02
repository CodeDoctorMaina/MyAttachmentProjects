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

class TimestampType(DataType):
    """
    Concrete class for timestamp data types.
    
        Examples
        --------
        >>> import pyarrow as pa
    
        Create an instance of timestamp type:
    
        >>> pa.timestamp('us')
        TimestampType(timestamp[us])
    
        Create an instance of timestamp type with timezone:
    
        >>> pa.timestamp('s', tz='UTC')
        TimestampType(timestamp[s, tz=UTC])
    """
    def __init__(self, timestamp, us=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ TimestampType.__reduce__(self) """
        pass

    tz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The timestamp time zone, if any, or None.

        Examples
        --------
        >>> import pyarrow as pa
        >>> t = pa.timestamp('s', tz='UTC')
        >>> t.tz
        'UTC'
        """

    unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The timestamp unit ('s', 'ms', 'us' or 'ns').

        Examples
        --------
        >>> import pyarrow as pa
        >>> t = pa.timestamp('us')
        >>> t.unit
        'us'
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000029E0467A720>'


