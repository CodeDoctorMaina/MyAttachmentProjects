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

class CumulativeOptions(_CumulativeOptions):
    """
    Options for `cumulative_*` functions.
    
        - cumulative_sum
        - cumulative_sum_checked
        - cumulative_prod
        - cumulative_prod_checked
        - cumulative_max
        - cumulative_min
    
        Parameters
        ----------
        start : Scalar, default None
            Starting value for the cumulative operation. If none is given,
            a default value depending on the operation and input type is used.
        skip_nulls : bool, default False
            When false, the first encountered null is propagated.
    """
    def __init__(self, start=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ CumulativeOptions.__init__(self, start=None, *, skip_nulls=False) """
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow._compute', '__doc__': '\\n    Options for `cumulative_*` functions.\\n\\n    - cumulative_sum\\n    - cumulative_sum_checked\\n    - cumulative_prod\\n    - cumulative_prod_checked\\n    - cumulative_max\\n    - cumulative_min\\n\\n    Parameters\\n    ----------\\n    start : Scalar, default None\\n        Starting value for the cumulative operation. If none is given,\\n        a default value depending on the operation and input type is used.\\n    skip_nulls : bool, default False\\n        When false, the first encountered null is propagated.\\n    ', '__init__': <cyfunction CumulativeOptions.__init__ at 0x000001FEE416CAD0>, '__dict__': <attribute '__dict__' of 'CumulativeOptions' objects>})"


