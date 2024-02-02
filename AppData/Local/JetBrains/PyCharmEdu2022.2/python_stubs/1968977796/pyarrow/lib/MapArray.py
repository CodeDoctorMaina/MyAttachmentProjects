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


from .ListArray import ListArray

class MapArray(ListArray):
    """ Concrete class for Arrow arrays of a map data type. """
    def from_arrays(self, offsets, keys, items, DataType_type=None, MemoryPool_pool=None): # real signature unknown; restored from __doc__
        """
        MapArray.from_arrays(offsets, keys, items, DataType type=None, MemoryPool pool=None)
        
                Construct MapArray from arrays of int32 offsets and key, item arrays.
        
                Parameters
                ----------
                offsets : array-like or sequence (int32 type)
                keys : array-like or sequence (any type)
                items : array-like or sequence (any type)
                type : DataType, optional
                    If not specified, a default MapArray with the keys' and items' type is used.
                pool : MemoryPool
        
                Returns
                -------
                map_array : MapArray
        
                Examples
                --------
                First, let's understand the structure of our dataset when viewed in a rectangular data model.
                The total of 5 respondents answered the question "How much did you like the movie x?".
                The value -1 in the integer array means that the value is missing. The boolean array
                represents the null bitmask corresponding to the missing values in the integer array.
        
                >>> import pyarrow as pa
                >>> movies_rectangular = np.ma.masked_array([
                ...     [10, -1, -1],
                ...     [8, 4, 5],
                ...     [-1, 10, 3],
                ...     [-1, -1, -1],
                ...     [-1, -1, -1]
                ... ],
                ... [
                ...     [False, True, True],
                ...     [False, False, False],
                ...     [True, False, False],
                ...     [True, True, True],
                ...     [True, True, True],
                ... ])
        
                To represent the same data with the MapArray and from_arrays, the data is
                formed like this:
        
                >>> offsets = [
                ...     0, #  -- row 1 start
                ...     1, #  -- row 2 start
                ...     4, #  -- row 3 start
                ...     6, #  -- row 4 start
                ...     6, #  -- row 5 start
                ...     6, #  -- row 5 end
                ... ]
                >>> movies = [
                ...     "Dark Knight", #  ---------------------------------- row 1
                ...     "Dark Knight", "Meet the Parents", "Superman", #  -- row 2
                ...     "Meet the Parents", "Superman", #  ----------------- row 3
                ... ]
                >>> likings = [
                ...     10, #  -------- row 1
                ...     8, 4, 5, #  --- row 2
                ...     10, 3 #  ------ row 3
                ... ]
                >>> pa.MapArray.from_arrays(offsets, movies, likings).to_pandas()
                0                                  [(Dark Knight, 10)]
                1    [(Dark Knight, 8), (Meet the Parents, 4), (Sup...
                2              [(Meet the Parents, 10), (Superman, 3)]
                3                                                   []
                4                                                   []
                dtype: object
        
                If the data in the empty rows needs to be marked as missing, it's possible
                to do so by modifying the offsets argument, so that we specify `None` as
                the starting positions of the rows we want marked as missing. The end row
                offset still has to refer to the existing value from keys (and values):
        
                >>> offsets = [
                ...     0, #  ----- row 1 start
                ...     1, #  ----- row 2 start
                ...     4, #  ----- row 3 start
                ...     None, #  -- row 4 start
                ...     None, #  -- row 5 start
                ...     6, #  ----- row 5 end
                ... ]
                >>> pa.MapArray.from_arrays(offsets, movies, likings).to_pandas()
                0                                  [(Dark Knight, 10)]
                1    [(Dark Knight, 8), (Meet the Parents, 4), (Sup...
                2              [(Meet the Parents, 10), (Superman, 3)]
                3                                                 None
                4                                                 None
                dtype: object
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Flattened array of items across all maps in array"""

    keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Flattened array of keys across all maps in array"""


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000029E04689840>'


