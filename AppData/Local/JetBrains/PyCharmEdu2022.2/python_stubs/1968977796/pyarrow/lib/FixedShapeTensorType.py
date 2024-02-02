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


from .BaseExtensionType import BaseExtensionType

class FixedShapeTensorType(BaseExtensionType):
    """
    Concrete class for fixed shape tensor extension type.
    
        Examples
        --------
        Create an instance of fixed shape tensor extension type:
    
        >>> import pyarrow as pa
        >>> pa.fixed_shape_tensor(pa.int32(), [2, 2])
        FixedShapeTensorType(extension<arrow.fixed_shape_tensor[value_type=int32, shape=[2,2]]>)
    
        Create an instance of fixed shape tensor extension type with
        permutation:
    
        >>> tensor_type = pa.fixed_shape_tensor(pa.int8(), (2, 2, 3),
        ...                                     permutation=[0, 2, 1])
        >>> tensor_type.permutation
        [0, 2, 1]
    """
    def __arrow_ext_class__(self): # real signature unknown; restored from __doc__
        """ FixedShapeTensorType.__arrow_ext_class__(self) """
        pass

    @classmethod
    def __arrow_ext_deserialize__(cls, type_self, storage_type, serialized): # real signature unknown; restored from __doc__
        """
        FixedShapeTensorType.__arrow_ext_deserialize__(type self, storage_type, serialized)
        
                Return an FixedShapeTensor type instance from the storage type and serialized
                metadata.
        """
        pass

    def __arrow_ext_serialize__(self): # real signature unknown; restored from __doc__
        """
        FixedShapeTensorType.__arrow_ext_serialize__(self)
        
                Serialized representation of metadata to reconstruct the type object.
        """
        pass

    def __init__(self, extension, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ FixedShapeTensorType.__reduce__(self) """
        pass

    dim_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Explicit names of the dimensions.
        """

    permutation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Indices of the dimensions ordering.
        """

    shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Shape of the tensors.
        """

    value_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Data type of an individual tensor.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000029E0467AAE0>'


