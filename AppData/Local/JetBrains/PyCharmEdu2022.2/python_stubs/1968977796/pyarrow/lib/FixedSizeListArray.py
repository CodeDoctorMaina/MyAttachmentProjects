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


from .BaseListArray import BaseListArray

class FixedSizeListArray(BaseListArray):
    """ Concrete class for Arrow arrays of a fixed size list data type. """
    def from_arrays(self, values, list_size=None, DataType_type=None, mask=None): # real signature unknown; restored from __doc__
        """
        FixedSizeListArray.from_arrays(values, list_size=None, DataType type=None, mask=None)
        
                Construct FixedSizeListArray from array of values and a list length.
        
                Parameters
                ----------
                values : Array (any type)
                list_size : int
                    The fixed length of the lists.
                type : DataType, optional
                    If not specified, a default ListType with the values' type and
                    `list_size` length is used.
                mask : Array (boolean type), optional
                    Indicate which values are null (True) or not null (False).
        
        
                Returns
                -------
                FixedSizeListArray
        
                Examples
                --------
        
                Create from a values array and a list size:
        
                >>> import pyarrow as pa
                >>> values = pa.array([1, 2, 3, 4])
                >>> arr = pa.FixedSizeListArray.from_arrays(values, 2)
                >>> arr
                <pyarrow.lib.FixedSizeListArray object at ...>
                [
                  [
                    1,
                    2
                  ],
                  [
                    3,
                    4
                  ]
                ]
        
                Or create from a values array, list size and matching type:
        
                >>> typ = pa.list_(pa.field("values", pa.int64()), 2)
                >>> arr = pa.FixedSizeListArray.from_arrays(values,type=typ)
                >>> arr
                <pyarrow.lib.FixedSizeListArray object at ...>
                [
                  [
                    1,
                    2
                  ],
                  [
                    3,
                    4
                  ]
                ]
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the underlying array of values which backs the
        FixedSizeListArray.

        Note even null elements are included.

        Compare with :meth:`flatten`, which returns only the non-null
        sub-list values.

        Returns
        -------
        values : Array

        See Also
        --------
        FixedSizeListArray.flatten : ...

        Examples
        --------
        >>> import pyarrow as pa
        >>> array = pa.array(
        ...     [[1, 2], None, [3, None]],
        ...     type=pa.list_(pa.int32(), 2)
        ... )
        >>> array.values
        <pyarrow.lib.Int32Array object at ...>
        [
          1,
          2,
          null,
          null,
          3,
          null
        ]

        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000029E046898A0>'


