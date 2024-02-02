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


from ._DictionaryEncodeOptions import _DictionaryEncodeOptions

class DictionaryEncodeOptions(_DictionaryEncodeOptions):
    """
    Options for dictionary encoding.
    
        Parameters
        ----------
        null_encoding : str, default "mask"
            How to encode nulls in the input.
            Accepted values are "mask" (null inputs emit a null in the indices
            array), "encode" (null inputs emit a non-null index pointing to
            a null value in the dictionary array).
    """
    def __init__(self, null_encoding=None): # real signature unknown; restored from __doc__
        """ DictionaryEncodeOptions.__init__(self, null_encoding=u'mask') """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._compute\', \'__doc__\': \'\\n    Options for dictionary encoding.\\n\\n    Parameters\\n    ----------\\n    null_encoding : str, default "mask"\\n        How to encode nulls in the input.\\n        Accepted values are "mask" (null inputs emit a null in the indices\\n        array), "encode" (null inputs emit a non-null index pointing to\\n        a null value in the dictionary array).\\n    \', \'__init__\': <cyfunction DictionaryEncodeOptions.__init__ at 0x000001FEE4164930>, \'__dict__\': <attribute \'__dict__\' of \'DictionaryEncodeOptions\' objects>})'


