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


from ._SortOptions import _SortOptions

class SortOptions(_SortOptions):
    """
    Options for the `sort_indices` function.
    
        Parameters
        ----------
        sort_keys : sequence of (name, order) tuples
            Names of field/column keys to sort the input on,
            along with the order each field/column is sorted in.
            Accepted values for `order` are "ascending", "descending".
            The field name can be a string column name or expression.
        null_placement : str, default "at_end"
            Where nulls in input should be sorted, only applying to
            columns/fields mentioned in `sort_keys`.
            Accepted values are "at_start", "at_end".
    """
    def __init__(self, sort_keys=(), *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ SortOptions.__init__(self, sort_keys=(), *, null_placement=u'at_end') """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._compute\', \'__doc__\': \'\\n    Options for the `sort_indices` function.\\n\\n    Parameters\\n    ----------\\n    sort_keys : sequence of (name, order) tuples\\n        Names of field/column keys to sort the input on,\\n        along with the order each field/column is sorted in.\\n        Accepted values for `order` are "ascending", "descending".\\n        The field name can be a string column name or expression.\\n    null_placement : str, default "at_end"\\n        Where nulls in input should be sorted, only applying to\\n        columns/fields mentioned in `sort_keys`.\\n        Accepted values are "at_start", "at_end".\\n    \', \'__init__\': <cyfunction SortOptions.__init__ at 0x000001FEE416CE10>, \'__dict__\': <attribute \'__dict__\' of \'SortOptions\' objects>})'


