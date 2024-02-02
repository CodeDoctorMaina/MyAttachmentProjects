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


from .NativeFile import NativeFile

class FixedSizeBufferWriter(NativeFile):
    """
    A stream writing to a Arrow buffer.
    
        Examples
        --------
        Create a stream to write to ``pyarrow.Buffer``:
    
        >>> import pyarrow as pa
        >>> buf = pa.allocate_buffer(5)
        >>> with pa.output_stream(buf) as stream:
        ...     stream.write(b'abcde')
        ...     stream
        ...
        5
        <pyarrow.FixedSizeBufferWriter closed=False own_file=False is_seekable=False is_writable=True is_readable=False>
    
        Inspect the buffer:
    
        >>> buf.to_pybytes()
        b'abcde'
        >>> buf
        <pyarrow.Buffer address=... size=5 is_cpu=True is_mutable=True>
    """
    def set_memcopy_blocksize(self, int64_t_blocksize): # real signature unknown; restored from __doc__
        """
        FixedSizeBufferWriter.set_memcopy_blocksize(self, int64_t blocksize)
        
                Parameters
                ----------
                blocksize : int64
        """
        pass

    def set_memcopy_threads(self, int_num_threads): # real signature unknown; restored from __doc__
        """
        FixedSizeBufferWriter.set_memcopy_threads(self, int num_threads)
        
                Parameters
                ----------
                num_threads : int
        """
        pass

    def set_memcopy_threshold(self, int64_t_threshold): # real signature unknown; restored from __doc__
        """
        FixedSizeBufferWriter.set_memcopy_threshold(self, int64_t threshold)
        
                Parameters
                ----------
                threshold : int64
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ FixedSizeBufferWriter.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ FixedSizeBufferWriter.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000029E04703600>'


