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


from .Array import Array

class BaseListArray(Array):
    # no doc
    def flatten(self): # real signature unknown; restored from __doc__
        """
        BaseListArray.flatten(self)
        
                Unnest this ListArray/LargeListArray by one level.
        
                The returned Array is logically a concatenation of all the sub-lists
                in this Array.
        
                Note that this method is different from ``self.values`` in that
                it takes care of the slicing offset as well as null elements backed
                by non-empty sub-lists.
        
                Returns
                -------
                result : Array
        """
        pass

    def value_lengths(self): # real signature unknown; restored from __doc__
        """
        BaseListArray.value_lengths(self)
        
                Return integers array with values equal to the respective length of
                each list element. Null list values are null in the output.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> arr = pa.array([[1, 2, 3], [], None, [4]],
                ...                type=pa.list_(pa.int32()))
                >>> arr.value_lengths()
                <pyarrow.lib.Int32Array object at ...>
                [
                  3,
                  0,
                  null,
                  1
                ]
        """
        pass

    def value_parent_indices(self): # real signature unknown; restored from __doc__
        """
        BaseListArray.value_parent_indices(self)
        
                Return array of same length as list child values array where each
                output value is the index of the parent list array slot containing each
                child value.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> arr = pa.array([[1, 2, 3], [], None, [4]],
                ...                type=pa.list_(pa.int32()))
                >>> arr.value_parent_indices()
                <pyarrow.lib.Int64Array object at ...>
                [
                  0,
                  0,
                  0,
                  3
                ]
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000029E04689720>'


