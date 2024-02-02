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

class RunEndEncodedArray(Array):
    """ Concrete class for Arrow run-end encoded arrays. """
    def find_physical_length(self): # real signature unknown; restored from __doc__
        """
        RunEndEncodedArray.find_physical_length(self)
        
                Find the physical length of this REE array.
        
                The physical length of an REE is the number of physical values (and
                run-ends) necessary to represent the logical range of values from offset
                to length.
        
                This function uses binary-search, so it has a O(log N) cost.
        """
        pass

    def find_physical_offset(self): # real signature unknown; restored from __doc__
        """
        RunEndEncodedArray.find_physical_offset(self)
        
                Find the physical offset of this REE array.
        
                This is the offset of the run that contains the value of the first
                logical element of this array considering its offset.
        
                This function uses binary-search, so it has a O(log N) cost.
        """
        pass

    def from_arrays(self, run_ends, values, type=None): # real signature unknown; restored from __doc__
        """
        RunEndEncodedArray.from_arrays(run_ends, values, type=None)
        
                Construct RunEndEncodedArray from run_ends and values arrays.
        
                Parameters
                ----------
                run_ends : Array (int16, int32, or int64 type)
                    The run_ends array.
                values : Array (any type)
                    The values array.
                type : pyarrow.DataType, optional
                    The run_end_encoded(run_end_type, value_type) array type.
        
                Returns
                -------
                RunEndEncodedArray
        """
        pass

    def from_buffers(self, DataType_type, length, buffers, null_count=-1, offset=0, children=None): # real signature unknown; restored from __doc__
        """
        RunEndEncodedArray.from_buffers(DataType type, length, buffers, null_count=-1, offset=0, children=None)
        
                Construct a RunEndEncodedArray from all the parameters that make up an
                Array.
        
                RunEndEncodedArrays do not have buffers, only children arrays, but this
                implementation is needed to satisfy the Array interface.
        
                Parameters
                ----------
                type : DataType
                    The run_end_encoded(run_end_type, value_type) type.
                length : int
                    The logical length of the run-end encoded array. Expected to match
                    the last value of the run_ends array (children[0]) minus the offset.
                buffers : List[Buffer]
                    Empty List or [None].
                null_count : int, default -1
                    The number of null entries in the array. Run-end encoded arrays
                    are specified to not have valid bits and null_count always equals 0.
                offset : int, default 0
                    The array's logical offset (in values, not in bytes) from the
                    start of each buffer.
                children : List[Array]
                    Nested type children containing the run_ends and values arrays.
        
                Returns
                -------
                RunEndEncodedArray
        """
        pass

    def _from_arrays(self, type, allow_none_for_type, logical_length, run_ends, values, logical_offset): # real signature unknown; restored from __doc__
        """ RunEndEncodedArray._from_arrays(type, allow_none_for_type, logical_length, run_ends, values, logical_offset) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    run_ends = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        An array holding the logical indexes of each run-end.

        The physical offset to the array is applied.
        """

    values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        An array holding the values of each run.

        The physical offset to the array is applied.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000029E04703450>'


