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

class MemoryMappedFile(NativeFile):
    """
    A stream that represents a memory-mapped file.
    
        Supports 'r', 'r+', 'w' modes.
    
        Examples
        --------
        Create a new file with memory map:
    
        >>> import pyarrow as pa
        >>> mmap = pa.create_memory_map('example_mmap.dat', 10)
        >>> mmap
        <pyarrow.MemoryMappedFile closed=False own_file=False is_seekable=True is_writable=True is_readable=True>
        >>> mmap.close()
    
        Open an existing file with memory map:
    
        >>> with pa.memory_map('example_mmap.dat') as mmap:
        ...     mmap
        ...
        <pyarrow.MemoryMappedFile closed=False own_file=False is_seekable=True is_writable=False is_readable=True>
    """
    def create(self, path, size): # real signature unknown; restored from __doc__
        """
        MemoryMappedFile.create(path, size)
        
                Create a MemoryMappedFile
        
                Parameters
                ----------
                path : str
                    Where to create the file.
                size : int
                    Size of the memory mapped file.
        """
        pass

    def fileno(self): # real signature unknown; restored from __doc__
        """ MemoryMappedFile.fileno(self) """
        pass

    def resize(self, new_size): # real signature unknown; restored from __doc__
        """
        MemoryMappedFile.resize(self, new_size)
        
                Resize the map and underlying file.
        
                Parameters
                ----------
                new_size : new size in bytes
        """
        pass

    def _open(self, path, mode=None): # real signature unknown; restored from __doc__
        """ MemoryMappedFile._open(self, path, mode=u'r') """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ MemoryMappedFile.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ MemoryMappedFile.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000029E04703540>'


