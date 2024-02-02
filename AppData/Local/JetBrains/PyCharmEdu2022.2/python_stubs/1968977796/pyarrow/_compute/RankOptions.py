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


from ._RankOptions import _RankOptions

class RankOptions(_RankOptions):
    """
    Options for the `rank` function.
    
        Parameters
        ----------
        sort_keys : sequence of (name, order) tuples or str, default "ascending"
            Names of field/column keys to sort the input on,
            along with the order each field/column is sorted in.
            Accepted values for `order` are "ascending", "descending".
            The field name can be a string column name or expression.
            Alternatively, one can simply pass "ascending" or "descending" as a string
            if the input is array-like.
        null_placement : str, default "at_end"
            Where nulls in input should be sorted.
            Accepted values are "at_start", "at_end".
        tiebreaker : str, default "first"
            Configure how ties between equal values are handled.
            Accepted values are:
    
            - "min": Ties get the smallest possible rank in sorted order.
            - "max": Ties get the largest possible rank in sorted order.
            - "first": Ranks are assigned in order of when ties appear in the
                       input. This ensures the ranks are a stable permutation
                       of the input.
            - "dense": The ranks span a dense [1, M] interval where M is the
                       number of distinct values in the input.
    """
    def __init__(self, sort_keys=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ RankOptions.__init__(self, sort_keys=u'ascending', *, null_placement=u'at_end', tiebreaker=u'first') """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._compute\', \'__doc__\': \'\\n    Options for the `rank` function.\\n\\n    Parameters\\n    ----------\\n    sort_keys : sequence of (name, order) tuples or str, default "ascending"\\n        Names of field/column keys to sort the input on,\\n        along with the order each field/column is sorted in.\\n        Accepted values for `order` are "ascending", "descending".\\n        The field name can be a string column name or expression.\\n        Alternatively, one can simply pass "ascending" or "descending" as a string\\n        if the input is array-like.\\n    null_placement : str, default "at_end"\\n        Where nulls in input should be sorted.\\n        Accepted values are "at_start", "at_end".\\n    tiebreaker : str, default "first"\\n        Configure how ties between equal values are handled.\\n        Accepted values are:\\n\\n        - "min": Ties get the smallest possible rank in sorted order.\\n        - "max": Ties get the largest possible rank in sorted order.\\n        - "first": Ranks are assigned in order of when ties appear in the\\n                   input. This ensures the ranks are a stable permutation\\n                   of the input.\\n        - "dense": The ranks span a dense [1, M] interval where M is the\\n                   number of distinct values in the input.\\n    \', \'__init__\': <cyfunction RankOptions.__init__ at 0x000001FEE4172380>, \'__dict__\': <attribute \'__dict__\' of \'RankOptions\' objects>})'


