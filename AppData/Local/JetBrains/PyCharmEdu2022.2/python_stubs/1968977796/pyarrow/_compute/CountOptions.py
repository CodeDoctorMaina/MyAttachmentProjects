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


from ._CountOptions import _CountOptions

class CountOptions(_CountOptions):
    """
    Options for the `count` function.
    
        Parameters
        ----------
        mode : str, default "only_valid"
            Which values to count in the input.
            Accepted values are "only_valid", "only_null", "all".
    """
    def __init__(self, mode=None): # real signature unknown; restored from __doc__
        """ CountOptions.__init__(self, mode=u'only_valid') """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._compute\', \'__doc__\': \'\\n    Options for the `count` function.\\n\\n    Parameters\\n    ----------\\n    mode : str, default "only_valid"\\n        Which values to count in the input.\\n        Accepted values are "only_valid", "only_null", "all".\\n    \', \'__init__\': <cyfunction CountOptions.__init__ at 0x000001FEE4164E10>, \'__dict__\': <attribute \'__dict__\' of \'CountOptions\' objects>})'


