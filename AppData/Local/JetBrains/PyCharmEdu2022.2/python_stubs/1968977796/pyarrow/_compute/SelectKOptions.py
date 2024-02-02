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


from ._SelectKOptions import _SelectKOptions

class SelectKOptions(_SelectKOptions):
    """
    Options for top/bottom k-selection.
    
        Parameters
        ----------
        k : int
            Number of leading values to select in sorted order
            (i.e. the largest values if sort order is "descending",
            the smallest otherwise).
        sort_keys : sequence of (name, order) tuples
            Names of field/column keys to sort the input on,
            along with the order each field/column is sorted in.
            Accepted values for `order` are "ascending", "descending".
            The field name can be a string column name or expression.
    """
    def __init__(self, k, sort_keys): # real signature unknown; restored from __doc__
        """ SelectKOptions.__init__(self, k, sort_keys) """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._compute\', \'__doc__\': \'\\n    Options for top/bottom k-selection.\\n\\n    Parameters\\n    ----------\\n    k : int\\n        Number of leading values to select in sorted order\\n        (i.e. the largest values if sort order is "descending",\\n        the smallest otherwise).\\n    sort_keys : sequence of (name, order) tuples\\n        Names of field/column keys to sort the input on,\\n        along with the order each field/column is sorted in.\\n        Accepted values for `order` are "ascending", "descending".\\n        The field name can be a string column name or expression.\\n    \', \'__init__\': <cyfunction SelectKOptions.__init__ at 0x000001FEE416CEE0>, \'__dict__\': <attribute \'__dict__\' of \'SelectKOptions\' objects>})'


