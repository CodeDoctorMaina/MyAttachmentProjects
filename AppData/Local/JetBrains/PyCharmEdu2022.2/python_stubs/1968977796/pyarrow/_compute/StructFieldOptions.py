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


from ._StructFieldOptions import _StructFieldOptions

class StructFieldOptions(_StructFieldOptions):
    """
    Options for the `struct_field` function.
    
        Parameters
        ----------
        indices : List[str], List[bytes], List[int], Expression, bytes, str, or int
            List of indices for chained field lookup, for example `[4, 1]`
            will look up the second nested field in the fifth outer field.
    """
    def __init__(self, indices): # real signature unknown; restored from __doc__
        """ StructFieldOptions.__init__(self, indices) """
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow._compute', '__doc__': '\\n    Options for the `struct_field` function.\\n\\n    Parameters\\n    ----------\\n    indices : List[str], List[bytes], List[int], Expression, bytes, str, or int\\n        List of indices for chained field lookup, for example `[4, 1]`\\n        will look up the second nested field in the fifth outer field.\\n    ', '__init__': <cyfunction StructFieldOptions.__init__ at 0x000001FEE4164C70>, '__dict__': <attribute '__dict__' of 'StructFieldOptions' objects>})"


