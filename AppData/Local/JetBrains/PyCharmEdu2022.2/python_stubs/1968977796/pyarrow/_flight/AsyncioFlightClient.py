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


from .object import object

class AsyncioFlightClient(object):
    """
    AsyncioFlightClient(FlightClient client) -> None
    
        A FlightClient with an asyncio-based async interface.
    
        This interface is EXPERIMENTAL.
    """
    def get_flight_info(self, FlightDescriptor_descriptor, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ AsyncioFlightClient.get_flight_info(self, FlightDescriptor descriptor: FlightDescriptor, *, FlightCallOptions options: FlightCallOptions = None) """
        pass

    def __init__(self, FlightClient_client): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ AsyncioFlightClient.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ AsyncioFlightClient.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000262C58CF1E0>'


