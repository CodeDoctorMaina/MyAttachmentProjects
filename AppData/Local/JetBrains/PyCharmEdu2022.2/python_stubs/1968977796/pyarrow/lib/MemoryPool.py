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


from ._Weakrefable import _Weakrefable

class MemoryPool(_Weakrefable):
    """
    MemoryPool()
    
        Base class for memory allocation.
    
        Besides tracking its number of allocated bytes, a memory pool also
        takes care of the required 64-byte alignment for Arrow data.
    """
    def bytes_allocated(self): # real signature unknown; restored from __doc__
        """
        MemoryPool.bytes_allocated(self)
        
                Return the number of bytes that are currently allocated from this
                memory pool.
        """
        pass

    def max_memory(self): # real signature unknown; restored from __doc__
        """
        MemoryPool.max_memory(self)
        
                Return the peak memory allocation in this memory pool.
                This can be an approximate number in multi-threaded applications.
        
                None is returned if the pool implementation doesn't know how to
                compute this number.
        """
        pass

    def release_unused(self): # real signature unknown; restored from __doc__
        """
        MemoryPool.release_unused(self)
        
                Attempt to return to the OS any memory being held onto by the pool.
        
                This function should not be called except potentially for
                benchmarking or debugging as it could be expensive and detrimental to
                performance.
        
                This is best effort and may not have any effect on some memory pools
                or in some situations (e.g. fragmentation).
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ MemoryPool.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ MemoryPool.__setstate_cython__(self, __pyx_state) """
        pass

    backend_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The name of the backend used by this MemoryPool (e.g. "jemalloc").
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000029E0467A3F0>'


