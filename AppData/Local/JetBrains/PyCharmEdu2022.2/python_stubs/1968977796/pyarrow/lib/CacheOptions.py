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

class CacheOptions(_Weakrefable):
    """
    CacheOptions(hole_size_limit=None, *, range_size_limit=None, lazy=None, prefetch_limit=None)
    
        Cache options for a pre-buffered fragment scan.
    
        Parameters
        ----------
        hole_size_limit : int, default 8KiB
            The maximum distance in bytes between two consecutive ranges; beyond 
            this value, ranges are not combined.
        range_size_limit : int, default 32MiB
            The maximum size in bytes of a combined range; if combining two 
            consecutive ranges would produce a range of a size greater than this, 
            they are not combined
        lazy : bool, default True
            lazy = false: request all byte ranges when PreBuffer or WillNeed is called.
            lazy = True, prefetch_limit = 0: request merged byte ranges only after the reader 
            needs them. 
            lazy = True, prefetch_limit = k: prefetch up to k merged byte ranges ahead of the 
            range that is currently being read.
        prefetch_limit : int, default 0
            The maximum number of ranges to be prefetched. This is only used for 
            lazy cache to asynchronously read some ranges after reading the target 
            range.
    """
    def from_network_metrics(self, time_to_first_byte_millis, transfer_bandwidth_mib_per_sec, ideal_bandwidth_utilization_frac=0.9, max_ideal_request_size_mib=64): # real signature unknown; restored from __doc__
        """
        CacheOptions.from_network_metrics(time_to_first_byte_millis, transfer_bandwidth_mib_per_sec, ideal_bandwidth_utilization_frac=0.9, max_ideal_request_size_mib=64)
        
                Create suiteable CacheOptions based on provided network metrics.
        
                Typically this will be used with object storage solutions like Amazon S3, 
                Google Cloud Storage and Azure Blob Storage.
        
                Parameters
                ----------
                time_to_first_byte_millis : int
                    Seek-time or Time-To-First-Byte (TTFB) in milliseconds, also called call 
                    setup latency of a new read request. The value is a positive integer. 
                transfer_bandwidth_mib_per_sec : int
                    Data transfer Bandwidth (BW) in MiB/sec (per connection). The value is a positive 
                    integer.
                ideal_bandwidth_utilization_frac : int, default 0.9
                    Transfer bandwidth utilization fraction (per connection) to maximize the net 
                    data load. The value is a positive float less than 1.
                max_ideal_request_size_mib : int, default 64
                    The maximum single data request size (in MiB) to maximize the net data load.
        
                Returns
                -------
                CacheOptions
        """
        pass

    def _reconstruct(self, kwargs): # real signature unknown; restored from __doc__
        """ CacheOptions._reconstruct(kwargs) """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, hole_size_limit=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ CacheOptions.__reduce__(self) """
        pass

    hole_size_limit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lazy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prefetch_limit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    range_size_limit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000029E04689F90>'


