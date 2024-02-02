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


from ._MapLookupOptions import _MapLookupOptions

class MapLookupOptions(_MapLookupOptions):
    """
    Options for the `map_lookup` function.
    
        Parameters
        ----------
        query_key : Scalar or Object can be converted to Scalar
            The key to search for.
        occurrence : str
            The occurrence(s) to return from the Map
            Accepted values are "first", "last", or "all".
    """
    def __init__(self, query_key, occurrence): # real signature unknown; restored from __doc__
        """ MapLookupOptions.__init__(self, query_key, occurrence) """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._compute\', \'__doc__\': \'\\n    Options for the `map_lookup` function.\\n\\n    Parameters\\n    ----------\\n    query_key : Scalar or Object can be converted to Scalar\\n        The key to search for.\\n    occurrence : str\\n        The occurrence(s) to return from the Map\\n        Accepted values are "first", "last", or "all".\\n    \', \'__init__\': <cyfunction MapLookupOptions.__init__ at 0x000001FEE416C040>, \'__dict__\': <attribute \'__dict__\' of \'MapLookupOptions\' objects>})'


