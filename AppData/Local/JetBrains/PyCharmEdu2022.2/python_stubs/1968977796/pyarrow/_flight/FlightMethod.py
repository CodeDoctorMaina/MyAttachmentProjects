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


class FlightMethod(__enum.Enum):
    """ The implemented methods in Flight. """
    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    DO_ACTION = None # (!) real value is '<FlightMethod.DO_ACTION: 7>'
    DO_EXCHANGE = None # (!) real value is '<FlightMethod.DO_EXCHANGE: 9>'
    DO_GET = None # (!) real value is '<FlightMethod.DO_GET: 5>'
    DO_PUT = None # (!) real value is '<FlightMethod.DO_PUT: 6>'
    GET_FLIGHT_INFO = None # (!) real value is '<FlightMethod.GET_FLIGHT_INFO: 3>'
    GET_SCHEMA = None # (!) real value is '<FlightMethod.GET_SCHEMA: 4>'
    HANDSHAKE = None # (!) real value is '<FlightMethod.HANDSHAKE: 1>'
    INVALID = None # (!) real value is '<FlightMethod.INVALID: 0>'
    LIST_ACTIONS = None # (!) real value is '<FlightMethod.LIST_ACTIONS: 8>'
    LIST_FLIGHTS = None # (!) real value is '<FlightMethod.LIST_FLIGHTS: 2>'
    _member_map_ = {
        'DO_ACTION': None, # (!) real value is '<FlightMethod.DO_ACTION: 7>'
        'DO_EXCHANGE': None, # (!) real value is '<FlightMethod.DO_EXCHANGE: 9>'
        'DO_GET': None, # (!) real value is '<FlightMethod.DO_GET: 5>'
        'DO_PUT': None, # (!) real value is '<FlightMethod.DO_PUT: 6>'
        'GET_FLIGHT_INFO': None, # (!) real value is '<FlightMethod.GET_FLIGHT_INFO: 3>'
        'GET_SCHEMA': None, # (!) real value is '<FlightMethod.GET_SCHEMA: 4>'
        'HANDSHAKE': None, # (!) real value is '<FlightMethod.HANDSHAKE: 1>'
        'INVALID': None, # (!) real value is '<FlightMethod.INVALID: 0>'
        'LIST_ACTIONS': None, # (!) real value is '<FlightMethod.LIST_ACTIONS: 8>'
        'LIST_FLIGHTS': None, # (!) real value is '<FlightMethod.LIST_FLIGHTS: 2>'
    }
    _member_names_ = [
        'INVALID',
        'HANDSHAKE',
        'LIST_FLIGHTS',
        'GET_FLIGHT_INFO',
        'GET_SCHEMA',
        'DO_GET',
        'DO_PUT',
        'DO_ACTION',
        'LIST_ACTIONS',
        'DO_EXCHANGE',
    ]
    _member_type_ = object
    _value2member_map_ = {
        0: None, # (!) real value is '<FlightMethod.INVALID: 0>'
        1: None, # (!) real value is '<FlightMethod.HANDSHAKE: 1>'
        2: None, # (!) real value is '<FlightMethod.LIST_FLIGHTS: 2>'
        3: None, # (!) real value is '<FlightMethod.GET_FLIGHT_INFO: 3>'
        4: None, # (!) real value is '<FlightMethod.GET_SCHEMA: 4>'
        5: None, # (!) real value is '<FlightMethod.DO_GET: 5>'
        6: None, # (!) real value is '<FlightMethod.DO_PUT: 6>'
        7: None, # (!) real value is '<FlightMethod.DO_ACTION: 7>'
        8: None, # (!) real value is '<FlightMethod.LIST_ACTIONS: 8>'
        9: None, # (!) real value is '<FlightMethod.DO_EXCHANGE: 9>'
    }


