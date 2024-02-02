# encoding: utf-8
# module pyarrow.lib
# from C:\Users\hp\PycharmProjects\Text_Summarizer\venv\lib\site-packages\pyarrow\lib.cp38-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import datetime as datetime # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\datetime.py
import decimal as _pydecimal # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\decimal.py
import numpy as np # C:\Users\hp\PycharmProjects\Text_Summarizer\venv\lib\site-packages\numpy\__init__.py
import os as os # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\os.py
import sys as sys # <module 'sys' (built-in)>
import pickle as pickle # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\pickle.py
import signal as signal # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\signal.py
import threading as threading # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\threading.py
import warnings as warnings # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\warnings.py
import atexit as atexit # <module 'atexit' (built-in)>
import re as re # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\re.py
import collections as collections # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\collections\__init__.py
import codecs as codecs # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\codecs.py
import time as time # <module 'time' (built-in)>
from _queue import QueueEmpty

import collections.abc as __collections_abc
import enum as __enum
import importlib._bootstrap as __importlib__bootstrap
import io as __io
import _io as ___io


from .ExtensionArray import ExtensionArray

class FixedShapeTensorArray(ExtensionArray):
    """
    Concrete class for fixed shape tensor extension arrays.
    
        Examples
        --------
        Define the extension type for tensor array
    
        >>> import pyarrow as pa
        >>> tensor_type = pa.fixed_shape_tensor(pa.int32(), [2, 2])
    
        Create an extension array
    
        >>> arr = [[1, 2, 3, 4], [10, 20, 30, 40], [100, 200, 300, 400]]
        >>> storage = pa.array(arr, pa.list_(pa.int32(), 4))
        >>> pa.ExtensionArray.from_storage(tensor_type, storage)
        <pyarrow.lib.FixedShapeTensorArray object at ...>
        [
          [
            1,
            2,
            3,
            4
          ],
          [
            10,
            20,
            30,
            40
          ],
          [
            100,
            200,
            300,
            400
          ]
        ]
    """
    def from_numpy_ndarray(self, obj): # real signature unknown; restored from __doc__
        """
        FixedShapeTensorArray.from_numpy_ndarray(obj)
        
                Convert numpy tensors (ndarrays) to a fixed shape tensor extension array.
                The first dimension of ndarray will become the length of the fixed
                shape tensor array.
        
                Numpy array needs to be C-contiguous in memory
                (``obj.flags["C_CONTIGUOUS"]==True``).
        
                Parameters
                ----------
                obj : numpy.ndarray
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import numpy as np
                >>> arr = np.array(
                ...         [[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]],
                ...         dtype=np.float32)
                >>> pa.FixedShapeTensorArray.from_numpy_ndarray(arr)
                <pyarrow.lib.FixedShapeTensorArray object at ...>
                [
                  [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                  ],
                  [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                  ]
                ]
        """
        pass

    def to_numpy_ndarray(self): # real signature unknown; restored from __doc__
        """
        FixedShapeTensorArray.to_numpy_ndarray(self)
        
                Convert fixed shape tensor extension array to a numpy array (with dim+1).
        
                Note: ``permutation`` should be trivial (``None`` or ``[0, 1, ..., len(shape)-1]``).
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow.lib', '__doc__': '\\n    Concrete class for fixed shape tensor extension arrays.\\n\\n    Examples\\n    --------\\n    Define the extension type for tensor array\\n\\n    >>> import pyarrow as pa\\n    >>> tensor_type = pa.fixed_shape_tensor(pa.int32(), [2, 2])\\n\\n    Create an extension array\\n\\n    >>> arr = [[1, 2, 3, 4], [10, 20, 30, 40], [100, 200, 300, 400]]\\n    >>> storage = pa.array(arr, pa.list_(pa.int32(), 4))\\n    >>> pa.ExtensionArray.from_storage(tensor_type, storage)\\n    <pyarrow.lib.FixedShapeTensorArray object at ...>\\n    [\\n      [\\n        1,\\n        2,\\n        3,\\n        4\\n      ],\\n      [\\n        10,\\n        20,\\n        30,\\n        40\\n      ],\\n      [\\n        100,\\n        200,\\n        300,\\n        400\\n      ]\\n    ]\\n    ', 'to_numpy_ndarray': <cyfunction FixedShapeTensorArray.to_numpy_ndarray at 0x0000029E0B06D110>, 'from_numpy_ndarray': <staticmethod object at 0x0000029E0B068610>, '__dict__': <attribute '__dict__' of 'FixedShapeTensorArray' objects>})"


