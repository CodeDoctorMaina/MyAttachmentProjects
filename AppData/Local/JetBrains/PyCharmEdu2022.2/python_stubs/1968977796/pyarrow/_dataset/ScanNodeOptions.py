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


from ._ScanNodeOptions import _ScanNodeOptions

class ScanNodeOptions(_ScanNodeOptions):
    """
    A Source node which yields batches from a Dataset scan.
    
        This is the option class for the "scan" node factory.
    
        This node is capable of applying pushdown projections or filters
        to the file readers which reduce the amount of data that needs to
        be read (if supported by the file format). But note that this does not
        construct associated filter or project nodes to perform the final
        filtering or projection. Rather, you may supply the same filter
        expression or projection to the scan node that you also supply
        to the filter or project node.
    
        Yielded batches will be augmented with fragment/batch indices to
        enable stable ordering for simple ExecPlans.
    
        Parameters
        ----------
        dataset : pyarrow.dataset.Dataset
            The table which acts as the data source.
        **kwargs : dict, optional
            Scan options. See `Scanner.from_dataset` for possible arguments.
    """
    def __init__(self, Dataset_dataset, **kwargs): # real signature unknown; restored from __doc__
        """ ScanNodeOptions.__init__(self, Dataset dataset, **kwargs) """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._dataset\', \'__doc__\': \'\\n    A Source node which yields batches from a Dataset scan.\\n\\n    This is the option class for the "scan" node factory.\\n\\n    This node is capable of applying pushdown projections or filters\\n    to the file readers which reduce the amount of data that needs to\\n    be read (if supported by the file format). But note that this does not\\n    construct associated filter or project nodes to perform the final\\n    filtering or projection. Rather, you may supply the same filter\\n    expression or projection to the scan node that you also supply\\n    to the filter or project node.\\n\\n    Yielded batches will be augmented with fragment/batch indices to\\n    enable stable ordering for simple ExecPlans.\\n\\n    Parameters\\n    ----------\\n    dataset : pyarrow.dataset.Dataset\\n        The table which acts as the data source.\\n    **kwargs : dict, optional\\n        Scan options. See `Scanner.from_dataset` for possible arguments.\\n    \', \'__init__\': <cyfunction ScanNodeOptions.__init__ at 0x000001D1AA43AC70>, \'__dict__\': <attribute \'__dict__\' of \'ScanNodeOptions\' objects>})'


