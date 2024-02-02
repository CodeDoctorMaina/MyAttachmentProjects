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


from .tuple import tuple

class _ActionType(tuple):
    """ _ActionType(type, description) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new dict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new _ActionType object from a sequence or iterable """
        pass

    def _replace(self, **kwds): # reliably restored by inspect
        """ Return a new _ActionType object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, type, description): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, type, description): # reliably restored by inspect
        """ Create new instance of _ActionType(type, description) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    description = None # (!) real value is '<_collections._tuplegetter object at 0x00000262C58DD130>'
    type = None # (!) real value is '<_collections._tuplegetter object at 0x00000262C58DD1C0>'
    _fields = (
        'type',
        'description',
    )
    _fields_defaults = {}
    _field_defaults = {}
    __slots__ = ()


