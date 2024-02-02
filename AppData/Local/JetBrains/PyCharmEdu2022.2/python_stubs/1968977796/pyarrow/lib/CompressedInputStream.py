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

class CompressedInputStream(NativeFile):
    """
    CompressedInputStream(stream, unicode compression)
    
        An input stream wrapper which decompresses data on the fly.
    
        Parameters
        ----------
        stream : string, path, pyarrow.NativeFile, or file-like object
            Input stream object to wrap with the compression.
        compression : str
            The compression type ("bz2", "brotli", "gzip", "lz4" or "zstd").
    
        Examples
        --------
        Create an output stream wich compresses the data:
    
        >>> import pyarrow as pa
        >>> data = b"Compressed stream"
        >>> raw = pa.BufferOutputStream()
        >>> with pa.CompressedOutputStream(raw, "gzip") as compressed:
        ...     compressed.write(data)
        ...
        17
    
        Create an input stream with decompression referencing the
        buffer with compressed data:
    
        >>> cdata = raw.getvalue()
        >>> with pa.input_stream(cdata, compression="gzip") as compressed:
        ...     compressed.read()
        ...
        b'Compressed stream'
    
        which actually translates to the use of ``BufferReader``and
        ``CompressedInputStream``:
    
        >>> raw = pa.BufferReader(cdata)
        >>> with pa.CompressedInputStream(raw, "gzip") as compressed:
        ...     compressed.read()
        ...
        b'Compressed stream'
    """
    def __init__(self, stream, unicode_compression): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ CompressedInputStream.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ CompressedInputStream.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000029E04689E70>'


