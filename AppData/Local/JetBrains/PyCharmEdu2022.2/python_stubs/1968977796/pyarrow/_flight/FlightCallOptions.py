# encoding: utf-8
# module pyarrow._flight
# from C:\Users\hp\PycharmProjects\Text_Summarizer\venv\lib\site-packages\pyarrow\_flight.cp38-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import collections as collections # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\collections\__init__.py
import enum as enum # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\enum.py
import re as re # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\re.py
import time as time # <module 'time' (built-in)>
import warnings as warnings # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\warnings.py
import weakref as weakref # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\weakref.py
import pyarrow.lib as lib # C:\Users\hp\PycharmProjects\Text_Summarizer\venv\lib\site-packages\pyarrow\lib.cp38-win_amd64.pyd
from pyarrow.lib import (ArrowCancelled, ArrowException, ArrowInvalid, 
    SignalStopHandler, _ReadPandasMixin, as_buffer, frombytes, tobytes)

import enum as __enum
import importlib._bootstrap as __importlib__bootstrap
import pyarrow.lib as __pyarrow_lib


class FlightCallOptions(__pyarrow_lib._Weakrefable):
    """
    FlightCallOptions(timeout=None, write_options=None, headers=None, IpcReadOptions read_options=None)
    RPC-layer options for a Flight call.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Create call options.
        
                Parameters
                ----------
                timeout : float, None
                    A timeout for the call, in seconds. None means that the
                    timeout defaults to an implementation-specific value.
                write_options : pyarrow.ipc.IpcWriteOptions, optional
                    IPC write options. The default options can be controlled
                    by environment variables (see pyarrow.ipc).
                headers : List[Tuple[str, str]], optional
                    A list of arbitrary headers as key, value tuples
                read_options : pyarrow.ipc.IpcReadOptions, optional
                    Serialization options for reading IPC format.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ FlightCallOptions.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ FlightCallOptions.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000262C58BED20>'


