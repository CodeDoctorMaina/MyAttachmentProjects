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


from ._RunEndEncodeOptions import _RunEndEncodeOptions

class RunEndEncodeOptions(_RunEndEncodeOptions):
    """
    Options for run-end encoding.
    
        Parameters
        ----------
        run_end_type : DataType, default pyarrow.int32()
            The data type of the run_ends array.
    
            Accepted values are pyarrow.{int16(), int32(), int64()}.
    """
    def __init__(self, run_end_type=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ RunEndEncodeOptions.__init__(self, run_end_type=lib.int32()) """
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow._compute', '__doc__': '\\n    Options for run-end encoding.\\n\\n    Parameters\\n    ----------\\n    run_end_type : DataType, default pyarrow.int32()\\n        The data type of the run_ends array.\\n\\n        Accepted values are pyarrow.{int16(), int32(), int64()}.\\n    ', '__init__': <cyfunction RunEndEncodeOptions.__init__ at 0x000001FEE4164A00>, '__dict__': <attribute '__dict__' of 'RunEndEncodeOptions' objects>})"


