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


from ._StrptimeOptions import _StrptimeOptions

class StrptimeOptions(_StrptimeOptions):
    """
    Options for the `strptime` function.
    
        Parameters
        ----------
        format : str
            Pattern for parsing input strings as timestamps, such as "%Y/%m/%d".
            Note that the semantics of the format follow the C/C++ strptime, not the Python one.
            There are differences in behavior, for example how the "%y" placeholder
            handles years with less than four digits.
        unit : str
            Timestamp unit of the output.
            Accepted values are "s", "ms", "us", "ns".
        error_is_null : boolean, default False
            Return null on parsing errors if true or raise if false.
    """
    def __init__(self, format, unit, error_is_null=False): # real signature unknown; restored from __doc__
        """ StrptimeOptions.__init__(self, format, unit, error_is_null=False) """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._compute\', \'__doc__\': \'\\n    Options for the `strptime` function.\\n\\n    Parameters\\n    ----------\\n    format : str\\n        Pattern for parsing input strings as timestamps, such as "%Y/%m/%d".\\n        Note that the semantics of the format follow the C/C++ strptime, not the Python one.\\n        There are differences in behavior, for example how the "%y" placeholder\\n        handles years with less than four digits.\\n    unit : str\\n        Timestamp unit of the output.\\n        Accepted values are "s", "ms", "us", "ns".\\n    error_is_null : boolean, default False\\n        Return null on parsing errors if true or raise if false.\\n    \', \'__init__\': <cyfunction StrptimeOptions.__init__ at 0x000001FEE416C2B0>, \'__dict__\': <attribute \'__dict__\' of \'StrptimeOptions\' objects>})'


