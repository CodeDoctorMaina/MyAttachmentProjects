# encoding: utf-8
# module pyarrow._compute
# from C:\Users\hp\PycharmProjects\Text_Summarizer\venv\lib\site-packages\pyarrow\_compute.cp38-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import pyarrow.lib as lib # C:\Users\hp\PycharmProjects\Text_Summarizer\venv\lib\site-packages\pyarrow\lib.cp38-win_amd64.pyd
import inspect as inspect # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\inspect.py
import numpy as np # C:\Users\hp\PycharmProjects\Text_Summarizer\venv\lib\site-packages\numpy\__init__.py
import warnings as warnings # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\warnings.py
from pyarrow.lib import ArrowInvalid, frombytes, tobytes

import pyarrow.lib as __pyarrow_lib


class UdfContext(__pyarrow_lib._Weakrefable):
    """
    UdfContext()
    
        Per-invocation function context/state.
    
        This object will always be the first argument to a user-defined
        function. It should not be used outside of a call to the function.
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ UdfContext.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ UdfContext.__setstate_cython__(self, __pyx_state) """
        pass

    batch_length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The common length of all input arguments (int).

        In the case that all arguments are scalars, this value
        is used to pass the "actual length" of the arguments,
        e.g. because the scalar values are encoding a column
        with a constant value.
        """

    memory_pool = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        A memory pool for allocations (:class:`MemoryPool`).

        This is the memory pool supplied by the user when they invoked
        the function and it should be used in any calls to arrow that the
        UDF makes if that call accepts a memory_pool.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001FEE411BC60>'


