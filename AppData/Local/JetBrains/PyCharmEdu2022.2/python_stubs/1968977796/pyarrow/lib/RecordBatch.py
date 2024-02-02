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


from ._Tabular import _Tabular

class RecordBatch(_Tabular):
    """
    Batch of rows of columns of equal length
    
        Warnings
        --------
        Do not call this class's constructor directly, use one of the
        ``RecordBatch.from_*`` functions instead.
    
        Examples
        --------
        >>> import pyarrow as pa
        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
        >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
        >>> names = ["n_legs", "animals"]
    
        Constructing a RecordBatch from arrays:
    
        >>> pa.RecordBatch.from_arrays([n_legs, animals], names=names)
        pyarrow.RecordBatch
        n_legs: int64
        animals: string
        ----
        n_legs: [2,2,4,4,5,100]
        animals: ["Flamingo","Parrot","Dog","Horse","Brittle stars","Centipede"]
        >>> pa.RecordBatch.from_arrays([n_legs, animals], names=names).to_pandas()
           n_legs        animals
        0       2       Flamingo
        1       2         Parrot
        2       4            Dog
        3       4          Horse
        4       5  Brittle stars
        5     100      Centipede
    
        Constructing a RecordBatch from pandas DataFrame:
    
        >>> import pandas as pd
        >>> df = pd.DataFrame({'year': [2020, 2022, 2021, 2022],
        ...                    'month': [3, 5, 7, 9],
        ...                    'day': [1, 5, 9, 13],
        ...                    'n_legs': [2, 4, 5, 100],
        ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
        >>> pa.RecordBatch.from_pandas(df)
        pyarrow.RecordBatch
        year: int64
        month: int64
        day: int64
        n_legs: int64
        animals: string
        ----
        year: [2020,2022,2021,2022]
        month: [3,5,7,9]
        day: [1,5,9,13]
        n_legs: [2,4,5,100]
        animals: ["Flamingo","Horse","Brittle stars","Centipede"]
        >>> pa.RecordBatch.from_pandas(df).to_pandas()
           year  month  day  n_legs        animals
        0  2020      3    1       2       Flamingo
        1  2022      5    5       4          Horse
        2  2021      7    9       5  Brittle stars
        3  2022      9   13     100      Centipede
    
        Constructing a RecordBatch from pylist:
    
        >>> pylist = [{'n_legs': 2, 'animals': 'Flamingo'},
        ...           {'n_legs': 4, 'animals': 'Dog'}]
        >>> pa.RecordBatch.from_pylist(pylist).to_pandas()
           n_legs   animals
        0       2  Flamingo
        1       4       Dog
    
        You can also construct a RecordBatch using :func:`pyarrow.record_batch`:
    
        >>> pa.record_batch([n_legs, animals], names=names).to_pandas()
           n_legs        animals
        0       2       Flamingo
        1       2         Parrot
        2       4            Dog
        3       4          Horse
        4       5  Brittle stars
        5     100      Centipede
    
        >>> pa.record_batch(df)
        pyarrow.RecordBatch
        year: int64
        month: int64
        day: int64
        n_legs: int64
        animals: string
        ----
        year: [2020,2022,2021,2022]
        month: [3,5,7,9]
        day: [1,5,9,13]
        n_legs: [2,4,5,100]
        animals: ["Flamingo","Horse","Brittle stars","Centipede"]
    """
    def equals(self, other, bool_check_metadata=False): # real signature unknown; restored from __doc__
        """
        RecordBatch.equals(self, other, bool check_metadata=False)
        
                Check if contents of two record batches are equal.
        
                Parameters
                ----------
                other : pyarrow.RecordBatch
                    RecordBatch to compare against.
                check_metadata : bool, default False
                    Whether schema metadata equality should be checked as well.
        
                Returns
                -------
                are_equal : bool
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
                >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
                >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],
                ...                                     names=["n_legs", "animals"])
                >>> batch_0 = pa.record_batch([])
                >>> batch_1 = pa.RecordBatch.from_arrays([n_legs, animals],
                ...                                       names=["n_legs", "animals"],
                ...                                       metadata={"n_legs": "Number of legs per animal"})
                >>> batch.equals(batch)
                True
                >>> batch.equals(batch_0)
                False
                >>> batch.equals(batch_1)
                True
                >>> batch.equals(batch_1, check_metadata=True)
                False
        """
        pass

    def filter(self, mask, null_selection_behavior=None): # real signature unknown; restored from __doc__
        """
        RecordBatch.filter(self, mask, null_selection_behavior=u'drop')
        
                Select rows from the record batch.
        
                See :func:`pyarrow.compute.filter` for full usage.
        
                Parameters
                ----------
                mask : Array or array-like
                    The boolean mask to filter the record batch with.
                null_selection_behavior : str, default "drop"
                    How nulls in the mask should be handled.
        
                Returns
                -------
                filtered : RecordBatch
                    A record batch of the same schema, with only the rows selected
                    by the boolean mask.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
                >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
                >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],
                ...                                     names=["n_legs", "animals"])
                >>> batch.to_pandas()
                   n_legs        animals
                0       2       Flamingo
                1       2         Parrot
                2       4            Dog
                3       4          Horse
                4       5  Brittle stars
                5     100      Centipede
        
                Define a mask and select rows:
        
                >>> mask=[True, True, False, True, False, None]
                >>> batch.filter(mask).to_pandas()
                   n_legs   animals
                0       2  Flamingo
                1       2    Parrot
                2       4     Horse
                >>> batch.filter(mask, null_selection_behavior='emit_null').to_pandas()
                   n_legs   animals
                0     2.0  Flamingo
                1     2.0    Parrot
                2     4.0     Horse
                3     NaN      None
        """
        pass

    def from_arrays(self, list_arrays, names=None, schema=None, metadata=None): # real signature unknown; restored from __doc__
        """
        RecordBatch.from_arrays(list arrays, names=None, schema=None, metadata=None)
        
                Construct a RecordBatch from multiple pyarrow.Arrays
        
                Parameters
                ----------
                arrays : list of pyarrow.Array
                    One for each field in RecordBatch
                names : list of str, optional
                    Names for the batch fields. If not passed, schema must be passed
                schema : Schema, default None
                    Schema for the created batch. If not passed, names must be passed
                metadata : dict or Mapping, default None
                    Optional metadata for the schema (if inferred).
        
                Returns
                -------
                pyarrow.RecordBatch
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
                >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
                >>> names = ["n_legs", "animals"]
        
                Construct a RecordBatch from pyarrow Arrays using names:
        
                >>> pa.RecordBatch.from_arrays([n_legs, animals], names=names)
                pyarrow.RecordBatch
                n_legs: int64
                animals: string
                ----
                n_legs: [2,2,4,4,5,100]
                animals: ["Flamingo","Parrot","Dog","Horse","Brittle stars","Centipede"]
                >>> pa.RecordBatch.from_arrays([n_legs, animals], names=names).to_pandas()
                   n_legs        animals
                0       2       Flamingo
                1       2         Parrot
                2       4            Dog
                3       4          Horse
                4       5  Brittle stars
                5     100      Centipede
        
                Construct a RecordBatch from pyarrow Arrays using schema:
        
                >>> my_schema = pa.schema([
                ...     pa.field('n_legs', pa.int64()),
                ...     pa.field('animals', pa.string())],
                ...     metadata={"n_legs": "Number of legs per animal"})
                >>> pa.RecordBatch.from_arrays([n_legs, animals], schema=my_schema).to_pandas()
                   n_legs        animals
                0       2       Flamingo
                1       2         Parrot
                2       4            Dog
                3       4          Horse
                4       5  Brittle stars
                5     100      Centipede
                >>> pa.RecordBatch.from_arrays([n_legs, animals], schema=my_schema).schema
                n_legs: int64
                animals: string
                -- schema metadata --
                n_legs: 'Number of legs per animal'
        """
        pass

    @classmethod
    def from_pandas(cls, type_cls, df, Schema_schema=None, preserve_index=None, nthreads=None, columns=None): # real signature unknown; restored from __doc__
        """
        RecordBatch.from_pandas(type cls, df, Schema schema=None, preserve_index=None, nthreads=None, columns=None)
        
                Convert pandas.DataFrame to an Arrow RecordBatch
        
                Parameters
                ----------
                df : pandas.DataFrame
                schema : pyarrow.Schema, optional
                    The expected schema of the RecordBatch. This can be used to
                    indicate the type of columns if we cannot infer it automatically.
                    If passed, the output will have exactly this schema. Columns
                    specified in the schema that are not found in the DataFrame columns
                    or its index will raise an error. Additional columns or index
                    levels in the DataFrame which are not specified in the schema will
                    be ignored.
                preserve_index : bool, optional
                    Whether to store the index as an additional column in the resulting
                    ``RecordBatch``. The default of None will store the index as a
                    column, except for RangeIndex which is stored as metadata only. Use
                    ``preserve_index=True`` to force it to be stored as a column.
                nthreads : int, default None
                    If greater than 1, convert columns to Arrow in parallel using
                    indicated number of threads. By default, this follows
                    :func:`pyarrow.cpu_count` (may use up to system CPU count threads).
                columns : list, optional
                   List of column to be converted. If None, use all columns.
        
                Returns
                -------
                pyarrow.RecordBatch
        
        
                Examples
                --------
                >>> import pandas as pd
                >>> df = pd.DataFrame({'year': [2020, 2022, 2021, 2022],
                ...                    'month': [3, 5, 7, 9],
                ...                    'day': [1, 5, 9, 13],
                ...                    'n_legs': [2, 4, 5, 100],
                ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
        
                Convert pandas DataFrame to RecordBatch:
        
                >>> import pyarrow as pa
                >>> pa.RecordBatch.from_pandas(df)
                pyarrow.RecordBatch
                year: int64
                month: int64
                day: int64
                n_legs: int64
                animals: string
                ----
                year: [2020,2022,2021,2022]
                month: [3,5,7,9]
                day: [1,5,9,13]
                n_legs: [2,4,5,100]
                animals: ["Flamingo","Horse","Brittle stars","Centipede"]
        
                Convert pandas DataFrame to RecordBatch using schema:
        
                >>> my_schema = pa.schema([
                ...     pa.field('n_legs', pa.int64()),
                ...     pa.field('animals', pa.string())],
                ...     metadata={"n_legs": "Number of legs per animal"})
                >>> pa.RecordBatch.from_pandas(df, schema=my_schema)
                pyarrow.RecordBatch
                n_legs: int64
                animals: string
                ----
                n_legs: [2,4,5,100]
                animals: ["Flamingo","Horse","Brittle stars","Centipede"]
        
                Convert pandas DataFrame to RecordBatch specifying columns:
        
                >>> pa.RecordBatch.from_pandas(df, columns=["n_legs"])
                pyarrow.RecordBatch
                n_legs: int64
                ----
                n_legs: [2,4,5,100]
        """
        pass

    def from_struct_array(self, StructArray_struct_array): # real signature unknown; restored from __doc__
        """
        RecordBatch.from_struct_array(StructArray struct_array)
        
                Construct a RecordBatch from a StructArray.
        
                Each field in the StructArray will become a column in the resulting
                ``RecordBatch``.
        
                Parameters
                ----------
                struct_array : StructArray
                    Array to construct the record batch from.
        
                Returns
                -------
                pyarrow.RecordBatch
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> struct = pa.array([{'n_legs': 2, 'animals': 'Parrot'},
                ...                    {'year': 2022, 'n_legs': 4}])
                >>> pa.RecordBatch.from_struct_array(struct).to_pandas()
                  animals  n_legs    year
                0  Parrot       2     NaN
                1    None       4  2022.0
        """
        pass

    def get_total_buffer_size(self): # real signature unknown; restored from __doc__
        """
        RecordBatch.get_total_buffer_size(self)
        
                The sum of bytes in each buffer referenced by the record batch
        
                An array may only reference a portion of a buffer.
                This method will overestimate in this case and return the
                byte size of the entire buffer.
        
                If a buffer is referenced multiple times then it will
                only be counted once.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
                >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
                >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],
                ...                                     names=["n_legs", "animals"])
                >>> batch.get_total_buffer_size()
                120
        """
        pass

    def replace_schema_metadata(self, metadata=None): # real signature unknown; restored from __doc__
        """
        RecordBatch.replace_schema_metadata(self, metadata=None)
        
                Create shallow copy of record batch by replacing schema
                key-value metadata with the indicated new metadata (which may be None,
                which deletes any existing metadata
        
                Parameters
                ----------
                metadata : dict, default None
        
                Returns
                -------
                shallow_copy : RecordBatch
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
        
                Constructing a RecordBatch with schema and metadata:
        
                >>> my_schema = pa.schema([
                ...     pa.field('n_legs', pa.int64())],
                ...     metadata={"n_legs": "Number of legs per animal"})
                >>> batch = pa.RecordBatch.from_arrays([n_legs], schema=my_schema)
                >>> batch.schema
                n_legs: int64
                -- schema metadata --
                n_legs: 'Number of legs per animal'
        
                Shallow copy of a RecordBatch with deleted schema metadata:
        
                >>> batch.replace_schema_metadata().schema
                n_legs: int64
        """
        pass

    def select(self, columns): # real signature unknown; restored from __doc__
        """
        RecordBatch.select(self, columns)
        
                Select columns of the RecordBatch.
        
                Returns a new RecordBatch with the specified columns, and metadata
                preserved.
        
                Parameters
                ----------
                columns : list-like
                    The column names or integer indices to select.
        
                Returns
                -------
                RecordBatch
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
                >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
                >>> batch = pa.record_batch([n_legs, animals],
                ...                          names=["n_legs", "animals"])
        
                Select columns my indices:
        
                >>> batch.select([1])
                pyarrow.RecordBatch
                animals: string
                ----
                animals: ["Flamingo","Parrot","Dog","Horse","Brittle stars","Centipede"]
        
                Select columns by names:
        
                >>> batch.select(["n_legs"])
                pyarrow.RecordBatch
                n_legs: int64
                ----
                n_legs: [2,2,4,4,5,100]
        """
        pass

    def serialize(self, memory_pool=None): # real signature unknown; restored from __doc__
        """
        RecordBatch.serialize(self, memory_pool=None)
        
                Write RecordBatch to Buffer as encapsulated IPC message, which does not
                include a Schema.
        
                To reconstruct a RecordBatch from the encapsulated IPC message Buffer
                returned by this function, a Schema must be passed separately. See
                Examples.
        
                Parameters
                ----------
                memory_pool : MemoryPool, default None
                    Uses default memory pool if not specified
        
                Returns
                -------
                serialized : Buffer
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
                >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
                >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],
                ...                                     names=["n_legs", "animals"])
                >>> buf = batch.serialize()
                >>> buf
                <pyarrow.Buffer address=0x... size=... is_cpu=True is_mutable=True>
        
                Reconstruct RecordBatch from IPC message Buffer and original Schema
        
                >>> pa.ipc.read_record_batch(buf, batch.schema)
                pyarrow.RecordBatch
                n_legs: int64
                animals: string
                ----
                n_legs: [2,2,4,4,5,100]
                animals: ["Flamingo","Parrot","Dog","Horse","Brittle stars","Centipede"]
        """
        pass

    def slice(self, offset=0, length=None): # real signature unknown; restored from __doc__
        """
        RecordBatch.slice(self, offset=0, length=None)
        
                Compute zero-copy slice of this RecordBatch
        
                Parameters
                ----------
                offset : int, default 0
                    Offset from start of record batch to slice
                length : int, default None
                    Length of slice (default is until end of batch starting from
                    offset)
        
                Returns
                -------
                sliced : RecordBatch
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
                >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
                >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],
                ...                                     names=["n_legs", "animals"])
                >>> batch.to_pandas()
                   n_legs        animals
                0       2       Flamingo
                1       2         Parrot
                2       4            Dog
                3       4          Horse
                4       5  Brittle stars
                5     100      Centipede
                >>> batch.slice(offset=3).to_pandas()
                   n_legs        animals
                0       4          Horse
                1       5  Brittle stars
                2     100      Centipede
                >>> batch.slice(length=2).to_pandas()
                   n_legs   animals
                0       2  Flamingo
                1       2    Parrot
                >>> batch.slice(offset=3, length=1).to_pandas()
                   n_legs animals
                0       4   Horse
        """
        pass

    def to_struct_array(self): # real signature unknown; restored from __doc__
        """
        RecordBatch.to_struct_array(self)
        
                Convert to a struct array.
        """
        pass

    def validate(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        RecordBatch.validate(self, *, full=False)
        
                Perform validation checks.  An exception is raised if validation fails.
        
                By default only cheap validation checks are run.  Pass `full=True`
                for thorough validation checks (potentially O(n)).
        
                Parameters
                ----------
                full : bool, default False
                    If True, run expensive checks, otherwise cheap checks only.
        
                Raises
                ------
                ArrowInvalid
        """
        pass

    def _column(self, int_i): # real signature unknown; restored from __doc__
        """
        RecordBatch._column(self, int i)
        
                Select single column from record batch by its numeric index.
        
                Parameters
                ----------
                i : int
                    The index of the column to retrieve.
        
                Returns
                -------
                column : pyarrow.Array
        """
        pass

    def _export_to_c(self, out_ptr, out_schema_ptr=0): # real signature unknown; restored from __doc__
        """
        RecordBatch._export_to_c(self, out_ptr, out_schema_ptr=0)
        
                Export to a C ArrowArray struct, given its pointer.
        
                If a C ArrowSchema struct pointer is also given, the record batch
                schema is exported to it at the same time.
        
                Parameters
                ----------
                out_ptr: int
                    The raw pointer to a C ArrowArray struct.
                out_schema_ptr: int (optional)
                    The raw pointer to a C ArrowSchema struct.
        
                Be careful: if you don't pass the ArrowArray struct to a consumer,
                array memory will leak.  This is a low-level function intended for
                expert users.
        """
        pass

    def _import_from_c(self, in_ptr, schema): # real signature unknown; restored from __doc__
        """
        RecordBatch._import_from_c(in_ptr, schema)
        
                Import RecordBatch from a C ArrowArray struct, given its pointer
                and the imported schema.
        
                Parameters
                ----------
                in_ptr: int
                    The raw pointer to a C ArrowArray struct.
                type: Schema or int
                    Either a Schema object, or the raw pointer to a C ArrowSchema
                    struct.
        
                This is a low-level function intended for expert users.
        """
        pass

    def _import_from_c_capsule(self, schema_capsule, array_capsule): # real signature unknown; restored from __doc__
        """
        RecordBatch._import_from_c_capsule(schema_capsule, array_capsule)
        
                Import RecordBatch from a pair of PyCapsules containing a C ArrowArray
                and ArrowSchema, respectively.
        
                Parameters
                ----------
                schema_capsule : PyCapsule
                    A PyCapsule containing a C ArrowSchema representation of the schema.
                array_capsule : PyCapsule
                    A PyCapsule containing a C ArrowArray representation of the array.
        
                Returns
                -------
                pyarrow.RecordBatch
        """
        pass

    def _is_initialized(self): # real signature unknown; restored from __doc__
        """ RecordBatch._is_initialized(self) """
        pass

    def _to_pandas(self, options, **kwargs): # real signature unknown; restored from __doc__
        """ RecordBatch._to_pandas(self, options, **kwargs) """
        pass

    def __arrow_c_array__(self, requested_schema=None): # real signature unknown; restored from __doc__
        """
        RecordBatch.__arrow_c_array__(self, requested_schema=None)
        
                Get a pair of PyCapsules containing a C ArrowArray representation of the object.
        
                Parameters
                ----------
                requested_schema : PyCapsule | None
                    A PyCapsule containing a C ArrowSchema representation of a requested
                    schema. PyArrow will attempt to cast the batch to this schema.
                    If None, the schema will be returned as-is, with a schema matching the
                    one returned by :meth:`__arrow_c_schema__()`.
        
                Returns
                -------
                Tuple[PyCapsule, PyCapsule]
                    A pair of PyCapsules containing a C ArrowSchema and ArrowArray,
                    respectively.
        """
        pass

    def __arrow_c_stream__(self, requested_schema=None): # real signature unknown; restored from __doc__
        """
        RecordBatch.__arrow_c_stream__(self, requested_schema=None)
        
                Export the batch as an Arrow C stream PyCapsule.
        
                Parameters
                ----------
                requested_schema : PyCapsule, default None
                    The schema to which the stream should be casted, passed as a
                    PyCapsule containing a C ArrowSchema representation of the
                    requested schema.
                    Currently, this is not supported and will raise a
                    NotImplementedError if the schema doesn't match the current schema.
        
                Returns
                -------
                PyCapsule
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ RecordBatch.__reduce__(self) """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ RecordBatch.__sizeof__(self) """
        pass

    nbytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Total number of bytes consumed by the elements of the record batch.

        In other words, the sum of bytes from all buffer ranges referenced.

        Unlike `get_total_buffer_size` this method will account for array
        offsets.

        If buffers are shared between arrays then the shared
        portion will only be counted multiple times.

        The dictionary of dictionary arrays will always be counted in their
        entirety even if the array only references a portion of the dictionary.

        Examples
        --------
        >>> import pyarrow as pa
        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
        >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
        >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],
        ...                                     names=["n_legs", "animals"])
        >>> batch.nbytes
        116
        """

    num_columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Number of columns

        Returns
        -------
        int

        Examples
        --------
        >>> import pyarrow as pa
        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
        >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
        >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],
        ...                                     names=["n_legs", "animals"])
        >>> batch.num_columns
        2
        """

    num_rows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Number of rows

        Due to the definition of a RecordBatch, all columns have the same
        number of rows.

        Returns
        -------
        int

        Examples
        --------
        >>> import pyarrow as pa
        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
        >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
        >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],
        ...                                     names=["n_legs", "animals"])
        >>> batch.num_rows
        6
        """

    schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Schema of the RecordBatch and its columns

        Returns
        -------
        pyarrow.Schema

        Examples
        --------
        >>> import pyarrow as pa
        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
        >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
        >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],
        ...                                     names=["n_legs", "animals"])
        >>> batch.schema
        n_legs: int64
        animals: string
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000029E04689C30>'


