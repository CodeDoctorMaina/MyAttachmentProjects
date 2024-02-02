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


from ._PartitionNthOptions import _PartitionNthOptions

class PartitionNthOptions(_PartitionNthOptions):
    """
    Options for the `partition_nth_indices` function.
    
        Parameters
        ----------
        pivot : int
            Index into the equivalent sorted array of the pivot element.
        null_placement : str, default "at_end"
            Where nulls in the input should be partitioned.
            Accepted values are "at_start", "at_end".
    """
    def __init__(self, pivot, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ PartitionNthOptions.__init__(self, pivot, *, null_placement=u'at_end') """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._compute\', \'__doc__\': \'\\n    Options for the `partition_nth_indices` function.\\n\\n    Parameters\\n    ----------\\n    pivot : int\\n        Index into the equivalent sorted array of the pivot element.\\n    null_placement : str, default "at_end"\\n        Where nulls in the input should be partitioned.\\n        Accepted values are "at_start", "at_end".\\n    \', \'__init__\': <cyfunction PartitionNthOptions.__init__ at 0x000001FEE416CA00>, \'__dict__\': <attribute \'__dict__\' of \'PartitionNthOptions\' objects>})'


