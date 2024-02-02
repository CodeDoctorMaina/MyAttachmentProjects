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


class ActionType(__importlib__bootstrap._ActionType):
    """ A type of action that is executable on a Flight service. """
    def make_action(self, buf): # real signature unknown; restored from __doc__
        """
        ActionType.make_action(self, buf)
        Create an Action with this type.
        
                Parameters
                ----------
                buf : obj
                    An Arrow buffer or Python bytes or bytes-like object.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow._flight', '__doc__': 'A type of action that is executable on a Flight service.', 'make_action': <cyfunction ActionType.make_action at 0x00000262BEF56450>, '__dict__': <attribute '__dict__' of 'ActionType' objects>})"


