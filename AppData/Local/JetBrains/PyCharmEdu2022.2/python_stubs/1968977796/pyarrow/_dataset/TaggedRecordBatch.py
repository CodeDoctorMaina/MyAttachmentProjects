# encoding: utf-8
# module pyarrow._dataset
# from C:\Users\hp\PycharmProjects\Text_Summarizer\venv\lib\site-packages\pyarrow\_dataset.cp38-win_amd64.pyd
# by generator 1.147
""" Dataset is currently unstable. APIs subject to change without notice. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import codecs as codecs # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\codecs.py
import collections as collections # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\collections\__init__.py
import pyarrow as pa # C:\Users\hp\PycharmProjects\Text_Summarizer\venv\lib\site-packages\pyarrow\__init__.py
from pyarrow.lib import ArrowTypeError, _pac, frombytes, tobytes

from pyarrow._compute import _forbid_instantiation

import importlib._bootstrap as __importlib__bootstrap
import pyarrow.lib as __pyarrow_lib
import pyarrow._acero as __pyarrow__acero


class TaggedRecordBatch(__importlib__bootstrap.TaggedRecordBatch):
    """
    A combination of a record batch and the fragment it came from.
    
        Parameters
        ----------
        record_batch : RecordBatch
            The record batch.
        fragment : Fragment
            Fragment of the record batch.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow._dataset', '__doc__': '\\n    A combination of a record batch and the fragment it came from.\\n\\n    Parameters\\n    ----------\\n    record_batch : RecordBatch\\n        The record batch.\\n    fragment : Fragment\\n        Fragment of the record batch.\\n    ', '__dict__': <attribute '__dict__' of 'TaggedRecordBatch' objects>})"


