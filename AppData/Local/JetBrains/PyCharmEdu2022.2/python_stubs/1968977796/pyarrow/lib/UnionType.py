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

class UnionType(DataType):
    """
    Base class for union data types.
    
        Examples
        --------
        Create an instance of a dense UnionType using ``pa.union``:
    
        >>> import pyarrow as pa
        >>> pa.union([pa.field('a', pa.binary(10)), pa.field('b', pa.string())],
        ...          mode=pa.lib.UnionMode_DENSE),
        (DenseUnionType(dense_union<a: fixed_size_binary[10]=0, b: string=1>),)
    
        Create an instance of a dense UnionType using ``pa.dense_union``:
    
        >>> pa.dense_union([pa.field('a', pa.binary(10)), pa.field('b', pa.string())])
        DenseUnionType(dense_union<a: fixed_size_binary[10]=0, b: string=1>)
    
        Create an instance of a sparse UnionType using ``pa.union``:
    
        >>> pa.union([pa.field('a', pa.binary(10)), pa.field('b', pa.string())],
        ...          mode=pa.lib.UnionMode_SPARSE),
        (SparseUnionType(sparse_union<a: fixed_size_binary[10]=0, b: string=1>),)
    
        Create an instance of a sparse UnionType using ``pa.sparse_union``:
    
        >>> pa.sparse_union([pa.field('a', pa.binary(10)), pa.field('b', pa.string())])
        SparseUnionType(sparse_union<a: fixed_size_binary[10]=0, b: string=1>)
    """
    def field(self, i): # real signature unknown; restored from __doc__
        """
        UnionType.field(self, i) -> Field
        
                Return a child field by its numeric index.
        
                Parameters
                ----------
                i : int
        
                Returns
                -------
                pyarrow.Field
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> union = pa.sparse_union([pa.field('a', pa.binary(10)), pa.field('b', pa.string())])
                >>> union[0]
                pyarrow.Field<a: fixed_size_binary[10]>
        """
        return Field

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """
        Return a child field by its index.
        
                Alias of ``field``.
        """
        pass

    def __init__(self, dense_union, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Iterate over union members, in order. """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Like num_fields(). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ UnionType.__reduce__(self) """
        pass

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The mode of the union ("dense" or "sparse").

        Examples
        --------
        >>> import pyarrow as pa
        >>> union = pa.sparse_union([pa.field('a', pa.binary(10)), pa.field('b', pa.string())])
        >>> union.mode
        'sparse'
        """

    type_codes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The type code to indicate each data type in this union.

        Examples
        --------
        >>> import pyarrow as pa
        >>> union = pa.sparse_union([pa.field('a', pa.binary(10)), pa.field('b', pa.string())])
        >>> union.type_codes
        [0, 1]
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000029E046F7240>'


