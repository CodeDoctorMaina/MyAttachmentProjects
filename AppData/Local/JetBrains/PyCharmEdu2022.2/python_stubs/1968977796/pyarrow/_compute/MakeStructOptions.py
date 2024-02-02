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


from ._MakeStructOptions import _MakeStructOptions

class MakeStructOptions(_MakeStructOptions):
    """
    Options for the `make_struct` function.
    
        Parameters
        ----------
        field_names : sequence of str
            Names of the struct fields to create.
        field_nullability : sequence of bool, optional
            Nullability information for each struct field.
            If omitted, all fields are nullable.
        field_metadata : sequence of KeyValueMetadata, optional
            Metadata for each struct field.
    """
    def __init__(self, field_names=(), *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ MakeStructOptions.__init__(self, field_names=(), *, field_nullability=None, field_metadata=None) """
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow._compute', '__doc__': '\\n    Options for the `make_struct` function.\\n\\n    Parameters\\n    ----------\\n    field_names : sequence of str\\n        Names of the struct fields to create.\\n    field_nullability : sequence of bool, optional\\n        Nullability information for each struct field.\\n        If omitted, all fields are nullable.\\n    field_metadata : sequence of KeyValueMetadata, optional\\n        Metadata for each struct field.\\n    ', '__init__': <cyfunction MakeStructOptions.__init__ at 0x000001FEE4164BA0>, '__dict__': <attribute '__dict__' of 'MakeStructOptions' objects>})"


