# encoding: utf-8
# module pyarrow._compute
# from C:\Users\hp\PycharmProjects\Text_Summarizer\venv\lib\site-packages\pyarrow\_compute.cp38-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import pyarrow.lib as lib # C:\Users\hp\PycharmProjects\Text_Summarizer\venv\lib\site-packages\pyarrow\lib.cp38-win_amd64.pyd
import inspect as inspect # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\inspect.py
import numpy as np # C:\Users\hp\PycharmProjects\Text_Summarizer\venv\lib\site-packages\numpy\__init__.py
import warnings as warnings # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\warnings.py
from pyarrow.lib import ArrowInvalid, frombytes, tobytes

import pyarrow.lib as __pyarrow_lib


from ._CumulativeOptions import _CumulativeOptions

class CumulativeSumOptions(_CumulativeOptions):
    """
    Options for `cumulative_sum` function.
    
        Parameters
        ----------
        start : Scalar, default None
            Starting value for sum computation
        skip_nulls : bool, default False
            When false, the first encountered null is propagated.
    """
    def __init__(self, start=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ CumulativeSumOptions.__init__(self, start=None, *, skip_nulls=False) """
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow._compute', '__doc__': '\\n    Options for `cumulative_sum` function.\\n\\n    Parameters\\n    ----------\\n    start : Scalar, default None\\n        Starting value for sum computation\\n    skip_nulls : bool, default False\\n        When false, the first encountered null is propagated.\\n    ', '__init__': <cyfunction CumulativeSumOptions.__init__ at 0x000001FEE416CBA0>, '__dict__': <attribute '__dict__' of 'CumulativeSumOptions' objects>})"


