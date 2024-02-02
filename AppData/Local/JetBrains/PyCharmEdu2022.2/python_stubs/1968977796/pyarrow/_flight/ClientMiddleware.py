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


class ClientMiddleware(__pyarrow_lib._Weakrefable):
    """
    Client-side middleware for a call, instantiated per RPC.
    
        Methods here should be fast and must be infallible: they should
        not raise exceptions or stall indefinitely.
    """
    def call_completed(self, exception): # real signature unknown; restored from __doc__
        """
        ClientMiddleware.call_completed(self, exception)
        A callback when the call finishes.
        
                The default implementation does nothing.
        
                Parameters
                ----------
                exception : ArrowException
                    If the call errored, this is the equivalent
                    exception. Will be None if the call succeeded.
        """
        pass

    def received_headers(self, headers): # real signature unknown; restored from __doc__
        """
        ClientMiddleware.received_headers(self, headers)
        A callback when headers are received.
        
                The default implementation does nothing.
        
                Parameters
                ----------
                headers : dict
                    A dictionary of headers from the server. Keys are strings
                    and values are lists of strings (for text headers) or
                    bytes (for binary headers).
        """
        pass

    def sending_headers(self): # real signature unknown; restored from __doc__
        """
        ClientMiddleware.sending_headers(self)
        A callback before headers are sent.
        
                Returns
                -------
                headers : dict
                    A dictionary of header values to add to the request, or
                    None if no headers are to be added. The dictionary should
                    have string keys and string or list-of-string values.
        
                    Bytes values are allowed, but the underlying transport may
                    not support them or may restrict them. For gRPC, binary
                    values are only allowed on headers ending in "-bin".
        
                    Header names must be lowercase ASCII.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ClientMiddleware.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ClientMiddleware.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000262C58CF690>'


