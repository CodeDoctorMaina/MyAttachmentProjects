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


class ClientMiddlewareFactory(__pyarrow_lib._Weakrefable):
    """
    A factory for new middleware instances.
    
        All middleware methods will be called from the same thread as the
        RPC method implementation. That is, thread-locals set in the
        client are accessible from the middleware itself.
    """
    def start_call(self, info): # real signature unknown; restored from __doc__
        """
        ClientMiddlewareFactory.start_call(self, info)
        Called at the start of an RPC.
        
                This must be thread-safe and must not raise exceptions.
        
                Parameters
                ----------
                info : CallInfo
                    Information about the call.
        
                Returns
                -------
                instance : ClientMiddleware
                    An instance of ClientMiddleware (the instance to use for
                    the call), or None if this call is not intercepted.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ClientMiddlewareFactory.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ClientMiddlewareFactory.__setstate_cython__(self, __pyx_state) """
        pass


