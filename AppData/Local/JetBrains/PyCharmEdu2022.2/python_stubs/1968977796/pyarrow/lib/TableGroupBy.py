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


from .object import object

class TableGroupBy(object):
    """
    A grouping of columns in a table on which to perform aggregations.
    
        Parameters
        ----------
        table : pyarrow.Table
            Input table to execute the aggregation on.
        keys : str or list[str]
            Name of the grouped columns.
        use_threads : bool, default True
            Whether to use multithreading or not. When set to True (the default),
            no stable ordering of the output is guaranteed.
    
        Examples
        --------
        >>> import pyarrow as pa
        >>> t = pa.table([
        ...       pa.array(["a", "a", "b", "b", "c"]),
        ...       pa.array([1, 2, 3, 4, 5]),
        ... ], names=["keys", "values"])
    
        Grouping of columns:
    
        >>> pa.TableGroupBy(t,"keys")
        <pyarrow.lib.TableGroupBy object at ...>
    
        Perform aggregations:
    
        >>> pa.TableGroupBy(t,"keys").aggregate([("values", "sum")])
        pyarrow.Table
        keys: string
        values_sum: int64
        ----
        keys: [["a","b","c"]]
        values_sum: [[3,7,5]]
    """
    def aggregate(self, aggregations): # real signature unknown; restored from __doc__
        """
        TableGroupBy.aggregate(self, aggregations)
        
                Perform an aggregation over the grouped columns of the table.
        
                Parameters
                ----------
                aggregations : list[tuple(str, str)] or list[tuple(str, str, FunctionOptions)]
                    List of tuples, where each tuple is one aggregation specification
                    and consists of: aggregation column name followed
                    by function name and optionally aggregation function option.
                    Pass empty list to get a single row for each group.
                    The column name can be a string, an empty list or a list of
                    column names, for unary, nullary and n-ary aggregation functions
                    respectively.
        
                    For the list of function names and respective aggregation
                    function options see :ref:`py-grouped-aggrs`.
        
                Returns
                -------
                Table
                    Results of the aggregation functions.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> t = pa.table([
                ...       pa.array(["a", "a", "b", "b", "c"]),
                ...       pa.array([1, 2, 3, 4, 5]),
                ... ], names=["keys", "values"])
        
                Sum the column "values" over the grouped column "keys":
        
                >>> t.group_by("keys").aggregate([("values", "sum")])
                pyarrow.Table
                keys: string
                values_sum: int64
                ----
                keys: [["a","b","c"]]
                values_sum: [[3,7,5]]
        
                Count the rows over the grouped column "keys":
        
                >>> t.group_by("keys").aggregate([([], "count_all")])
                pyarrow.Table
                keys: string
                count_all: int64
                ----
                keys: [["a","b","c"]]
                count_all: [[2,2,1]]
        
                Do multiple aggregations:
        
                >>> t.group_by("keys").aggregate([
                ...    ("values", "sum"),
                ...    ("keys", "count")
                ... ])
                pyarrow.Table
                keys: string
                values_sum: int64
                keys_count: int64
                ----
                keys: [["a","b","c"]]
                values_sum: [[3,7,5]]
                keys_count: [[2,2,1]]
        
                Count the number of non-null values for column "values"
                over the grouped column "keys":
        
                >>> import pyarrow.compute as pc
                >>> t.group_by(["keys"]).aggregate([
                ...    ("values", "count", pc.CountOptions(mode="only_valid"))
                ... ])
                pyarrow.Table
                keys: string
                values_count: int64
                ----
                keys: [["a","b","c"]]
                values_count: [[2,2,1]]
        
                Get a single row for each group in column "keys":
        
                >>> t.group_by("keys").aggregate([])
                pyarrow.Table
                keys: string
                ----
                keys: [["a","b","c"]]
        """
        pass

    def __init__(self, table, keys, use_threads=True): # real signature unknown; restored from __doc__
        """ TableGroupBy.__init__(self, table, keys, use_threads=True) """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow.lib\', \'__doc__\': \'\\n    A grouping of columns in a table on which to perform aggregations.\\n\\n    Parameters\\n    ----------\\n    table : pyarrow.Table\\n        Input table to execute the aggregation on.\\n    keys : str or list[str]\\n        Name of the grouped columns.\\n    use_threads : bool, default True\\n        Whether to use multithreading or not. When set to True (the default),\\n        no stable ordering of the output is guaranteed.\\n\\n    Examples\\n    --------\\n    >>> import pyarrow as pa\\n    >>> t = pa.table([\\n    ...       pa.array(["a", "a", "b", "b", "c"]),\\n    ...       pa.array([1, 2, 3, 4, 5]),\\n    ... ], names=["keys", "values"])\\n\\n    Grouping of columns:\\n\\n    >>> pa.TableGroupBy(t,"keys")\\n    <pyarrow.lib.TableGroupBy object at ...>\\n\\n    Perform aggregations:\\n\\n    >>> pa.TableGroupBy(t,"keys").aggregate([("values", "sum")])\\n    pyarrow.Table\\n    keys: string\\n    values_sum: int64\\n    ----\\n    keys: [["a","b","c"]]\\n    values_sum: [[3,7,5]]\\n    \', \'__init__\': <cyfunction TableGroupBy.__init__ at 0x0000029E0B06D2B0>, \'aggregate\': <cyfunction TableGroupBy.aggregate at 0x0000029E0B06D380>, \'__dict__\': <attribute \'__dict__\' of \'TableGroupBy\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'TableGroupBy\' objects>})'


