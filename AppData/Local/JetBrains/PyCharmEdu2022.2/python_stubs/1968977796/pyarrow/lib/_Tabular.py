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


from ._PandasConvertible import _PandasConvertible

class _Tabular(_PandasConvertible):
    """
    _Tabular()
    Internal: An interface for common operations on tabular objects.
    """
    def column(self, i): # real signature unknown; restored from __doc__
        """
        _Tabular.column(self, i)
        
                Select single column from Table or RecordBatch.
        
                Parameters
                ----------
                i : int or string
                    The index or name of the column to retrieve.
        
                Returns
                -------
                column : Array (for RecordBatch) or ChunkedArray (for Table)
        
                Examples
                --------
                Table (works similarly for RecordBatch)
        
                >>> import pyarrow as pa
                >>> import pandas as pd
                >>> df = pd.DataFrame({'n_legs': [2, 4, 5, 100],
                ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
        
                Select a column by numeric index:
        
                >>> table.column(0)
                <pyarrow.lib.ChunkedArray object at ...>
                [
                  [
                    2,
                    4,
                    5,
                    100
                  ]
                ]
        
                Select a column by its name:
        
                >>> table.column("animals")
                <pyarrow.lib.ChunkedArray object at ...>
                [
                  [
                    "Flamingo",
                    "Horse",
                    "Brittle stars",
                    "Centipede"
                  ]
                ]
        """
        pass

    def drop_null(self): # real signature unknown; restored from __doc__
        """
        _Tabular.drop_null(self)
        
                Remove rows that contain missing values from a Table or RecordBatch.
        
                See :func:`pyarrow.compute.drop_null` for full usage.
        
                Returns
                -------
                Table or RecordBatch
                    A tabular object with the same schema, with rows containing
                    no missing values.
        
                Examples
                --------
                Table (works similarly for RecordBatch)
        
                >>> import pyarrow as pa
                >>> import pandas as pd
                >>> df = pd.DataFrame({'year': [None, 2022, 2019, 2021],
                ...                   'n_legs': [2, 4, 5, 100],
                ...                   'animals': ["Flamingo", "Horse", None, "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
                >>> table.drop_null()
                pyarrow.Table
                year: double
                n_legs: int64
                animals: string
                ----
                year: [[2022,2021]]
                n_legs: [[4,100]]
                animals: [["Horse","Centipede"]]
        """
        pass

    def field(self, i): # real signature unknown; restored from __doc__
        """
        _Tabular.field(self, i)
        
                Select a schema field by its column name or numeric index.
        
                Parameters
                ----------
                i : int or string
                    The index or name of the field to retrieve.
        
                Returns
                -------
                Field
        
                Examples
                --------
                Table (works similarly for RecordBatch)
        
                >>> import pyarrow as pa
                >>> import pandas as pd
                >>> df = pd.DataFrame({'n_legs': [2, 4, 5, 100],
                ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
                >>> table.field(0)
                pyarrow.Field<n_legs: int64>
                >>> table.field(1)
                pyarrow.Field<animals: string>
        """
        pass

    @classmethod
    def from_pydict(cls, type_cls, mapping, schema=None, metadata=None): # real signature unknown; restored from __doc__
        """
        _Tabular.from_pydict(type cls, mapping, schema=None, metadata=None)
        
                Construct a Table or RecordBatch from Arrow arrays or columns.
        
                Parameters
                ----------
                mapping : dict or Mapping
                    A mapping of strings to Arrays or Python lists.
                schema : Schema, default None
                    If not passed, will be inferred from the Mapping values.
                metadata : dict or Mapping, default None
                    Optional metadata for the schema (if inferred).
        
                Returns
                -------
                Table or RecordBatch
        
                Examples
                --------
                Table (works similarly for RecordBatch)
        
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 4, 5, 100])
                >>> animals = pa.array(["Flamingo", "Horse", "Brittle stars", "Centipede"])
                >>> pydict = {'n_legs': n_legs, 'animals': animals}
        
                Construct a Table from a dictionary of arrays:
        
                >>> pa.Table.from_pydict(pydict)
                pyarrow.Table
                n_legs: int64
                animals: string
                ----
                n_legs: [[2,4,5,100]]
                animals: [["Flamingo","Horse","Brittle stars","Centipede"]]
                >>> pa.Table.from_pydict(pydict).schema
                n_legs: int64
                animals: string
        
                Construct a Table from a dictionary of arrays with metadata:
        
                >>> my_metadata={"n_legs": "Number of legs per animal"}
                >>> pa.Table.from_pydict(pydict, metadata=my_metadata).schema
                n_legs: int64
                animals: string
                -- schema metadata --
                n_legs: 'Number of legs per animal'
        
                Construct a Table from a dictionary of arrays with pyarrow schema:
        
                >>> my_schema = pa.schema([
                ...     pa.field('n_legs', pa.int64()),
                ...     pa.field('animals', pa.string())],
                ...     metadata={"n_legs": "Number of legs per animal"})
                >>> pa.Table.from_pydict(pydict, schema=my_schema).schema
                n_legs: int64
                animals: string
                -- schema metadata --
                n_legs: 'Number of legs per animal'
        """
        pass

    @classmethod
    def from_pylist(cls, type_cls, mapping, schema=None, metadata=None): # real signature unknown; restored from __doc__
        """
        _Tabular.from_pylist(type cls, mapping, schema=None, metadata=None)
        
                Construct a Table or RecordBatch from list of rows / dictionaries.
        
                Parameters
                ----------
                mapping : list of dicts of rows
                    A mapping of strings to row values.
                schema : Schema, default None
                    If not passed, will be inferred from the first row of the
                    mapping values.
                metadata : dict or Mapping, default None
                    Optional metadata for the schema (if inferred).
        
                Returns
                -------
                Table or RecordBatch
        
                Examples
                --------
                Table (works similarly for RecordBatch)
        
                >>> import pyarrow as pa
                >>> pylist = [{'n_legs': 2, 'animals': 'Flamingo'},
                ...           {'n_legs': 4, 'animals': 'Dog'}]
        
                Construct a Table from a list of rows:
        
                >>> pa.Table.from_pylist(pylist)
                pyarrow.Table
                n_legs: int64
                animals: string
                ----
                n_legs: [[2,4]]
                animals: [["Flamingo","Dog"]]
        
                Construct a Table from a list of rows with metadata:
        
                >>> my_metadata={"n_legs": "Number of legs per animal"}
                >>> pa.Table.from_pylist(pylist, metadata=my_metadata).schema
                n_legs: int64
                animals: string
                -- schema metadata --
                n_legs: 'Number of legs per animal'
        
                Construct a Table from a list of rows with pyarrow schema:
        
                >>> my_schema = pa.schema([
                ...     pa.field('n_legs', pa.int64()),
                ...     pa.field('animals', pa.string())],
                ...     metadata={"n_legs": "Number of legs per animal"})
                >>> pa.Table.from_pylist(pylist, schema=my_schema).schema
                n_legs: int64
                animals: string
                -- schema metadata --
                n_legs: 'Number of legs per animal'
        """
        pass

    def itercolumns(self): # real signature unknown; restored from __doc__
        """
        _Tabular.itercolumns(self)
        
                Iterator over all columns in their numerical order.
        
                Yields
                ------
                Array (for RecordBatch) or ChunkedArray (for Table)
        
                Examples
                --------
                Table (works similarly for RecordBatch)
        
                >>> import pyarrow as pa
                >>> import pandas as pd
                >>> df = pd.DataFrame({'n_legs': [None, 4, 5, None],
                ...                    'animals': ["Flamingo", "Horse", None, "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
                >>> for i in table.itercolumns():
                ...     print(i.null_count)
                ...
                2
                1
        """
        pass

    def sort_by(self, sorting, **kwargs): # real signature unknown; restored from __doc__
        """
        _Tabular.sort_by(self, sorting, **kwargs)
        
                Sort the Table or RecordBatch by one or multiple columns.
        
                Parameters
                ----------
                sorting : str or list[tuple(name, order)]
                    Name of the column to use to sort (ascending), or
                    a list of multiple sorting conditions where
                    each entry is a tuple with column name
                    and sorting order ("ascending" or "descending")
                **kwargs : dict, optional
                    Additional sorting options.
                    As allowed by :class:`SortOptions`
        
                Returns
                -------
                Table or RecordBatch
                    A new tabular object sorted according to the sort keys.
        
                Examples
                --------
                Table (works similarly for RecordBatch)
        
                >>> import pandas as pd
                >>> import pyarrow as pa
                >>> df = pd.DataFrame({'year': [2020, 2022, 2021, 2022, 2019, 2021],
                ...                    'n_legs': [2, 2, 4, 4, 5, 100],
                ...                    'animal': ["Flamingo", "Parrot", "Dog", "Horse",
                ...                    "Brittle stars", "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
                >>> table.sort_by('animal')
                pyarrow.Table
                year: int64
                n_legs: int64
                animal: string
                ----
                year: [[2019,2021,2021,2020,2022,2022]]
                n_legs: [[5,100,4,2,4,2]]
                animal: [["Brittle stars","Centipede","Dog","Flamingo","Horse","Parrot"]]
        """
        pass

    def take(self, indices): # real signature unknown; restored from __doc__
        """
        _Tabular.take(self, indices)
        
                Select rows from a Table or RecordBatch.
        
                See :func:`pyarrow.compute.take` for full usage.
        
                Parameters
                ----------
                indices : Array or array-like
                    The indices in the tabular object whose rows will be returned.
        
                Returns
                -------
                Table or RecordBatch
                    A tabular object with the same schema, containing the taken rows.
        
                Examples
                --------
                Table (works similarly for RecordBatch)
        
                >>> import pyarrow as pa
                >>> import pandas as pd
                >>> df = pd.DataFrame({'year': [2020, 2022, 2019, 2021],
                ...                    'n_legs': [2, 4, 5, 100],
                ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
                >>> table.take([1,3])
                pyarrow.Table
                year: int64
                n_legs: int64
                animals: string
                ----
                year: [[2022,2021]]
                n_legs: [[4,100]]
                animals: [["Horse","Centipede"]]
        """
        pass

    def to_pydict(self): # real signature unknown; restored from __doc__
        """
        _Tabular.to_pydict(self)
        
                Convert the Table or RecordBatch to a dict or OrderedDict.
        
                Returns
                -------
                dict
        
                Examples
                --------
                Table (works similarly for RecordBatch)
        
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
                >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
                >>> table = pa.Table.from_arrays([n_legs, animals], names=["n_legs", "animals"])
                >>> table.to_pydict()
                {'n_legs': [2, 2, 4, 4, 5, 100], 'animals': ['Flamingo', 'Parrot', ..., 'Centipede']}
        """
        pass

    def to_pylist(self): # real signature unknown; restored from __doc__
        """
        _Tabular.to_pylist(self)
        
                Convert the Table or RecordBatch to a list of rows / dictionaries.
        
                Returns
                -------
                list
        
                Examples
                --------
                Table (works similarly for RecordBatch)
        
                >>> import pyarrow as pa
                >>> data = [[2, 4, 5, 100],
                ...         ["Flamingo", "Horse", "Brittle stars", "Centipede"]]
                >>> table = pa.table(data, names=["n_legs", "animals"])
                >>> table.to_pylist()
                [{'n_legs': 2, 'animals': 'Flamingo'}, {'n_legs': 4, 'animals': 'Horse'}, ...
        """
        pass

    def to_string(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        _Tabular.to_string(self, *, show_metadata=False, preview_cols=0)
        
                Return human-readable string representation of Table or RecordBatch.
        
                Parameters
                ----------
                show_metadata : bool, default False
                    Display Field-level and Schema-level KeyValueMetadata.
                preview_cols : int, default 0
                    Display values of the columns for the first N columns.
        
                Returns
                -------
                str
        """
        pass

    def _column(self, int_i): # real signature unknown; restored from __doc__
        """ _Tabular._column(self, int i) """
        pass

    def _ensure_integer_index(self, i): # real signature unknown; restored from __doc__
        """
        _Tabular._ensure_integer_index(self, i)
        
                Ensure integer index (convert string column name to integer if needed).
        """
        pass

    def _is_initialized(self): # real signature unknown; restored from __doc__
        """ _Tabular._is_initialized(self) """
        pass

    def __array__(self, dtype=None): # real signature unknown; restored from __doc__
        """ _Tabular.__array__(self, dtype=None) """
        pass

    def __dataframe__(self, nan_as_null=False, allow_copy=True): # real signature unknown; restored from __doc__
        """
        _Tabular.__dataframe__(self, nan_as_null: bool = False, allow_copy: bool = True)
        
                Return the dataframe interchange object implementing the interchange protocol.
        
                Parameters
                ----------
                nan_as_null : bool, default False
                    Whether to tell the DataFrame to overwrite null values in the data
                    with ``NaN`` (or ``NaT``).
                allow_copy : bool, default True
                    Whether to allow memory copying when exporting. If set to False
                    it would cause non-zero-copy exports to fail.
        
                Returns
                -------
                DataFrame interchange object
                    The object which consuming library can use to ingress the dataframe.
        
                Notes
                -----
                Details on the interchange protocol:
                https://data-apis.org/dataframe-protocol/latest/index.html
                `nan_as_null` currently has no effect; once support for nullable extension
                dtypes is added, this value should be propagated to columns.
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """
        Slice or return column at given index or column name
        
                Parameters
                ----------
                key : integer, str, or slice
                    Slices with step not equal to 1 (or None) will produce a copy
                    rather than a zero-copy view
        
                Returns
                -------
                Array (from RecordBatch) or ChunkedArray (from Table) for column input.
                RecordBatch or Table for slice input.
        """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _Tabular.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _Tabular.__setstate_cython__(self, __pyx_state) """
        pass

    columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        List of all columns in numerical order.

        Returns
        -------
        columns : list of Array (for RecordBatch) or list of ChunkedArray (for Table)

        Examples
        --------
        Table (works similarly for RecordBatch)

        >>> import pyarrow as pa
        >>> import pandas as pd
        >>> df = pd.DataFrame({'n_legs': [None, 4, 5, None],
        ...                    'animals': ["Flamingo", "Horse", None, "Centipede"]})
        >>> table = pa.Table.from_pandas(df)
        >>> table.columns
        [<pyarrow.lib.ChunkedArray object at ...>
        [
          [
            null,
            4,
            5,
            null
          ]
        ], <pyarrow.lib.ChunkedArray object at ...>
        [
          [
            "Flamingo",
            "Horse",
            null,
            "Centipede"
          ]
        ]]
        """

    column_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Names of the Table or RecordBatch columns.

        Returns
        -------
        list of str

        Examples
        --------
        Table (works similarly for RecordBatch)

        >>> import pyarrow as pa
        >>> table = pa.Table.from_arrays([[2, 4, 5, 100],
        ...                               ["Flamingo", "Horse", "Brittle stars", "Centipede"]],
        ...                               names=['n_legs', 'animals'])
        >>> table.column_names
        ['n_legs', 'animals']
        """

    num_columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_rows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None


