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

class AsyncioCall(object):
    """ State for an async RPC using asyncio. """
    def as_awaitable(self): # real signature unknown; restored from __doc__
        """ AsyncioCall.as_awaitable(self) -> object """
        return object()

    def wakeup(self, result_or_exception): # real signature unknown; restored from __doc__
        """ AsyncioCall.wakeup(self, result_or_exception) -> None """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        """ AsyncioCall.__init__(self) -> None """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow._flight', '__doc__': 'State for an async RPC using asyncio.', '__init__': <cyfunction AsyncioCall.__init__ at 0x00000262BEF562B0>, 'as_awaitable': <cyfunction AsyncioCall.as_awaitable at 0x00000262C58ACAD0>, 'wakeup': <cyfunction AsyncioCall.wakeup at 0x00000262C58ACA00>, '__dict__': <attribute '__dict__' of 'AsyncioCall' objects>, '__weakref__': <attribute '__weakref__' of 'AsyncioCall' objects>})"


