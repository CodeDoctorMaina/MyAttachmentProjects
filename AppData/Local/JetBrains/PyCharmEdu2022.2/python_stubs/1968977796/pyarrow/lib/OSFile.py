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

class OSFile(NativeFile):
    """
    A stream backed by a regular file descriptor.
    
        Examples
        --------
        Create a new file to write to:
    
        >>> import pyarrow as pa
        >>> with pa.OSFile('example_osfile.arrow', mode='w') as f:
        ...     f.writable()
        ...     f.write(b'OSFile')
        ...     f.seekable()
        ...
        True
        6
        False
    
        Open the file to read:
    
        >>> with pa.OSFile('example_osfile.arrow', mode='r') as f:
        ...     f.mode
        ...     f.read()
        ...
        'rb'
        b'OSFile'
    
        Open the file to append:
    
        >>> with pa.OSFile('example_osfile.arrow', mode='ab') as f:
        ...     f.mode
        ...     f.write(b' is super!')
        ...
        'ab'
        10
        >>> with pa.OSFile('example_osfile.arrow') as f:
        ...     f.read()
        ...
        b'OSFile is super!'
    
        Inspect created OSFile:
    
        >>> pa.OSFile('example_osfile.arrow')
        <pyarrow.OSFile closed=False own_file=False is_seekable=True is_writable=False is_readable=True>
    """
    def fileno(self): # real signature unknown; restored from __doc__
        """ OSFile.fileno(self) """
        pass

    def __init__(self, example_osfile_arrow, mode='w'): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ OSFile.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ OSFile.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000029E047035A0>'


