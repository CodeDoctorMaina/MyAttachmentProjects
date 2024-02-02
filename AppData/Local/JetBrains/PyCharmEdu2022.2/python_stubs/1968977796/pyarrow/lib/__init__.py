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


# Variables with simple values

cpp_version = '15.0.0'

DEFAULT_BUFFER_SIZE = 65536

have_signal_refcycle = True

Type_BINARY = 14
Type_BOOL = 1
Type_DATE32 = 16
Type_DATE64 = 17
Type_DECIMAL128 = 23
Type_DECIMAL256 = 24

Type_DENSE_UNION = 28

Type_DICTIONARY = 29
Type_DOUBLE = 12
Type_DURATION = 33

Type_FIXED_SIZE_BINARY = 15
Type_FIXED_SIZE_LIST = 32

Type_FLOAT = 11

Type_HALF_FLOAT = 10

Type_INT16 = 5
Type_INT32 = 7
Type_INT64 = 9
Type_INT8 = 3

Type_INTERVAL_MONTH_DAY_NANO = 37

Type_LARGE_BINARY = 35
Type_LARGE_LIST = 36
Type_LARGE_STRING = 34

Type_LIST = 25
Type_MAP = 30
Type_NA = 0

Type_RUN_END_ENCODED = 38

Type_SPARSE_UNION = 27

Type_STRING = 13
Type_STRUCT = 26
Type_TIME32 = 19
Type_TIME64 = 20
Type_TIMESTAMP = 18
Type_UINT16 = 4
Type_UINT32 = 6
Type_UINT64 = 8
Type_UINT8 = 2

UnionMode_DENSE = 1
UnionMode_SPARSE = 0

V1 = 0

V2 = 1

V3 = 2

V4 = 3

V5 = 4

_py_extension_type_auto_load = False

__pac = None
__pc = None

# functions

def allocate_buffer(int64_t_size, MemoryPool_memory_pool=None, resizable=False): # real signature unknown; restored from __doc__
    """
    allocate_buffer(int64_t size, MemoryPool memory_pool=None, resizable=False)
    
        Allocate a mutable buffer.
    
        Parameters
        ----------
        size : int
            Number of bytes to allocate (plus internal padding)
        memory_pool : MemoryPool, optional
            The pool to allocate memory from.
            If not given, the default memory pool is used.
        resizable : bool, default False
            If true, the returned buffer is resizable.
    
        Returns
        -------
        buffer : Buffer or ResizableBuffer
    """
    pass

def array(obj, type=None, mask=None, size=None, from_pandas=None, bool_safe=True, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
    """
    array(obj, type=None, mask=None, size=None, from_pandas=None, bool safe=True, MemoryPool memory_pool=None)
    
        Create pyarrow.Array instance from a Python object.
    
        Parameters
        ----------
        obj : sequence, iterable, ndarray, pandas.Series, Arrow-compatible array
            If both type and size are specified may be a single use iterable. If
            not strongly-typed, Arrow type will be inferred for resulting array.
            Any Arrow-compatible array that implements the Arrow PyCapsule Protocol
            (has an ``__arrow_c_array__`` method) can be passed as well.
        type : pyarrow.DataType
            Explicit type to attempt to coerce to, otherwise will be inferred from
            the data.
        mask : array[bool], optional
            Indicate which values are null (True) or not null (False).
        size : int64, optional
            Size of the elements. If the input is larger than size bail at this
            length. For iterators, if size is larger than the input iterator this
            will be treated as a "max size", but will involve an initial allocation
            of size followed by a resize to the actual size (so if you know the
            exact size specifying it correctly will give you better performance).
        from_pandas : bool, default None
            Use pandas's semantics for inferring nulls from values in
            ndarray-like data. If passed, the mask tasks precedence, but
            if a value is unmasked (not-null), but still null according to
            pandas semantics, then it is null. Defaults to False if not
            passed explicitly by user, or True if a pandas object is
            passed in.
        safe : bool, default True
            Check for overflows or other unsafe conversions.
        memory_pool : pyarrow.MemoryPool, optional
            If not passed, will allocate memory from the currently-set default
            memory pool.
    
        Returns
        -------
        array : pyarrow.Array or pyarrow.ChunkedArray
            A ChunkedArray instead of an Array is returned if:
    
            - the object data overflowed binary storage.
            - the object's ``__arrow_array__`` protocol method returned a chunked
              array.
    
        Notes
        -----
        Timezone will be preserved in the returned array for timezone-aware data,
        else no timezone will be returned for naive timestamps.
        Internally, UTC values are stored for timezone-aware data with the
        timezone set in the data type.
    
        Pandas's DateOffsets and dateutil.relativedelta.relativedelta are by
        default converted as MonthDayNanoIntervalArray. relativedelta leapdays
        are ignored as are all absolute fields on both objects. datetime.timedelta
        can also be converted to MonthDayNanoIntervalArray but this requires
        passing MonthDayNanoIntervalType explicitly.
    
        Converting to dictionary array will promote to a wider integer type for
        indices if the number of distinct values cannot be represented, even if
        the index type was explicitly set. This means that if there are more than
        127 values the returned dictionary array's index type will be at least
        pa.int16() even if pa.int8() was passed to the function. Note that an
        explicit index type will not be demoted even if it is wider than required.
    
        Examples
        --------
        >>> import pandas as pd
        >>> import pyarrow as pa
        >>> pa.array(pd.Series([1, 2]))
        <pyarrow.lib.Int64Array object at ...>
        [
          1,
          2
        ]
    
        >>> pa.array(["a", "b", "a"], type=pa.dictionary(pa.int8(), pa.string()))
        <pyarrow.lib.DictionaryArray object at ...>
        ...
        -- dictionary:
          [
            "a",
            "b"
          ]
        -- indices:
          [
            0,
            1,
            0
          ]
    
        >>> import numpy as np
        >>> pa.array(pd.Series([1, 2]), mask=np.array([0, 1], dtype=bool))
        <pyarrow.lib.Int64Array object at ...>
        [
          1,
          null
        ]
    
        >>> arr = pa.array(range(1024), type=pa.dictionary(pa.int8(), pa.int64()))
        >>> arr.type.index_type
        DataType(int16)
    """
    pass

def asarray(values, type=None): # real signature unknown; restored from __doc__
    """
    asarray(values, type=None)
    
        Convert to pyarrow.Array, inferring type if not provided.
    
        Parameters
        ----------
        values : array-like
            This can be a sequence, numpy.ndarray, pyarrow.Array or
            pyarrow.ChunkedArray. If a ChunkedArray is passed, the output will be
            a ChunkedArray, otherwise the output will be a Array.
        type : string or DataType
            Explicitly construct the array with this type. Attempt to cast if
            indicated type is different.
    
        Returns
        -------
        arr : Array or ChunkedArray
    """
    pass

def as_buffer(o): # real signature unknown; restored from __doc__
    """ as_buffer(o) """
    pass

def benchmark_PandasObjectIsNull(list_obj): # real signature unknown; restored from __doc__
    """ benchmark_PandasObjectIsNull(list obj) """
    pass

def binary(int_length=-1): # real signature unknown; restored from __doc__
    """
    binary(int length=-1)
    
        Create variable-length or fixed size binary type.
    
        Parameters
        ----------
        length : int, optional, default -1
            If length == -1 then return a variable length binary type. If length is
            greater than or equal to 0 then return a fixed size binary type of
            width `length`.
    
        Examples
        --------
        Create an instance of a variable-length binary type:
    
        >>> import pyarrow as pa
        >>> pa.binary()
        DataType(binary)
    
        and use the variable-length binary type to create an array:
    
        >>> pa.array(['foo', 'bar', 'baz'], type=pa.binary())
        <pyarrow.lib.BinaryArray object at ...>
        [
          666F6F,
          626172,
          62617A
        ]
    
        Create an instance of a fixed-size binary type:
    
        >>> pa.binary(3)
        FixedSizeBinaryType(fixed_size_binary[3])
    
        and use the fixed-length binary type to create an array:
    
        >>> pa.array(['foo', 'bar', 'baz'], type=pa.binary(3))
        <pyarrow.lib.FixedSizeBinaryArray object at ...>
        [
          666F6F,
          626172,
          62617A
        ]
    """
    pass

def bool_(): # real signature unknown; restored from __doc__
    """
    bool_()
    
        Create instance of boolean type.
    
        Examples
        --------
        Create an instance of a boolean type:
    
        >>> import pyarrow as pa
        >>> pa.bool_()
        DataType(bool)
        >>> print(pa.bool_())
        bool
    
        Create a ``Field`` type with a boolean type
        and a name:
    
        >>> pa.field('bool_field', pa.bool_())
        pyarrow.Field<bool_field: bool>
    """
    pass

def chunked_array(arrays, type=None): # real signature unknown; restored from __doc__
    """
    chunked_array(arrays, type=None)
    
        Construct chunked array from list of array-like objects
    
        Parameters
        ----------
        arrays : Array, list of Array, or array-like
            Must all be the same data type. Can be empty only if type also passed.
        type : DataType or string coercible to DataType
    
        Returns
        -------
        ChunkedArray
    
        Examples
        --------
        >>> import pyarrow as pa
        >>> pa.chunked_array([], type=pa.int8())
        <pyarrow.lib.ChunkedArray object at ...>
        [
        ...
        ]
    
        >>> pa.chunked_array([[2, 2, 4], [4, 5, 100]])
        <pyarrow.lib.ChunkedArray object at ...>
        [
          [
            2,
            2,
            4
          ],
          [
            4,
            5,
            100
          ]
        ]
    """
    pass

def compress(buf, codec=None, asbytes=False, memory_pool=None): # real signature unknown; restored from __doc__
    """
    compress(buf, codec=u'lz4', asbytes=False, memory_pool=None)
    
        Compress data from buffer-like object.
    
        Parameters
        ----------
        buf : pyarrow.Buffer, bytes, or other object supporting buffer protocol
        codec : str, default 'lz4'
            Compression codec.
            Supported types: {'brotli, 'gzip', 'lz4', 'lz4_raw', 'snappy', 'zstd'}
        asbytes : bool, default False
            Return result as Python bytes object, otherwise Buffer.
        memory_pool : MemoryPool, default None
            Memory pool to use for buffer allocations, if any.
    
        Returns
        -------
        compressed : pyarrow.Buffer or bytes (if asbytes=True)
    """
    pass

def concat_arrays(arrays, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
    """
    concat_arrays(arrays, MemoryPool memory_pool=None)
    
        Concatenate the given arrays.
    
        The contents of the input arrays are copied into the returned array.
    
        Raises
        ------
        ArrowInvalid
            If not all of the arrays have the same type.
    
        Parameters
        ----------
        arrays : iterable of pyarrow.Array
            Arrays to concatenate, must be identically typed.
        memory_pool : MemoryPool, default None
            For memory allocations. If None, the default pool is used.
    
        Examples
        --------
        >>> import pyarrow as pa
        >>> arr1 = pa.array([2, 4, 5, 100])
        >>> arr2 = pa.array([2, 4])
        >>> pa.concat_arrays([arr1, arr2])
        <pyarrow.lib.Int64Array object at ...>
        [
          2,
          4,
          5,
          100,
          2,
          4
        ]
    """
    pass

def concat_tables(tables, MemoryPool_memory_pool=None, unicode_promote_options=None, **kwargs): # real signature unknown; restored from __doc__
    """
    concat_tables(tables, MemoryPool memory_pool=None, unicode promote_options=u'none', **kwargs)
    
        Concatenate pyarrow.Table objects.
    
        If promote_options="none", a zero-copy concatenation will be performed. The schemas
        of all the Tables must be the same (except the metadata), otherwise an
        exception will be raised. The result Table will share the metadata with the
        first table.
    
        If promote_options="default", any null type arrays will be casted to the type of other
        arrays in the column of the same name. If a table is missing a particular
        field, null values of the appropriate type will be generated to take the
        place of the missing field. The new schema will share the metadata with the
        first table. Each field in the new schema will share the metadata with the
        first table which has the field defined. Note that type promotions may
        involve additional allocations on the given ``memory_pool``.
    
        If promote_options="permissive", the behavior of default plus types will be promoted
        to the common denominator that fits all the fields.
    
        Parameters
        ----------
        tables : iterable of pyarrow.Table objects
            Pyarrow tables to concatenate into a single Table.
        memory_pool : MemoryPool, default None
            For memory allocations, if required, otherwise use default pool.
        promote_options : str, default none
            Accepts strings "none", "default" and "permissive".
        **kwargs : dict, optional
    
        Examples
        --------
        >>> import pyarrow as pa
        >>> t1 = pa.table([
        ...     pa.array([2, 4, 5, 100]),
        ...     pa.array(["Flamingo", "Horse", "Brittle stars", "Centipede"])
        ...     ], names=['n_legs', 'animals'])
        >>> t2 = pa.table([
        ...     pa.array([2, 4]),
        ...     pa.array(["Parrot", "Dog"])
        ...     ], names=['n_legs', 'animals'])
        >>> pa.concat_tables([t1,t2])
        pyarrow.Table
        n_legs: int64
        animals: string
        ----
        n_legs: [[2,4,5,100],[2,4]]
        animals: [["Flamingo","Horse","Brittle stars","Centipede"],["Parrot","Dog"]]
    """
    pass

def contextmanager(func): # reliably restored by inspect
    """
    @contextmanager decorator.
    
        Typical usage:
    
            @contextmanager
            def some_generator(<arguments>):
                <setup>
                try:
                    yield <value>
                finally:
                    <cleanup>
    
        This makes this:
    
            with some_generator(<arguments>) as <variable>:
                <body>
    
        equivalent to this:
    
            <setup>
            try:
                <variable> = <value>
                <body>
            finally:
                <cleanup>
    """
    pass

def cpu_count(): # real signature unknown; restored from __doc__
    """
    cpu_count()
    
        Return the number of threads to use in parallel operations.
    
        The number of threads is determined at startup by inspecting the
        ``OMP_NUM_THREADS`` and ``OMP_THREAD_LIMIT`` environment variables.
        If neither is present, it will default to the number of hardware threads
        on the system. It can be modified at runtime by calling
        :func:`set_cpu_count()`.
    
        See Also
        --------
        set_cpu_count : Modify the size of this pool.
        io_thread_count : The analogous function for the I/O thread pool.
    """
    pass

def create_memory_map(path, size): # real signature unknown; restored from __doc__
    """
    create_memory_map(path, size)
    
        Create a file of the given size and memory-map it.
    
        Parameters
        ----------
        path : str
            The file path to create, on the local filesystem.
        size : int
            The file size to create.
    
        Returns
        -------
        mmap : MemoryMappedFile
    
        Examples
        --------
        Create a file with a memory map:
    
        >>> import pyarrow as pa
        >>> with pa.create_memory_map('example_mmap_create.dat', 27) as mmap:
        ...     mmap.write(b'Create a memory-mapped file')
        ...     mmap.read_at(10, 9)
        ...
        27
        b'memory-map'
    """
    pass

def date32(): # real signature unknown; restored from __doc__
    """
    date32()
    
        Create instance of 32-bit date (days since UNIX epoch 1970-01-01).
    
        Examples
        --------
        Create an instance of 32-bit date type:
    
        >>> import pyarrow as pa
        >>> pa.date32()
        DataType(date32[day])
    
        Create a scalar with 32-bit date type:
    
        >>> from datetime import date
        >>> pa.scalar(date(2012, 1, 1), type=pa.date32())
        <pyarrow.Date32Scalar: datetime.date(2012, 1, 1)>
    """
    pass

def date64(): # real signature unknown; restored from __doc__
    """
    date64()
    
        Create instance of 64-bit date (milliseconds since UNIX epoch 1970-01-01).
    
        Examples
        --------
        Create an instance of 64-bit date type:
    
        >>> import pyarrow as pa
        >>> pa.date64()
        DataType(date64[ms])
    
        Create a scalar with 64-bit date type:
    
        >>> from datetime import datetime
        >>> pa.scalar(datetime(2012, 1, 1), type=pa.date64())
        <pyarrow.Date64Scalar: datetime.date(2012, 1, 1)>
    """
    pass

def decimal128(int_precision, int_scale=0): # real signature unknown; restored from __doc__
    """
    decimal128(int precision, int scale=0) -> DataType
    
        Create decimal type with precision and scale and 128-bit width.
    
        Arrow decimals are fixed-point decimal numbers encoded as a scaled
        integer.  The precision is the number of significant digits that the
        decimal type can represent; the scale is the number of digits after
        the decimal point (note the scale can be negative).
    
        As an example, ``decimal128(7, 3)`` can exactly represent the numbers
        1234.567 and -1234.567 (encoded internally as the 128-bit integers
        1234567 and -1234567, respectively), but neither 12345.67 nor 123.4567.
    
        ``decimal128(5, -3)`` can exactly represent the number 12345000
        (encoded internally as the 128-bit integer 12345), but neither
        123450000 nor 1234500.
    
        If you need a precision higher than 38 significant digits, consider
        using ``decimal256``.
    
        Parameters
        ----------
        precision : int
            Must be between 1 and 38
        scale : int
    
        Returns
        -------
        decimal_type : Decimal128Type
    
        Examples
        --------
        Create an instance of decimal type:
    
        >>> import pyarrow as pa
        >>> pa.decimal128(5, 2)
        Decimal128Type(decimal128(5, 2))
    
        Create an array with decimal type:
    
        >>> import decimal
        >>> a = decimal.Decimal('123.45')
        >>> pa.array([a], pa.decimal128(5, 2))
        <pyarrow.lib.Decimal128Array object at ...>
        [
          123.45
        ]
    """
    return DataType

def decimal256(int_precision, int_scale=0): # real signature unknown; restored from __doc__
    """
    decimal256(int precision, int scale=0) -> DataType
    
        Create decimal type with precision and scale and 256-bit width.
    
        Arrow decimals are fixed-point decimal numbers encoded as a scaled
        integer.  The precision is the number of significant digits that the
        decimal type can represent; the scale is the number of digits after
        the decimal point (note the scale can be negative).
    
        For most use cases, the maximum precision offered by ``decimal128``
        is sufficient, and it will result in a more compact and more efficient
        encoding.  ``decimal256`` is useful if you need a precision higher
        than 38 significant digits.
    
        Parameters
        ----------
        precision : int
            Must be between 1 and 76
        scale : int
    
        Returns
        -------
        decimal_type : Decimal256Type
    """
    return DataType

def decompress(buf, decompressed_size=None, codec=None, asbytes=False, memory_pool=None): # real signature unknown; restored from __doc__
    """
    decompress(buf, decompressed_size=None, codec=u'lz4', asbytes=False, memory_pool=None)
    
        Decompress data from buffer-like object.
    
        Parameters
        ----------
        buf : pyarrow.Buffer, bytes, or memoryview-compatible object
            Input object to decompress data from.
        decompressed_size : int, default None
            Size of the decompressed result
        codec : str, default 'lz4'
            Compression codec.
            Supported types: {'brotli, 'gzip', 'lz4', 'lz4_raw', 'snappy', 'zstd'}
        asbytes : bool, default False
            Return result as Python bytes object, otherwise Buffer.
        memory_pool : MemoryPool, default None
            Memory pool to use for buffer allocations, if any.
    
        Returns
        -------
        uncompressed : pyarrow.Buffer or bytes (if asbytes=True)
    """
    pass

def default_memory_pool(): # real signature unknown; restored from __doc__
    """
    default_memory_pool()
    
        Return the process-global memory pool.
    
        Examples
        --------
        >>> default_memory_pool()
        <pyarrow.MemoryPool backend_name=... bytes_allocated=0 max_memory=...>
    """
    pass

def dense_union(child_fields, type_codes=None): # real signature unknown; restored from __doc__
    """
    dense_union(child_fields, type_codes=None)
    
        Create DenseUnionType from child fields.
    
        A dense union is a nested type where each logical value is taken from
        a single child, at a specific offset.  A buffer of 8-bit type ids
        indicates which child a given logical value is to be taken from,
        and a buffer of 32-bit offsets indicates at which physical position
        in the given child array the logical value is to be taken from.
    
        Unlike a sparse union, a dense union allows encoding only the child array
        values which are actually referred to by the union array.  This is
        counterbalanced by the additional footprint of the offsets buffer, and
        the additional indirection cost when looking up values.
    
        Parameters
        ----------
        child_fields : sequence of Field values
            Each field must have a UTF8-encoded name, and these field names are
            part of the type metadata.
        type_codes : list of integers, default None
    
        Returns
        -------
        type : DenseUnionType
    """
    pass

def dictionary(index_type, value_type, bool_ordered=False): # real signature unknown; restored from __doc__
    """
    dictionary(index_type, value_type, bool ordered=False) -> DictionaryType
    
        Dictionary (categorical, or simply encoded) type.
    
        Parameters
        ----------
        index_type : DataType
        value_type : DataType
        ordered : bool
    
        Returns
        -------
        type : DictionaryType
    
        Examples
        --------
        Create an instance of dictionary type:
    
        >>> import pyarrow as pa
        >>> pa.dictionary(pa.int64(), pa.utf8())
        DictionaryType(dictionary<values=string, indices=int64, ordered=0>)
    
        Use dictionary type to create an array:
    
        >>> pa.array(["a", "b", None, "d"], pa.dictionary(pa.int64(), pa.utf8()))
        <pyarrow.lib.DictionaryArray object at ...>
        ...
        -- dictionary:
          [
            "a",
            "b",
            "d"
          ]
        -- indices:
          [
            0,
            1,
            null,
            2
          ]
    """
    return DictionaryType

def duration(unit): # real signature unknown; restored from __doc__
    """
    duration(unit)
    
        Create instance of a duration type with unit resolution.
    
        Parameters
        ----------
        unit : str
            One of 's' [second], 'ms' [millisecond], 'us' [microsecond], or
            'ns' [nanosecond].
    
        Returns
        -------
        type : pyarrow.DurationType
    
        Examples
        --------
        Create an instance of duration type:
    
        >>> import pyarrow as pa
        >>> pa.duration('us')
        DurationType(duration[us])
        >>> pa.duration('s')
        DurationType(duration[s])
    
        Create an array with duration type:
    
        >>> pa.array([0, 1, 2], type=pa.duration('s'))
        <pyarrow.lib.DurationArray object at ...>
        [
          0,
          1,
          2
        ]
    """
    pass

def enable_signal_handlers(bool_enable): # real signature unknown; restored from __doc__
    """
    enable_signal_handlers(bool enable)
    
        Enable or disable interruption of long-running operations.
    
        By default, certain long running operations will detect user
        interruptions, such as by pressing Ctrl-C.  This detection relies
        on setting a signal handler for the duration of the long-running
        operation, and may therefore interfere with other frameworks or
        libraries (such as an event loop).
    
        Parameters
        ----------
        enable : bool
            Whether to enable user interruption by setting a temporary
            signal handler.
    """
    pass

def encode_file_path(path): # real signature unknown; restored from __doc__
    """ encode_file_path(path) """
    pass

def ensure_metadata(meta, bool_allow_none=False): # real signature unknown; restored from __doc__
    """ ensure_metadata(meta, bool allow_none=False) -> KeyValueMetadata """
    return KeyValueMetadata

def ensure_type(ty, bool_allow_none=False): # real signature unknown; restored from __doc__
    """ ensure_type(ty, bool allow_none=False) -> DataType """
    return DataType

def field(name, type, bool_nullable=True, metadata=None): # real signature unknown; restored from __doc__
    """
    field(name, type, bool nullable=True, metadata=None)
    
        Create a pyarrow.Field instance.
    
        Parameters
        ----------
        name : str or bytes
            Name of the field.
        type : pyarrow.DataType
            Arrow datatype of the field.
        nullable : bool, default True
            Whether the field's values are nullable.
        metadata : dict, default None
            Optional field metadata, the keys and values must be coercible to
            bytes.
    
        Returns
        -------
        field : pyarrow.Field
    
        Examples
        --------
        Create an instance of pyarrow.Field:
    
        >>> import pyarrow as pa
        >>> pa.field('key', pa.int32())
        pyarrow.Field<key: int32>
        >>> pa.field('key', pa.int32(), nullable=False)
        pyarrow.Field<key: int32 not null>
    
        >>> field = pa.field('key', pa.int32(),
        ...                  metadata={"key": "Something important"})
        >>> field
        pyarrow.Field<key: int32>
        >>> field.metadata
        {b'key': b'Something important'}
    
        Use the field to create a struct type:
    
        >>> pa.struct([field])
        StructType(struct<key: int32>)
    """
    pass

def fixed_shape_tensor(DataType_value_type, shape, dim_names=None, permutation=None): # real signature unknown; restored from __doc__
    """
    fixed_shape_tensor(DataType value_type, shape, dim_names=None, permutation=None)
    
        Create instance of fixed shape tensor extension type with shape and optional
        names of tensor dimensions and indices of the desired logical
        ordering of dimensions.
    
        Parameters
        ----------
        value_type : DataType
            Data type of individual tensor elements.
        shape : tuple or list of integers
            The physical shape of the contained tensors.
        dim_names : tuple or list of strings, default None
            Explicit names to tensor dimensions.
        permutation : tuple or list integers, default None
            Indices of the desired ordering of the original dimensions.
            The indices contain a permutation of the values ``[0, 1, .., N-1]`` where
            N is the number of dimensions. The permutation indicates which dimension
            of the logical layout corresponds to which dimension of the physical tensor.
            For more information on this parameter see
            :ref:`fixed_shape_tensor_extension`.
    
        Examples
        --------
        Create an instance of fixed shape tensor extension type:
    
        >>> import pyarrow as pa
        >>> tensor_type = pa.fixed_shape_tensor(pa.int32(), [2, 2])
        >>> tensor_type
        FixedShapeTensorType(extension<arrow.fixed_shape_tensor[value_type=int32, shape=[2,2]]>)
    
        Inspect the data type:
    
        >>> tensor_type.value_type
        DataType(int32)
        >>> tensor_type.shape
        [2, 2]
    
        Create a table with fixed shape tensor extension array:
    
        >>> arr = [[1, 2, 3, 4], [10, 20, 30, 40], [100, 200, 300, 400]]
        >>> storage = pa.array(arr, pa.list_(pa.int32(), 4))
        >>> tensor = pa.ExtensionArray.from_storage(tensor_type, storage)
        >>> pa.table([tensor], names=["tensor_array"])
        pyarrow.Table
        tensor_array: extension<arrow.fixed_shape_tensor[value_type=int32, shape=[2,2]]>
        ----
        tensor_array: [[[1,2,3,4],[10,20,30,40],[100,200,300,400]]]
    
        Create an instance of fixed shape tensor extension type with names
        of tensor dimensions:
    
        >>> tensor_type = pa.fixed_shape_tensor(pa.int8(), (2, 2, 3),
        ...                                     dim_names=['C', 'H', 'W'])
        >>> tensor_type.dim_names
        ['C', 'H', 'W']
    
        Create an instance of fixed shape tensor extension type with
        permutation:
    
        >>> tensor_type = pa.fixed_shape_tensor(pa.int8(), (2, 2, 3),
        ...                                     permutation=[0, 2, 1])
        >>> tensor_type.permutation
        [0, 2, 1]
    
        Returns
        -------
        type : FixedShapeTensorType
    """
    pass

def float16(): # real signature unknown; restored from __doc__
    """
    float16()
    
        Create half-precision floating point type.
    
        Examples
        --------
        Create an instance of float16 type:
    
        >>> import pyarrow as pa
        >>> pa.float16()
        DataType(halffloat)
        >>> print(pa.float16())
        halffloat
    
        Create an array with float16 type:
    
        >>> arr = np.array([1.5, np.nan], dtype=np.float16)
        >>> a = pa.array(arr, type=pa.float16())
        >>> a
        <pyarrow.lib.HalfFloatArray object at ...>
        [
          15872,
          32256
        ]
        >>> a.to_pylist()
        [1.5, nan]
    """
    pass

def float32(): # real signature unknown; restored from __doc__
    """
    float32()
    
        Create single-precision floating point type.
    
        Examples
        --------
        Create an instance of float32 type:
    
        >>> import pyarrow as pa
        >>> pa.float32()
        DataType(float)
        >>> print(pa.float32())
        float
    
        Create an array with float32 type:
    
        >>> pa.array([0.0, 1.0, 2.0], type=pa.float32())
        <pyarrow.lib.FloatArray object at ...>
        [
          0,
          1,
          2
        ]
    """
    pass

def float64(): # real signature unknown; restored from __doc__
    """
    float64()
    
        Create double-precision floating point type.
    
        Examples
        --------
        Create an instance of float64 type:
    
        >>> import pyarrow as pa
        >>> pa.float64()
        DataType(double)
        >>> print(pa.float64())
        double
    
        Create an array with float64 type:
    
        >>> pa.array([0.0, 1.0, 2.0], type=pa.float64())
        <pyarrow.lib.DoubleArray object at ...>
        [
          0,
          1,
          2
        ]
    """
    pass

def foreign_buffer(address, size, base=None): # real signature unknown; restored from __doc__
    """
    foreign_buffer(address, size, base=None)
    
        Construct an Arrow buffer with the given *address* and *size*.
    
        The buffer will be optionally backed by the Python *base* object, if given.
        The *base* object will be kept alive as long as this buffer is alive,
        including across language boundaries (for example if the buffer is
        referenced by C++ code).
    
        Parameters
        ----------
        address : int
            The starting address of the buffer. The address can
            refer to both device or host memory but it must be
            accessible from device after mapping it with
            `get_device_address` method.
        size : int
            The size of device buffer in bytes.
        base : {None, object}
            Object that owns the referenced memory.
    """
    pass

def frombytes(o, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    frombytes(o, *, safe=False)
    
        Decode the given bytestring to unicode.
    
        Parameters
        ----------
        o : bytes-like
            Input object.
        safe : bool, default False
            If true, raise on encoding errors.
    """
    pass

def from_numpy_dtype(dtype): # real signature unknown; restored from __doc__
    """
    from_numpy_dtype(dtype)
    
        Convert NumPy dtype to pyarrow.DataType.
    
        Parameters
        ----------
        dtype : the numpy dtype to convert
    
    
        Examples
        --------
        Create a pyarrow DataType from NumPy dtype:
    
        >>> import pyarrow as pa
        >>> import numpy as np
        >>> pa.from_numpy_dtype(np.dtype('float16'))
        DataType(halffloat)
        >>> pa.from_numpy_dtype('U')
        DataType(string)
        >>> pa.from_numpy_dtype(bool)
        DataType(bool)
        >>> pa.from_numpy_dtype(np.str_)
        DataType(string)
    """
    pass

def get_record_batch_size(RecordBatch_batch): # real signature unknown; restored from __doc__
    """
    get_record_batch_size(RecordBatch batch)
    
        Return total size of serialized RecordBatch including metadata and padding.
    
        Parameters
        ----------
        batch : RecordBatch
            The recordbatch for which we want to know the size.
    """
    pass

def get_tensor_size(Tensor_tensor): # real signature unknown; restored from __doc__
    """
    get_tensor_size(Tensor tensor)
    
        Return total size of serialized Tensor including metadata and padding.
    
        Parameters
        ----------
        tensor : Tensor
            The tensor for which we want to known the size.
    """
    pass

def infer_type(values, mask=None, from_pandas=False): # real signature unknown; restored from __doc__
    """
    infer_type(values, mask=None, from_pandas=False)
    
        Attempt to infer Arrow data type that can hold the passed Python
        sequence type in an Array object
    
        Parameters
        ----------
        values : array-like
            Sequence to infer type from.
        mask : ndarray (bool type), optional
            Optional exclusion mask where True marks null, False non-null.
        from_pandas : bool, default False
            Use pandas's NA/null sentinel values for type inference.
    
        Returns
        -------
        type : DataType
    """
    pass

def input_stream(source, compression=None, buffer_size=None): # real signature unknown; restored from __doc__
    """
    input_stream(source, compression=u'detect', buffer_size=None)
    
        Create an Arrow input stream.
    
        Parameters
        ----------
        source : str, Path, buffer, or file-like object
            The source to open for reading.
        compression : str optional, default 'detect'
            The compression algorithm to use for on-the-fly decompression.
            If "detect" and source is a file path, then compression will be
            chosen based on the file extension.
            If None, no compression will be applied.
            Otherwise, a well-known algorithm name must be supplied (e.g. "gzip").
        buffer_size : int, default None
            If None or 0, no buffering will happen. Otherwise the size of the
            temporary read buffer.
    
        Examples
        --------
        Create a readable BufferReader (NativeFile) from a Buffer or a memoryview object:
    
        >>> import pyarrow as pa
        >>> buf = memoryview(b"some data")
        >>> with pa.input_stream(buf) as stream:
        ...     stream.read(4)
        ...
        b'some'
    
        Create a readable OSFile (NativeFile) from a string or file path:
    
        >>> import gzip
        >>> with gzip.open('example.gz', 'wb') as f:
        ...     f.write(b'some data')
        ...
        9
        >>> with pa.input_stream('example.gz') as stream:
        ...     stream.read()
        ...
        b'some data'
    
        Create a readable PythonFile (NativeFile) from a a Python file object:
    
        >>> with open('example.txt', mode='w') as f:
        ...     f.write('some text')
        ...
        9
        >>> with pa.input_stream('example.txt') as stream:
        ...     stream.read(6)
        ...
        b'some t'
    """
    pass

def int16(): # real signature unknown; restored from __doc__
    """
    int16()
    
        Create instance of signed int16 type.
    
        Examples
        --------
        Create an instance of int16 type:
    
        >>> import pyarrow as pa
        >>> pa.int16()
        DataType(int16)
        >>> print(pa.int16())
        int16
    
        Create an array with int16 type:
    
        >>> pa.array([0, 1, 2], type=pa.int16())
        <pyarrow.lib.Int16Array object at ...>
        [
          0,
          1,
          2
        ]
    """
    pass

def int32(): # real signature unknown; restored from __doc__
    """
    int32()
    
        Create instance of signed int32 type.
    
        Examples
        --------
        Create an instance of int32 type:
    
        >>> import pyarrow as pa
        >>> pa.int32()
        DataType(int32)
        >>> print(pa.int32())
        int32
    
        Create an array with int32 type:
    
        >>> pa.array([0, 1, 2], type=pa.int32())
        <pyarrow.lib.Int32Array object at ...>
        [
          0,
          1,
          2
        ]
    """
    pass

def int64(): # real signature unknown; restored from __doc__
    """
    int64()
    
        Create instance of signed int64 type.
    
        Examples
        --------
        Create an instance of int64 type:
    
        >>> import pyarrow as pa
        >>> pa.int64()
        DataType(int64)
        >>> print(pa.int64())
        int64
    
        Create an array with int64 type:
    
        >>> pa.array([0, 1, 2], type=pa.int64())
        <pyarrow.lib.Int64Array object at ...>
        [
          0,
          1,
          2
        ]
    """
    pass

def int8(): # real signature unknown; restored from __doc__
    """
    int8()
    
        Create instance of signed int8 type.
    
        Examples
        --------
        Create an instance of int8 type:
    
        >>> import pyarrow as pa
        >>> pa.int8()
        DataType(int8)
        >>> print(pa.int8())
        int8
    
        Create an array with int8 type:
    
        >>> pa.array([0, 1, 2], type=pa.int8())
        <pyarrow.lib.Int8Array object at ...>
        [
          0,
          1,
          2
        ]
    """
    pass

def io_thread_count(): # real signature unknown; restored from __doc__
    """
    io_thread_count()
    
        Return the number of threads to use for I/O operations.
    
        Many operations, such as scanning a dataset, will implicitly make
        use of this pool. The number of threads is set to a fixed value at
        startup. It can be modified at runtime by calling
        :func:`set_io_thread_count()`.
    
        See Also
        --------
        set_io_thread_count : Modify the size of this pool.
        cpu_count : The analogous function for the CPU thread pool.
    """
    pass

def is_boolean_value(obj): # real signature unknown; restored from __doc__
    """
    is_boolean_value(obj)
    
        Check if the object is a boolean.
    
        Parameters
        ----------
        obj : object
            The object to check
    """
    pass

def is_float_value(obj): # real signature unknown; restored from __doc__
    """
    is_float_value(obj)
    
        Check if the object is a float.
    
        Parameters
        ----------
        obj : object
            The object to check
    """
    pass

def is_integer_value(obj): # real signature unknown; restored from __doc__
    """
    is_integer_value(obj)
    
        Check if the object is an integer.
    
        Parameters
        ----------
        obj : object
            The object to check
    """
    pass

def jemalloc_memory_pool(): # real signature unknown; restored from __doc__
    """
    jemalloc_memory_pool()
    
        Return a memory pool based on the jemalloc heap.
    
        NotImplementedError is raised if jemalloc support is not enabled.
    """
    pass

def jemalloc_set_decay_ms(decay_ms): # real signature unknown; restored from __doc__
    """
    jemalloc_set_decay_ms(decay_ms)
    
        Set arenas.dirty_decay_ms and arenas.muzzy_decay_ms to indicated number of
        milliseconds. A value of 0 (the default) results in dirty / muzzy memory
        pages being released right away to the OS, while a higher value will result
        in a time-based decay. See the jemalloc docs for more information
    
        It's best to set this at the start of your application.
    
        Parameters
        ----------
        decay_ms : int
            Number of milliseconds to set for jemalloc decay conf parameters. Note
            that this change will only affect future memory arenas
    """
    pass

def large_binary(): # real signature unknown; restored from __doc__
    """
    large_binary()
    
        Create large variable-length binary type.
    
        This data type may not be supported by all Arrow implementations.  Unless
        you need to represent data larger than 2GB, you should prefer binary().
    
        Examples
        --------
        Create an instance of large variable-length binary type:
    
        >>> import pyarrow as pa
        >>> pa.large_binary()
        DataType(large_binary)
    
        and use the type to create an array:
    
        >>> pa.array(['foo', 'bar', 'baz'], type=pa.large_binary())
        <pyarrow.lib.LargeBinaryArray object at ...>
        [
          666F6F,
          626172,
          62617A
        ]
    """
    pass

def large_list(value_type): # real signature unknown; restored from __doc__
    """
    large_list(value_type) -> LargeListType
    
        Create LargeListType instance from child data type or field.
    
        This data type may not be supported by all Arrow implementations.
        Unless you need to represent data larger than 2**31 elements, you should
        prefer list_().
    
        Parameters
        ----------
        value_type : DataType or Field
    
        Returns
        -------
        list_type : DataType
    
        Examples
        --------
        Create an instance of LargeListType:
    
        >>> import pyarrow as pa
        >>> pa.large_list(pa.int8())
        LargeListType(large_list<item: int8>)
    
        Use the LargeListType to create an array:
    
        >>> pa.array([[-1, 3]] * 5, type=pa.large_list(pa.int8()))
        <pyarrow.lib.LargeListArray object at ...>
        [
          [
            -1,
            3
          ],
          [
            -1,
            3
          ],
        ...
    """
    return LargeListType

def large_string(): # real signature unknown; restored from __doc__
    """
    large_string()
    
        Create large UTF8 variable-length string type.
    
        This data type may not be supported by all Arrow implementations.  Unless
        you need to represent data larger than 2GB, you should prefer string().
    
        Examples
        --------
        Create an instance of large UTF8 variable-length binary type:
    
        >>> import pyarrow as pa
        >>> pa.large_string()
        DataType(large_string)
    
        and use the type to create an array:
    
        >>> pa.array(['foo', 'bar'] * 50, type=pa.large_string())
        <pyarrow.lib.LargeStringArray object at ...>
        [
          "foo",
          "bar",
          ...
          "foo",
          "bar"
        ]
    """
    pass

def large_utf8(): # real signature unknown; restored from __doc__
    """
    large_utf8()
    
        Alias for large_string().
    
        Examples
        --------
        Create an instance of large UTF8 variable-length binary type:
    
        >>> import pyarrow as pa
        >>> pa.large_utf8()
        DataType(large_string)
    
        and use the type to create an array:
    
        >>> pa.array(['foo', 'bar'] * 50, type=pa.large_utf8())
        <pyarrow.lib.LargeStringArray object at ...>
        [
          "foo",
          "bar",
          ...
          "foo",
          "bar"
        ]
    """
    pass

def list_(value_type, int_list_size=-1): # real signature unknown; restored from __doc__
    """
    list_(value_type, int list_size=-1)
    
        Create ListType instance from child data type or field.
    
        Parameters
        ----------
        value_type : DataType or Field
        list_size : int, optional, default -1
            If length == -1 then return a variable length list type. If length is
            greater than or equal to 0 then return a fixed size list type.
    
        Returns
        -------
        list_type : DataType
    
        Examples
        --------
        Create an instance of ListType:
    
        >>> import pyarrow as pa
        >>> pa.list_(pa.string())
        ListType(list<item: string>)
        >>> pa.list_(pa.int32(), 2)
        FixedSizeListType(fixed_size_list<item: int32>[2])
    
        Use the ListType to create a scalar:
    
        >>> pa.scalar(['foo', None], type=pa.list_(pa.string(), 2))
        <pyarrow.FixedSizeListScalar: ['foo', None]>
    
        or an array:
    
        >>> pa.array([[1, 2], [3, 4]], pa.list_(pa.int32(), 2))
        <pyarrow.lib.FixedSizeListArray object at ...>
        [
          [
            1,
            2
          ],
          [
            3,
            4
          ]
        ]
    """
    pass

def logging_memory_pool(MemoryPool_parent): # real signature unknown; restored from __doc__
    """
    logging_memory_pool(MemoryPool parent)
    
        Create and return a MemoryPool instance that redirects to the
        *parent*, but also dumps allocation logs on stderr.
    
        Parameters
        ----------
        parent : MemoryPool
            The real memory pool that should be used for allocations.
    """
    pass

def log_memory_allocations(enable=True): # real signature unknown; restored from __doc__
    """
    log_memory_allocations(enable=True)
    
        Enable or disable memory allocator logging for debugging purposes
    
        Parameters
        ----------
        enable : bool, default True
            Pass False to disable logging
    """
    pass

def map_(key_type, item_type, keys_sorted=False): # real signature unknown; restored from __doc__
    """
    map_(key_type, item_type, keys_sorted=False) -> MapType
    
        Create MapType instance from key and item data types or fields.
    
        Parameters
        ----------
        key_type : DataType or Field
        item_type : DataType or Field
        keys_sorted : bool
    
        Returns
        -------
        map_type : DataType
    
        Examples
        --------
        Create an instance of MapType:
    
        >>> import pyarrow as pa
        >>> pa.map_(pa.string(), pa.int32())
        MapType(map<string, int32>)
        >>> pa.map_(pa.string(), pa.int32(), keys_sorted=True)
        MapType(map<string, int32, keys_sorted>)
    
        Use MapType to create an array:
    
        >>> data = [[{'key': 'a', 'value': 1}, {'key': 'b', 'value': 2}], [{'key': 'c', 'value': 3}]]
        >>> pa.array(data, type=pa.map_(pa.string(), pa.int32(), keys_sorted=True))
        <pyarrow.lib.MapArray object at ...>
        [
          keys:
          [
            "a",
            "b"
          ]
          values:
          [
            1,
            2
          ],
          keys:
          [
            "c"
          ]
          values:
          [
            3
          ]
        ]
    """
    return MapType

def memory_map(path, mode=None): # real signature unknown; restored from __doc__
    """
    memory_map(path, mode=u'r')
    
        Open memory map at file path. Size of the memory map cannot change.
    
        Parameters
        ----------
        path : str
        mode : {'r', 'r+', 'w'}, default 'r'
            Whether the file is opened for reading ('r'), writing ('w')
            or both ('r+').
    
        Returns
        -------
        mmap : MemoryMappedFile
    
        Examples
        --------
        Reading from a memory map without any memory allocation or copying:
    
        >>> import pyarrow as pa
        >>> with pa.output_stream('example_mmap.txt') as stream:
        ...     stream.write(b'Constructing a buffer referencing the mapped memory')
        ...
        51
        >>> with pa.memory_map('example_mmap.txt') as mmap:
        ...     mmap.read_at(6,45)
        ...
        b'memory'
    """
    pass

def mimalloc_memory_pool(): # real signature unknown; restored from __doc__
    """
    mimalloc_memory_pool()
    
        Return a memory pool based on the mimalloc heap.
    
        NotImplementedError is raised if mimalloc support is not enabled.
    """
    pass

def month_day_nano_interval(): # real signature unknown; restored from __doc__
    """
    month_day_nano_interval()
    
        Create instance of an interval type representing months, days and
        nanoseconds between two dates.
    
        Examples
        --------
        Create an instance of an month_day_nano_interval type:
    
        >>> import pyarrow as pa
        >>> pa.month_day_nano_interval()
        DataType(month_day_nano_interval)
    
        Create a scalar with month_day_nano_interval type:
    
        >>> pa.scalar((1, 15, -30), type=pa.month_day_nano_interval())
        <pyarrow.MonthDayNanoIntervalScalar: MonthDayNano(months=1, days=15, nanoseconds=-30)>
    """
    pass

def namedtuple(typename, field_names, *, rename=False, defaults=None, module=None): # reliably restored by inspect
    """
    Returns a new subclass of tuple with named fields.
    
        >>> Point = namedtuple('Point', ['x', 'y'])
        >>> Point.__doc__                   # docstring for the new class
        'Point(x, y)'
        >>> p = Point(11, y=22)             # instantiate with positional args or keywords
        >>> p[0] + p[1]                     # indexable like a plain tuple
        33
        >>> x, y = p                        # unpack like a regular tuple
        >>> x, y
        (11, 22)
        >>> p.x + p.y                       # fields also accessible by name
        33
        >>> d = p._asdict()                 # convert to a dictionary
        >>> d['x']
        11
        >>> Point(**d)                      # convert from a dictionary
        Point(x=11, y=22)
        >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
        Point(x=100, y=22)
    """
    pass

def null(): # real signature unknown; restored from __doc__
    """
    null()
    
        Create instance of null type.
    
        Examples
        --------
        Create an instance of a null type:
    
        >>> import pyarrow as pa
        >>> pa.null()
        DataType(null)
        >>> print(pa.null())
        null
    
        Create a ``Field`` type with a null type and a name:
    
        >>> pa.field('null_field', pa.null())
        pyarrow.Field<null_field: null>
    """
    pass

def nulls(size, type=None, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
    """
    nulls(size, type=None, MemoryPool memory_pool=None)
    
        Create a strongly-typed Array instance with all elements null.
    
        Parameters
        ----------
        size : int
            Array length.
        type : pyarrow.DataType, default None
            Explicit type for the array. By default use NullType.
        memory_pool : MemoryPool, default None
            Arrow MemoryPool to use for allocations. Uses the default memory
            pool if not passed.
    
        Returns
        -------
        arr : Array
    
        Examples
        --------
        >>> import pyarrow as pa
        >>> pa.nulls(10)
        <pyarrow.lib.NullArray object at ...>
        10 nulls
    
        >>> pa.nulls(3, pa.uint32())
        <pyarrow.lib.UInt32Array object at ...>
        [
          null,
          null,
          null
        ]
    """
    pass

def output_stream(source, compression=None, buffer_size=None): # real signature unknown; restored from __doc__
    """
    output_stream(source, compression=u'detect', buffer_size=None)
    
        Create an Arrow output stream.
    
        Parameters
        ----------
        source : str, Path, buffer, file-like object
            The source to open for writing.
        compression : str optional, default 'detect'
            The compression algorithm to use for on-the-fly compression.
            If "detect" and source is a file path, then compression will be
            chosen based on the file extension.
            If None, no compression will be applied.
            Otherwise, a well-known algorithm name must be supplied (e.g. "gzip").
        buffer_size : int, default None
            If None or 0, no buffering will happen. Otherwise the size of the
            temporary write buffer.
    
        Examples
        --------
        Create a writable NativeFile from a pyarrow Buffer:
    
        >>> import pyarrow as pa
        >>> data = b"buffer data"
        >>> empty_obj = bytearray(11)
        >>> buf = pa.py_buffer(empty_obj)
        >>> with pa.output_stream(buf) as stream:
        ...     stream.write(data)
        ...
        11
        >>> with pa.input_stream(buf) as stream:
        ...     stream.read(6)
        ...
        b'buffer'
    
        or from a memoryview object:
    
        >>> buf = memoryview(empty_obj)
        >>> with pa.output_stream(buf) as stream:
        ...     stream.write(data)
        ...
        11
        >>> with pa.input_stream(buf) as stream:
        ...     stream.read()
        ...
        b'buffer data'
    
        Create a writable NativeFile from a string or file path:
    
        >>> with pa.output_stream('example_second.txt') as stream:
        ...     stream.write(b'Write some data')
        ...
        15
        >>> with pa.input_stream('example_second.txt') as stream:
        ...     stream.read()
        ...
        b'Write some data'
    """
    pass

def proxy_memory_pool(MemoryPool_parent): # real signature unknown; restored from __doc__
    """
    proxy_memory_pool(MemoryPool parent)
    
        Create and return a MemoryPool instance that redirects to the
        *parent*, but with separate allocation statistics.
    
        Parameters
        ----------
        parent : MemoryPool
            The real memory pool that should be used for allocations.
    """
    pass

def py_buffer(obj): # real signature unknown; restored from __doc__
    """
    py_buffer(obj)
    
        Construct an Arrow buffer from a Python bytes-like or buffer-like object
    
        Parameters
        ----------
        obj : object
            the object from which the buffer should be constructed.
    """
    pass

def read_message(source): # real signature unknown; restored from __doc__
    """
    read_message(source)
    
        Read length-prefixed message from file or buffer-like object
    
        Parameters
        ----------
        source : pyarrow.NativeFile, file-like object, or buffer-like object
    
        Returns
        -------
        message : Message
    """
    pass

def read_record_batch(obj, Schema_schema, DictionaryMemo_dictionary_memo=None): # real signature unknown; restored from __doc__
    """
    read_record_batch(obj, Schema schema, DictionaryMemo dictionary_memo=None)
    
        Read RecordBatch from message, given a known schema. If reading data from a
        complete IPC stream, use ipc.open_stream instead
    
        Parameters
        ----------
        obj : Message or Buffer-like
        schema : Schema
        dictionary_memo : DictionaryMemo, optional
            If message contains dictionaries, must pass a populated
            DictionaryMemo
    
        Returns
        -------
        batch : RecordBatch
    """
    pass

def read_schema(obj, DictionaryMemo_dictionary_memo=None): # real signature unknown; restored from __doc__
    """
    read_schema(obj, DictionaryMemo dictionary_memo=None)
    
        Read Schema from message or buffer
    
        Parameters
        ----------
        obj : buffer or Message
        dictionary_memo : DictionaryMemo, optional
            Needed to be able to reconstruct dictionary-encoded fields
            with read_record_batch
    
        Returns
        -------
        schema : Schema
    """
    pass

def read_tensor(source): # real signature unknown; restored from __doc__
    """
    read_tensor(source)
    Read pyarrow.Tensor from pyarrow.NativeFile object from current
        position. If the file source supports zero copy (e.g. a memory map), then
        this operation does not allocate any memory. This function not assume that
        the stream is aligned
    
        Parameters
        ----------
        source : pyarrow.NativeFile
    
        Returns
        -------
        tensor : Tensor
    """
    pass

def record_batch(data, names=None, schema=None, metadata=None): # real signature unknown; restored from __doc__
    """
    record_batch(data, names=None, schema=None, metadata=None)
    
        Create a pyarrow.RecordBatch from another Python data structure or sequence
        of arrays.
    
        Parameters
        ----------
        data : pandas.DataFrame, list, Arrow-compatible table
            A DataFrame, list of arrays or chunked arrays, or a tabular object
            implementing the Arrow PyCapsule Protocol (has an
            ``__arrow_c_array__`` method).
        names : list, default None
            Column names if list of arrays passed as data. Mutually exclusive with
            'schema' argument.
        schema : Schema, default None
            The expected schema of the RecordBatch. If not passed, will be inferred
            from the data. Mutually exclusive with 'names' argument.
        metadata : dict or Mapping, default None
            Optional metadata for the schema (if schema not passed).
    
        Returns
        -------
        RecordBatch
    
        See Also
        --------
        RecordBatch.from_arrays, RecordBatch.from_pandas, table
    
        Examples
        --------
        >>> import pyarrow as pa
        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
        >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
        >>> names = ["n_legs", "animals"]
    
        Creating a RecordBatch from a list of arrays with names:
    
        >>> pa.record_batch([n_legs, animals], names=names)
        pyarrow.RecordBatch
        n_legs: int64
        animals: string
        ----
        n_legs: [2,2,4,4,5,100]
        animals: ["Flamingo","Parrot","Dog","Horse","Brittle stars","Centipede"]
        >>> pa.record_batch([n_legs, animals], names=["n_legs", "animals"]).to_pandas()
           n_legs        animals
        0       2       Flamingo
        1       2         Parrot
        2       4            Dog
        3       4          Horse
        4       5  Brittle stars
        5     100      Centipede
    
        Creating a RecordBatch from a list of arrays with names and metadata:
    
        >>> my_metadata={"n_legs": "How many legs does an animal have?"}
        >>> pa.record_batch([n_legs, animals],
        ...                  names=names,
        ...                  metadata = my_metadata)
        pyarrow.RecordBatch
        n_legs: int64
        animals: string
        ----
        n_legs: [2,2,4,4,5,100]
        animals: ["Flamingo","Parrot","Dog","Horse","Brittle stars","Centipede"]
        >>> pa.record_batch([n_legs, animals],
        ...                  names=names,
        ...                  metadata = my_metadata).schema
        n_legs: int64
        animals: string
        -- schema metadata --
        n_legs: 'How many legs does an animal have?'
    
        Creating a RecordBatch from a pandas DataFrame:
    
        >>> import pandas as pd
        >>> df = pd.DataFrame({'year': [2020, 2022, 2021, 2022],
        ...                    'month': [3, 5, 7, 9],
        ...                    'day': [1, 5, 9, 13],
        ...                    'n_legs': [2, 4, 5, 100],
        ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
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
    
        >>> pa.record_batch(df).to_pandas()
           year  month  day  n_legs        animals
        0  2020      3    1       2       Flamingo
        1  2022      5    5       4          Horse
        2  2021      7    9       5  Brittle stars
        3  2022      9   13     100      Centipede
    
        Creating a RecordBatch from a pandas DataFrame with schema:
    
        >>> my_schema = pa.schema([
        ...     pa.field('n_legs', pa.int64()),
        ...     pa.field('animals', pa.string())],
        ...     metadata={"n_legs": "Number of legs per animal"})
        >>> pa.record_batch(df, my_schema).schema
        n_legs: int64
        animals: string
        -- schema metadata --
        n_legs: 'Number of legs per animal'
        pandas: ...
        >>> pa.record_batch(df, my_schema).to_pandas()
           n_legs        animals
        0       2       Flamingo
        1       4          Horse
        2       5  Brittle stars
        3     100      Centipede
    """
    pass

def register_extension_type(ext_type): # real signature unknown; restored from __doc__
    """
    register_extension_type(ext_type)
    
        Register a Python extension type.
    
        Registration is based on the extension name (so different registered types
        need unique extension names). Registration needs an extension type
        instance, but then works for any instance of the same subclass regardless
        of parametrization of the type.
    
        Parameters
        ----------
        ext_type : BaseExtensionType instance
            The ExtensionType subclass to register.
    
        Examples
        --------
        Define a UuidType extension type subclassing ExtensionType:
    
        >>> import pyarrow as pa
        >>> class UuidType(pa.ExtensionType):
        ...    def __init__(self):
        ...       pa.ExtensionType.__init__(self, pa.binary(16), "my_package.uuid")
        ...    def __arrow_ext_serialize__(self):
        ...       # since we don't have a parameterized type, we don't need extra
        ...       # metadata to be deserialized
        ...       return b''
        ...    @classmethod
        ...    def __arrow_ext_deserialize__(self, storage_type, serialized):
        ...       # return an instance of this subclass given the serialized
        ...       # metadata.
        ...       return UuidType()
        ...
    
        Register the extension type:
    
        >>> pa.register_extension_type(UuidType())
    
        Unregister the extension type:
    
        >>> pa.unregister_extension_type("my_package.uuid")
    """
    pass

def repeat(value, size, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
    """
    repeat(value, size, MemoryPool memory_pool=None)
    
        Create an Array instance whose slots are the given scalar.
    
        Parameters
        ----------
        value : Scalar-like object
            Either a pyarrow.Scalar or any python object coercible to a Scalar.
        size : int
            Number of times to repeat the scalar in the output Array.
        memory_pool : MemoryPool, default None
            Arrow MemoryPool to use for allocations. Uses the default memory
            pool if not passed.
    
        Returns
        -------
        arr : Array
    
        Examples
        --------
        >>> import pyarrow as pa
        >>> pa.repeat(10, 3)
        <pyarrow.lib.Int64Array object at ...>
        [
          10,
          10,
          10
        ]
    
        >>> pa.repeat([1, 2], 2)
        <pyarrow.lib.ListArray object at ...>
        [
          [
            1,
            2
          ],
          [
            1,
            2
          ]
        ]
    
        >>> pa.repeat("string", 3)
        <pyarrow.lib.StringArray object at ...>
        [
          "string",
          "string",
          "string"
        ]
    
        >>> pa.repeat(pa.scalar({'a': 1, 'b': [1, 2]}), 2)
        <pyarrow.lib.StructArray object at ...>
        -- is_valid: all not null
        -- child 0 type: int64
          [
            1,
            1
          ]
        -- child 1 type: list<item: int64>
          [
            [
              1,
              2
            ],
            [
              1,
              2
            ]
          ]
    """
    pass

def runtime_info(): # real signature unknown; restored from __doc__
    """
    runtime_info()
    
        Get runtime information.
    
        Returns
        -------
        info : pyarrow.RuntimeInfo
    """
    pass

def run_end_encoded(run_end_type, value_type): # real signature unknown; restored from __doc__
    """
    run_end_encoded(run_end_type, value_type)
    
        Create RunEndEncodedType from run-end and value types.
    
        Parameters
        ----------
        run_end_type : pyarrow.DataType
            The integer type of the run_ends array. Must be 'int16', 'int32', or 'int64'.
        value_type : pyarrow.DataType
            The type of the values array.
    
        Returns
        -------
        type : RunEndEncodedType
    """
    pass

def scalar(value, type=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    scalar(value, type=None, *, from_pandas=None, MemoryPool memory_pool=None)
    
        Create a pyarrow.Scalar instance from a Python object.
    
        Parameters
        ----------
        value : Any
            Python object coercible to arrow's type system.
        type : pyarrow.DataType
            Explicit type to attempt to coerce to, otherwise will be inferred from
            the value.
        from_pandas : bool, default None
            Use pandas's semantics for inferring nulls from values in
            ndarray-like data. Defaults to False if not passed explicitly by user,
            or True if a pandas object is passed in.
        memory_pool : pyarrow.MemoryPool, optional
            If not passed, will allocate memory from the currently-set default
            memory pool.
    
        Returns
        -------
        scalar : pyarrow.Scalar
    
        Examples
        --------
        >>> import pyarrow as pa
    
        >>> pa.scalar(42)
        <pyarrow.Int64Scalar: 42>
    
        >>> pa.scalar("string")
        <pyarrow.StringScalar: 'string'>
    
        >>> pa.scalar([1, 2])
        <pyarrow.ListScalar: [1, 2]>
    
        >>> pa.scalar([1, 2], type=pa.list_(pa.int16()))
        <pyarrow.ListScalar: [1, 2]>
    """
    pass

def schema(fields, metadata=None): # real signature unknown; restored from __doc__
    """
    schema(fields, metadata=None)
    
        Construct pyarrow.Schema from collection of fields.
    
        Parameters
        ----------
        fields : iterable of Fields or tuples, or mapping of strings to DataTypes
            Can also pass an object that implements the Arrow PyCapsule Protocol
            for schemas (has an ``__arrow_c_schema__`` method).
        metadata : dict, default None
            Keys and values must be coercible to bytes.
    
        Examples
        --------
        Create a Schema from iterable of tuples:
    
        >>> import pyarrow as pa
        >>> pa.schema([
        ...     ('some_int', pa.int32()),
        ...     ('some_string', pa.string()),
        ...     pa.field('some_required_string', pa.string(), nullable=False)
        ... ])
        some_int: int32
        some_string: string
        some_required_string: string not null
    
        Create a Schema from iterable of Fields:
    
        >>> pa.schema([
        ...     pa.field('some_int', pa.int32()),
        ...     pa.field('some_string', pa.string())
        ... ])
        some_int: int32
        some_string: string
    
        Returns
        -------
        schema : pyarrow.Schema
    """
    pass

def set_cpu_count(int_count): # real signature unknown; restored from __doc__
    """
    set_cpu_count(int count)
    
        Set the number of threads to use in parallel operations.
    
        Parameters
        ----------
        count : int
            The number of concurrent threads that should be used.
    
        See Also
        --------
        cpu_count : Get the size of this pool.
        set_io_thread_count : The analogous function for the I/O thread pool.
    """
    pass

def set_io_thread_count(int_count): # real signature unknown; restored from __doc__
    """
    set_io_thread_count(int count)
    
        Set the number of threads to use for I/O operations.
    
        Many operations, such as scanning a dataset, will implicitly make
        use of this pool.
    
        Parameters
        ----------
        count : int
            The max number of threads that may be used for I/O.
            Must be positive.
    
        See Also
        --------
        io_thread_count : Get the size of this pool.
        set_cpu_count : The analogous function for the CPU thread pool.
    """
    pass

def set_memory_pool(MemoryPool_pool): # real signature unknown; restored from __doc__
    """
    set_memory_pool(MemoryPool pool)
    
        Set the default memory pool.
    
        Parameters
        ----------
        pool : MemoryPool
            The memory pool that should be used by default.
    """
    pass

def set_timezone_db_path(path): # real signature unknown; restored from __doc__
    """
    set_timezone_db_path(path)
    
        Configure the path to text timezone database on Windows.
    
        Parameters
        ----------
        path : str
            Path to text timezone database.
    """
    pass

def sparse_union(child_fields, type_codes=None): # real signature unknown; restored from __doc__
    """
    sparse_union(child_fields, type_codes=None)
    
        Create SparseUnionType from child fields.
    
        A sparse union is a nested type where each logical value is taken from
        a single child.  A buffer of 8-bit type ids indicates which child
        a given logical value is to be taken from.
    
        In a sparse union, each child array should have the same length as the
        union array, regardless of the actual number of union values that
        refer to it.
    
        Parameters
        ----------
        child_fields : sequence of Field values
            Each field must have a UTF8-encoded name, and these field names are
            part of the type metadata.
        type_codes : list of integers, default None
    
        Returns
        -------
        type : SparseUnionType
    """
    pass

def string(): # real signature unknown; restored from __doc__
    """
    string()
    
        Create UTF8 variable-length string type.
    
        Examples
        --------
        Create an instance of a string type:
    
        >>> import pyarrow as pa
        >>> pa.string()
        DataType(string)
    
        and use the string type to create an array:
    
        >>> pa.array(['foo', 'bar', 'baz'], type=pa.string())
        <pyarrow.lib.StringArray object at ...>
        [
          "foo",
          "bar",
          "baz"
        ]
    """
    pass

def string_to_tzinfo(name): # real signature unknown; restored from __doc__
    """
    string_to_tzinfo(name)
    
        Convert a time zone name into a time zone object.
    
        Supported input strings are:
        * As used in the Olson time zone database (the "tz database" or
          "tzdata"), such as "America/New_York"
        * An absolute time zone offset of the form +XX:XX or -XX:XX, such as +07:30
    
        Parameters
        ----------
          name: str
            Time zone name.
    
        Returns
        -------
          tz : datetime.tzinfo
            Time zone object
    """
    pass

def struct(fields): # real signature unknown; restored from __doc__
    """
    struct(fields)
    
        Create StructType instance from fields.
    
        A struct is a nested type parameterized by an ordered sequence of types
        (which can all be distinct), called its fields.
    
        Parameters
        ----------
        fields : iterable of Fields or tuples, or mapping of strings to DataTypes
            Each field must have a UTF8-encoded name, and these field names are
            part of the type metadata.
    
        Examples
        --------
        Create an instance of StructType from an iterable of tuples:
    
        >>> import pyarrow as pa
        >>> fields = [
        ...     ('f1', pa.int32()),
        ...     ('f2', pa.string()),
        ... ]
        >>> struct_type = pa.struct(fields)
        >>> struct_type
        StructType(struct<f1: int32, f2: string>)
    
        Retrieve a field from a StructType:
    
        >>> struct_type[0]
        pyarrow.Field<f1: int32>
        >>> struct_type['f1']
        pyarrow.Field<f1: int32>
    
        Create an instance of StructType from an iterable of Fields:
    
        >>> fields = [
        ...     pa.field('f1', pa.int32()),
        ...     pa.field('f2', pa.string(), nullable=False),
        ... ]
        >>> pa.struct(fields)
        StructType(struct<f1: int32, f2: string not null>)
    
        Returns
        -------
        type : DataType
    """
    pass

def supported_memory_backends(): # real signature unknown; restored from __doc__
    """
    supported_memory_backends()
    
        Return a list of available memory pool backends
    """
    pass

def system_memory_pool(): # real signature unknown; restored from __doc__
    """
    system_memory_pool()
    
        Return a memory pool based on the C malloc heap.
    """
    pass

def table(data, names=None, schema=None, metadata=None, nthreads=None): # real signature unknown; restored from __doc__
    """
    table(data, names=None, schema=None, metadata=None, nthreads=None)
    
        Create a pyarrow.Table from a Python data structure or sequence of arrays.
    
        Parameters
        ----------
        data : pandas.DataFrame, dict, list
            A DataFrame, mapping of strings to Arrays or Python lists, or list of
            arrays or chunked arrays.
        names : list, default None
            Column names if list of arrays passed as data. Mutually exclusive with
            'schema' argument.
        schema : Schema, default None
            The expected schema of the Arrow Table. If not passed, will be inferred
            from the data. Mutually exclusive with 'names' argument.
            If passed, the output will have exactly this schema (raising an error
            when columns are not found in the data and ignoring additional data not
            specified in the schema, when data is a dict or DataFrame).
        metadata : dict or Mapping, default None
            Optional metadata for the schema (if schema not passed).
        nthreads : int, default None
            For pandas.DataFrame inputs: if greater than 1, convert columns to
            Arrow in parallel using indicated number of threads. By default,
            this follows :func:`pyarrow.cpu_count` (may use up to system CPU count
            threads).
    
        Returns
        -------
        Table
    
        See Also
        --------
        Table.from_arrays, Table.from_pandas, Table.from_pydict
    
        Examples
        --------
        >>> import pyarrow as pa
        >>> n_legs = pa.array([2, 4, 5, 100])
        >>> animals = pa.array(["Flamingo", "Horse", "Brittle stars", "Centipede"])
        >>> names = ["n_legs", "animals"]
    
        Construct a Table from arrays:
    
        >>> pa.table([n_legs, animals], names=names)
        pyarrow.Table
        n_legs: int64
        animals: string
        ----
        n_legs: [[2,4,5,100]]
        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]
    
        Construct a Table from arrays with metadata:
    
        >>> my_metadata={"n_legs": "Number of legs per animal"}
        >>> pa.table([n_legs, animals], names=names, metadata = my_metadata).schema
        n_legs: int64
        animals: string
        -- schema metadata --
        n_legs: 'Number of legs per animal'
    
        Construct a Table from pandas DataFrame:
    
        >>> import pandas as pd
        >>> df = pd.DataFrame({'year': [2020, 2022, 2019, 2021],
        ...                    'n_legs': [2, 4, 5, 100],
        ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
        >>> pa.table(df)
        pyarrow.Table
        year: int64
        n_legs: int64
        animals: string
        ----
        year: [[2020,2022,2019,2021]]
        n_legs: [[2,4,5,100]]
        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]
    
        Construct a Table from pandas DataFrame with pyarrow schema:
    
        >>> my_schema = pa.schema([
        ...     pa.field('n_legs', pa.int64()),
        ...     pa.field('animals', pa.string())],
        ...     metadata={"n_legs": "Number of legs per animal"})
        >>> pa.table(df, my_schema).schema
        n_legs: int64
        animals: string
        -- schema metadata --
        n_legs: 'Number of legs per animal'
        pandas: '{"index_columns": [], "column_indexes": [{"name": null, ...
    
        Construct a Table from chunked arrays:
    
        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])
        >>> animals = pa.chunked_array([["Flamingo", "Parrot", "Dog"], ["Horse", "Brittle stars", "Centipede"]])
        >>> table = pa.table([n_legs, animals], names=names)
        >>> table
        pyarrow.Table
        n_legs: int64
        animals: string
        ----
        n_legs: [[2,2,4],[4,5,100]]
        animals: [["Flamingo","Parrot","Dog"],["Horse","Brittle stars","Centipede"]]
    """
    pass

def table_to_blocks(options, Table_table, categories, extension_columns): # real signature unknown; restored from __doc__
    """ table_to_blocks(options, Table table, categories, extension_columns) """
    pass

def time32(unit): # real signature unknown; restored from __doc__
    """
    time32(unit)
    
        Create instance of 32-bit time (time of day) type with unit resolution.
    
        Parameters
        ----------
        unit : str
            one of 's' [second], or 'ms' [millisecond]
    
        Returns
        -------
        type : pyarrow.Time32Type
    
        Examples
        --------
        >>> import pyarrow as pa
        >>> pa.time32('s')
        Time32Type(time32[s])
        >>> pa.time32('ms')
        Time32Type(time32[ms])
    """
    pass

def time64(unit): # real signature unknown; restored from __doc__
    """
    time64(unit)
    
        Create instance of 64-bit time (time of day) type with unit resolution.
    
        Parameters
        ----------
        unit : str
            One of 'us' [microsecond], or 'ns' [nanosecond].
    
        Returns
        -------
        type : pyarrow.Time64Type
    
        Examples
        --------
        >>> import pyarrow as pa
        >>> pa.time64('us')
        Time64Type(time64[us])
        >>> pa.time64('ns')
        Time64Type(time64[ns])
    """
    pass

def timestamp(unit, tz=None): # real signature unknown; restored from __doc__
    """
    timestamp(unit, tz=None)
    
        Create instance of timestamp type with resolution and optional time zone.
    
        Parameters
        ----------
        unit : str
            one of 's' [second], 'ms' [millisecond], 'us' [microsecond], or 'ns'
            [nanosecond]
        tz : str, default None
            Time zone name. None indicates time zone naive
    
        Examples
        --------
        Create an instance of timestamp type:
    
        >>> import pyarrow as pa
        >>> pa.timestamp('us')
        TimestampType(timestamp[us])
        >>> pa.timestamp('s', tz='America/New_York')
        TimestampType(timestamp[s, tz=America/New_York])
        >>> pa.timestamp('s', tz='+07:30')
        TimestampType(timestamp[s, tz=+07:30])
    
        Use timestamp type when creating a scalar object:
    
        >>> from datetime import datetime
        >>> pa.scalar(datetime(2012, 1, 1), type=pa.timestamp('s', tz='UTC'))
        <pyarrow.TimestampScalar: '2012-01-01T00:00:00+0000'>
        >>> pa.scalar(datetime(2012, 1, 1), type=pa.timestamp('us'))
        <pyarrow.TimestampScalar: '2012-01-01T00:00:00.000000'>
    
        Returns
        -------
        timestamp_type : TimestampType
    """
    pass

def tobytes(o): # real signature unknown; restored from __doc__
    """
    tobytes(o)
    
        Encode a unicode or bytes string to bytes.
    
        Parameters
        ----------
        o : str or bytes
            Input string.
    """
    pass

def total_allocated_bytes(): # real signature unknown; restored from __doc__
    """
    total_allocated_bytes()
    
        Return the currently allocated bytes from the default memory pool.
        Other memory pools may not be accounted for.
    """
    pass

def transcoding_input_stream(stream, src_encoding, dest_encoding): # real signature unknown; restored from __doc__
    """
    transcoding_input_stream(stream, src_encoding, dest_encoding)
    
        Add a transcoding transformation to the stream.
        Incoming data will be decoded according to ``src_encoding`` and
        then re-encoded according to ``dest_encoding``.
    
        Parameters
        ----------
        stream : NativeFile
            The stream to which the transformation should be applied.
        src_encoding : str
            The codec to use when reading data.
        dest_encoding : str
            The codec to use for emitted data.
    """
    pass

def type_for_alias(name): # real signature unknown; restored from __doc__
    """
    type_for_alias(name)
    
        Return DataType given a string alias if one exists.
    
        Parameters
        ----------
        name : str
            The alias of the DataType that should be retrieved.
    
        Returns
        -------
        type : DataType
    """
    pass

def tzinfo_to_string(tz): # real signature unknown; restored from __doc__
    """
    tzinfo_to_string(tz)
    
        Converts a time zone object into a string indicating the name of a time
        zone, one of:
        * As used in the Olson time zone database (the "tz database" or
          "tzdata"), such as "America/New_York"
        * An absolute time zone offset of the form +XX:XX or -XX:XX, such as +07:30
    
        Parameters
        ----------
          tz : datetime.tzinfo
            Time zone object
    
        Returns
        -------
          name : str
            Time zone name
    """
    pass

def uint16(): # real signature unknown; restored from __doc__
    """
    uint16()
    
        Create instance of unsigned uint16 type.
    
        Examples
        --------
        Create an instance of unsigned int16 type:
    
        >>> import pyarrow as pa
        >>> pa.uint16()
        DataType(uint16)
        >>> print(pa.uint16())
        uint16
    
        Create an array with unsigned int16 type:
    
        >>> pa.array([0, 1, 2], type=pa.uint16())
        <pyarrow.lib.UInt16Array object at ...>
        [
          0,
          1,
          2
        ]
    """
    pass

def uint32(): # real signature unknown; restored from __doc__
    """
    uint32()
    
        Create instance of unsigned uint32 type.
    
        Examples
        --------
        Create an instance of unsigned int32 type:
    
        >>> import pyarrow as pa
        >>> pa.uint32()
        DataType(uint32)
        >>> print(pa.uint32())
        uint32
    
        Create an array with unsigned int32 type:
    
        >>> pa.array([0, 1, 2], type=pa.uint32())
        <pyarrow.lib.UInt32Array object at ...>
        [
          0,
          1,
          2
        ]
    """
    pass

def uint64(): # real signature unknown; restored from __doc__
    """
    uint64()
    
        Create instance of unsigned uint64 type.
    
        Examples
        --------
        Create an instance of unsigned int64 type:
    
        >>> import pyarrow as pa
        >>> pa.uint64()
        DataType(uint64)
        >>> print(pa.uint64())
        uint64
    
        Create an array with unsigned uint64 type:
    
        >>> pa.array([0, 1, 2], type=pa.uint64())
        <pyarrow.lib.UInt64Array object at ...>
        [
          0,
          1,
          2
        ]
    """
    pass

def uint8(): # real signature unknown; restored from __doc__
    """
    uint8()
    
        Create instance of unsigned int8 type.
    
        Examples
        --------
        Create an instance of unsigned int8 type:
    
        >>> import pyarrow as pa
        >>> pa.uint8()
        DataType(uint8)
        >>> print(pa.uint8())
        uint8
    
        Create an array with unsigned int8 type:
    
        >>> pa.array([0, 1, 2], type=pa.uint8())
        <pyarrow.lib.UInt8Array object at ...>
        [
          0,
          1,
          2
        ]
    """
    pass

def unify_schemas(schemas, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unify_schemas(schemas, *, promote_options=u'default')
    
        Unify schemas by merging fields by name.
    
        The resulting schema will contain the union of fields from all schemas.
        Fields with the same name will be merged. Note that two fields with
        different types will fail merging by default.
    
        - The unified field will inherit the metadata from the schema where
            that field is first defined.
        - The first N fields in the schema will be ordered the same as the
            N fields in the first schema.
    
        The resulting schema will inherit its metadata from the first input
        schema.
    
        Parameters
        ----------
        schemas : list of Schema
            Schemas to merge into a single one.
        promote_options : str, default default
            Accepts strings "default" and "permissive".
            Default: null and only null can be unified with another type.
            Permissive: types are promoted to the greater common denominator.
    
        Returns
        -------
        Schema
    
        Raises
        ------
        ArrowInvalid :
            If any input schema contains fields with duplicate names.
            If Fields of the same name are not mergeable.
    """
    pass

def union(child_fields, mode, type_codes=None): # real signature unknown; restored from __doc__
    """
    union(child_fields, mode, type_codes=None)
    
        Create UnionType from child fields.
    
        A union is a nested type where each logical value is taken from a
        single child.  A buffer of 8-bit type ids indicates which child
        a given logical value is to be taken from.
    
        Unions come in two flavors: sparse and dense
        (see also `pyarrow.sparse_union` and `pyarrow.dense_union`).
    
        Parameters
        ----------
        child_fields : sequence of Field values
            Each field must have a UTF8-encoded name, and these field names are
            part of the type metadata.
        mode : str
            Must be 'sparse' or 'dense'
        type_codes : list of integers, default None
    
        Returns
        -------
        type : UnionType
    """
    pass

def unregister_extension_type(type_name): # real signature unknown; restored from __doc__
    """
    unregister_extension_type(type_name)
    
        Unregister a Python extension type.
    
        Parameters
        ----------
        type_name : str
            The name of the ExtensionType subclass to unregister.
    
        Examples
        --------
        Define a UuidType extension type subclassing ExtensionType:
    
        >>> import pyarrow as pa
        >>> class UuidType(pa.ExtensionType):
        ...    def __init__(self):
        ...       pa.ExtensionType.__init__(self, pa.binary(16), "my_package.uuid")
        ...    def __arrow_ext_serialize__(self):
        ...       # since we don't have a parameterized type, we don't need extra
        ...       # metadata to be deserialized
        ...       return b''
        ...    @classmethod
        ...    def __arrow_ext_deserialize__(self, storage_type, serialized):
        ...       # return an instance of this subclass given the serialized
        ...       # metadata.
        ...       return UuidType()
        ...
    
        Register the extension type:
    
        >>> pa.register_extension_type(UuidType())
    
        Unregister the extension type:
    
        >>> pa.unregister_extension_type("my_package.uuid")
    """
    pass

def utf8(): # real signature unknown; restored from __doc__
    """
    utf8()
    
        Alias for string().
    
        Examples
        --------
        Create an instance of a string type:
    
        >>> import pyarrow as pa
        >>> pa.utf8()
        DataType(string)
    
        and use the string type to create an array:
    
        >>> pa.array(['foo', 'bar', 'baz'], type=pa.utf8())
        <pyarrow.lib.StringArray object at ...>
        [
          "foo",
          "bar",
          "baz"
        ]
    """
    pass

def write_tensor(Tensor_tensor, NativeFile_dest): # real signature unknown; restored from __doc__
    """
    write_tensor(Tensor tensor, NativeFile dest)
    
        Write pyarrow.Tensor to pyarrow.NativeFile object its current position.
    
        Parameters
        ----------
        tensor : pyarrow.Tensor
        dest : pyarrow.NativeFile
    
        Returns
        -------
        bytes_written : int
            Total number of bytes written to the file
    """
    pass

def _break_traceback_cycle_from_frame(frame): # reliably restored by inspect
    # no doc
    pass

def _datetime_from_int(int64_t_value, TimeUnit_unit, tzinfo=None): # real signature unknown; restored from __doc__
    """ _datetime_from_int(int64_t value, TimeUnit unit, tzinfo=None) """
    pass

def _detect_compression(path): # real signature unknown; restored from __doc__
    """ _detect_compression(path) """
    pass

def _empty_array(DataType_type): # real signature unknown; restored from __doc__
    """
    _empty_array(DataType type)
    
        Create empty array of the given type.
    """
    pass

def _from_pydict(cls, mapping, schema, metadata): # real signature unknown; restored from __doc__
    """
    _from_pydict(cls, mapping, schema, metadata)
    
        Construct a Table/RecordBatch from Arrow arrays or columns.
    
        Parameters
        ----------
        cls : Class Table/RecordBatch
        mapping : dict or Mapping
            A mapping of strings to Arrays or Python lists.
        schema : Schema, default None
            If not passed, will be inferred from the Mapping values.
        metadata : dict or Mapping, default None
            Optional metadata for the schema (if inferred).
    
        Returns
        -------
        Table/RecordBatch
    """
    pass

def _from_pylist(cls, mapping, schema, metadata): # real signature unknown; restored from __doc__
    """
    _from_pylist(cls, mapping, schema, metadata)
    
        Construct a Table/RecordBatch from list of rows / dictionaries.
    
        Parameters
        ----------
        cls : Class Table/RecordBatch
        mapping : list of dicts of rows
            A mapping of strings to row values.
        schema : Schema, default None
            If not passed, will be inferred from the first row of the
            mapping values.
        metadata : dict or Mapping, default None
            Optional metadata for the schema (if inferred).
    
        Returns
        -------
        Table/RecordBatch
    """
    pass

def _gdb_test_session(): # real signature unknown; restored from __doc__
    """ _gdb_test_session() """
    pass

def _get_pandas_type(arrow_type, coerce_to_ns=False): # real signature unknown; restored from __doc__
    """ _get_pandas_type(arrow_type, coerce_to_ns=False) """
    pass

def _get_pandas_tz_type(arrow_type, coerce_to_ns=False): # real signature unknown; restored from __doc__
    """ _get_pandas_tz_type(arrow_type, coerce_to_ns=False) """
    pass

def _handle_arrow_array_protocol(obj, type, mask, size): # real signature unknown; restored from __doc__
    """ _handle_arrow_array_protocol(obj, type, mask, size) """
    pass

def _is_path_like(path): # reliably restored by inspect
    # no doc
    pass

def _is_primitive(Type_type): # real signature unknown; restored from __doc__
    """ _is_primitive(Type type) """
    pass

def _ndarray_to_arrow_type(values, DataType_type): # real signature unknown; restored from __doc__
    """ _ndarray_to_arrow_type(values, DataType type) """
    pass

def _normalize_slice(arrow_obj, slice_key): # real signature unknown; restored from __doc__
    """
    _normalize_slice(arrow_obj, slice key)
    
        Slices with step not equal to 1 (or None) will produce a copy
        rather than a zero-copy view
    """
    pass

def _pac(): # real signature unknown; restored from __doc__
    """ _pac() """
    pass

def _pc(): # real signature unknown; restored from __doc__
    """ _pc() """
    pass

def _reconstruct_record_batch(columns, schema): # real signature unknown; restored from __doc__
    """
    _reconstruct_record_batch(columns, schema)
    
        Internal: reconstruct RecordBatch from pickled components.
    """
    pass

def _reconstruct_table(arrays, schema): # real signature unknown; restored from __doc__
    """
    _reconstruct_table(arrays, schema)
    
        Internal: reconstruct pa.Table from pickled components.
    """
    pass

def _register_py_extension_type(): # real signature unknown; restored from __doc__
    """ _register_py_extension_type() """
    pass

def _restore_array(data): # real signature unknown; restored from __doc__
    """
    _restore_array(data)
    
        Reconstruct an Array from pickled ArrayData.
    """
    pass

def _stringify_path(path): # reliably restored by inspect
    """ Convert *path* to a string or unicode path if possible. """
    pass

def _to_pandas_dtype(arrow_type, options=None): # real signature unknown; restored from __doc__
    """ _to_pandas_dtype(arrow_type, options=None) """
    pass

def _unregister_py_extension_types(): # real signature unknown; restored from __doc__
    """ _unregister_py_extension_types() """
    pass

def __pyx_unpickle__PandasAPIShim(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle__PandasAPIShim(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle__PandasConvertible(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle__PandasConvertible(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle__Tabular(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle__Tabular(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle___Pyx_EnumMeta(*args, **kwargs): # real signature unknown
    pass

# classes

from ._Weakrefable import _Weakrefable
from ._PandasConvertible import _PandasConvertible
from .Array import Array
from .ArrowException import ArrowException
from .ArrowCancelled import ArrowCancelled
from .ArrowCapacityError import ArrowCapacityError
from .ArrowIndexError import ArrowIndexError
from .ArrowInvalid import ArrowInvalid
from .ArrowIOError import ArrowIOError
from .ArrowKeyError import ArrowKeyError
from .ArrowMemoryError import ArrowMemoryError
from .ArrowNotImplementedError import ArrowNotImplementedError
from .ArrowSerializationError import ArrowSerializationError
from .ArrowTypeError import ArrowTypeError
from .DataType import DataType
from .BaseExtensionType import BaseExtensionType
from .BaseListArray import BaseListArray
from .BinaryArray import BinaryArray
from .Scalar import Scalar
from .BinaryScalar import BinaryScalar
from .BooleanArray import BooleanArray
from .BooleanScalar import BooleanScalar
from .Buffer import Buffer
from .NativeFile import NativeFile
from .BufferedInputStream import BufferedInputStream
from .IOBase import IOBase
from .BufferedIOBase import BufferedIOBase
from .BufferedOutputStream import BufferedOutputStream
from .BufferOutputStream import BufferOutputStream
from .BufferReader import BufferReader
from .BuildInfo import BuildInfo
from .CacheOptions import CacheOptions
from .ChunkedArray import ChunkedArray
from .Codec import Codec
from .CompressedInputStream import CompressedInputStream
from .CompressedOutputStream import CompressedOutputStream
from .NumericArray import NumericArray
from .Date32Array import Date32Array
from .Date32Scalar import Date32Scalar
from .Date64Array import Date64Array
from .Date64Scalar import Date64Scalar
from .FixedSizeBinaryArray import FixedSizeBinaryArray
from .Decimal128Array import Decimal128Array
from .Decimal128Scalar import Decimal128Scalar
from .FixedSizeBinaryType import FixedSizeBinaryType
from .Decimal128Type import Decimal128Type
from .Decimal256Array import Decimal256Array
from .Decimal256Scalar import Decimal256Scalar
from .Decimal256Type import Decimal256Type
from .UnionType import UnionType
from .DenseUnionType import DenseUnionType
from .DictionaryArray import DictionaryArray
from .DictionaryMemo import DictionaryMemo
from .DictionaryScalar import DictionaryScalar
from .DictionaryType import DictionaryType
from .FloatingPointArray import FloatingPointArray
from .DoubleArray import DoubleArray
from .DoubleScalar import DoubleScalar
from .DurationArray import DurationArray
from .DurationScalar import DurationScalar
from .DurationType import DurationType
from .ExtensionArray import ExtensionArray
from .ExtensionScalar import ExtensionScalar
from .ExtensionType import ExtensionType
from .Field import Field
from .FixedShapeTensorArray import FixedShapeTensorArray
from .FixedShapeTensorType import FixedShapeTensorType
from .FixedSizeBinaryScalar import FixedSizeBinaryScalar
from .FixedSizeBufferWriter import FixedSizeBufferWriter
from .FixedSizeListArray import FixedSizeListArray
from .ListScalar import ListScalar
from .FixedSizeListScalar import FixedSizeListScalar
from .FixedSizeListType import FixedSizeListType
from .FloatArray import FloatArray
from .FloatScalar import FloatScalar
from .HalfFloatArray import HalfFloatArray
from .HalfFloatScalar import HalfFloatScalar
from .IntegerArray import IntegerArray
from .Int16Array import Int16Array
from .Int16Scalar import Int16Scalar
from .Int32Array import Int32Array
from .Int32Scalar import Int32Scalar
from .Int64Array import Int64Array
from .Int64Scalar import Int64Scalar
from .Int8Array import Int8Array
from .Int8Scalar import Int8Scalar
from .IpcReadOptions import IpcReadOptions
from .IpcWriteOptions import IpcWriteOptions
from .Mapping import Mapping
from ._Metadata import _Metadata
from .KeyValueMetadata import KeyValueMetadata
from .LargeBinaryArray import LargeBinaryArray
from .LargeBinaryScalar import LargeBinaryScalar
from .LargeListArray import LargeListArray
from .LargeListScalar import LargeListScalar
from .LargeListType import LargeListType
from .LargeStringArray import LargeStringArray
from .StringScalar import StringScalar
from .LargeStringScalar import LargeStringScalar
from .ListArray import ListArray
from .ListType import ListType
from .MemoryPool import MemoryPool
from .LoggingMemoryPool import LoggingMemoryPool
from .MapArray import MapArray
from .MapScalar import MapScalar
from .MapType import MapType
from .MemoryMappedFile import MemoryMappedFile
from .Message import Message
from .MessageReader import MessageReader
from .MetadataVersion import MetadataVersion
from .MockOutputStream import MockOutputStream
from .MonthDayNano import MonthDayNano
from .MonthDayNanoIntervalArray import MonthDayNanoIntervalArray
from .MonthDayNanoIntervalScalar import MonthDayNanoIntervalScalar
from .NullArray import NullArray
from .NullScalar import NullScalar
from .ordered_dict import ordered_dict
from .OSFile import OSFile
from .ProxyMemoryPool import ProxyMemoryPool
from .PyExtensionType import PyExtensionType
from .PythonFile import PythonFile
from .Queue import Queue
from ._ReadStats import _ReadStats
from .ReadStats import ReadStats
from ._Tabular import _Tabular
from .RecordBatch import RecordBatch
from .RecordBatchReader import RecordBatchReader
from ._RecordBatchWithMetadata import _RecordBatchWithMetadata
from .RecordBatchWithMetadata import RecordBatchWithMetadata
from .ResizableBuffer import ResizableBuffer
from .RunEndEncodedArray import RunEndEncodedArray
from .RunEndEncodedScalar import RunEndEncodedScalar
from .RunEndEncodedType import RunEndEncodedType
from .RuntimeInfo import RuntimeInfo
from .Schema import Schema
from .SignalStopHandler import SignalStopHandler
from .SparseCOOTensor import SparseCOOTensor
from .SparseCSCMatrix import SparseCSCMatrix
from .SparseCSFTensor import SparseCSFTensor
from .SparseCSRMatrix import SparseCSRMatrix
from .SparseUnionType import SparseUnionType
from .StopToken import StopToken
from .StringArray import StringArray
from .StringBuilder import StringBuilder
from .StructArray import StructArray
from .StructScalar import StructScalar
from .StructType import StructType
from .Table import Table
from .TableGroupBy import TableGroupBy
from .Tensor import Tensor
from .TextIOBase import TextIOBase
from .Time32Array import Time32Array
from .Time32Scalar import Time32Scalar
from .Time32Type import Time32Type
from .Time64Array import Time64Array
from .Time64Scalar import Time64Scalar
from .Time64Type import Time64Type
from .TimestampArray import TimestampArray
from .TimestampScalar import TimestampScalar
from .TimestampType import TimestampType
from .Transcoder import Transcoder
from .TransformInputStream import TransformInputStream
from .UInt16Array import UInt16Array
from .UInt16Scalar import UInt16Scalar
from .UInt32Array import UInt32Array
from .UInt32Scalar import UInt32Scalar
from .UInt64Array import UInt64Array
from .UInt64Scalar import UInt64Scalar
from .UInt8Array import UInt8Array
from .UInt8Scalar import UInt8Scalar
from .UnionArray import UnionArray
from .UnionScalar import UnionScalar
from .UnknownExtensionType import UnknownExtensionType
from .UnsupportedOperation import UnsupportedOperation
from .VersionInfo import VersionInfo
from ._WriteStats import _WriteStats
from .WriteStats import WriteStats
from ._CRecordBatchWriter import _CRecordBatchWriter
from ._ExtensionRegistryNanny import _ExtensionRegistryNanny
from ._PandasAPIShim import _PandasAPIShim
from ._ReadPandasMixin import _ReadPandasMixin
from ._RecordBatchFileReader import _RecordBatchFileReader
from ._RecordBatchStreamWriter import _RecordBatchStreamWriter
from ._RecordBatchFileWriter import _RecordBatchFileWriter
from ._RecordBatchStreamReader import _RecordBatchStreamReader
# variables with complex values

cpp_build_info = (
    '15.0.0',
    (
        15,
        0,
        0,
    ),
    '1500',
    '1500.0.0',
    'MSVC',
    '19.16.27045.0',
    '/DWIN32 /D_WINDOWS /GR /EHsc /D_SILENCE_TR1_NAMESPACE_DEPRECATION_WARNING',
    'a61f4af724cd06c3a9b4abd20491345997e532c0',
    '',
    'python-wheel-windows',
    'release',
)

cpp_version_info = (
    15,
    0,
    0,
)

NA = None # (!) forward: _NULL, real value is '<pyarrow.NullScalar: None>'

_NULL = None # (!) real value is '<pyarrow.NullScalar: None>'

_pandas_api = None # (!) real value is '<pyarrow.lib._PandasAPIShim object at 0x0000029E0B064D50>'

_python_extension_types_registry = []

_registry_nanny = None # (!) real value is '<pyarrow.lib._ExtensionRegistryNanny object at 0x0000029E0B068150>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000029E04641CA0>'

__pyx_capi__ = {
    'box_memory_pool': None, # (!) real value is '<capsule object "PyObject *( arrow::MemoryPool *)" at 0x0000029E0466E780>'
    'check_status': None, # (!) real value is '<capsule object "int (arrow::Status const &)" at 0x0000029E0466E6F0>'
    'convert_status': None, # (!) real value is '<capsule object "PyObject *(arrow::Status const &)" at 0x0000029E0466E720>'
    'ensure_type': None, # (!) real value is '<capsule object "struct __pyx_obj_7pyarrow_3lib_DataType *(PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_7pyarrow_3lib_ensure_type *__pyx_optional_args)" at 0x0000029E0466E930>'
    'get_input_stream': None, # (!) real value is '<capsule object "PyObject *(PyObject *, bool, std::shared_ptr< arrow::io::InputStream>  *)" at 0x0000029E0466E810>'
    'get_native_file': None, # (!) real value is '<capsule object "struct __pyx_obj_7pyarrow_3lib_NativeFile *(PyObject *, bool)" at 0x0000029E0466E8A0>'
    'get_reader': None, # (!) real value is '<capsule object "PyObject *(PyObject *, bool, std::shared_ptr< arrow::io::RandomAccessFile>  *)" at 0x0000029E0466E840>'
    'get_writer': None, # (!) real value is '<capsule object "PyObject *(PyObject *, std::shared_ptr< arrow::io::OutputStream>  *)" at 0x0000029E0466E870>'
    'make_streamwrap_func': None, # (!) real value is '<capsule object "std::shared_ptr<std::function<__pyx_t_7pyarrow_8includes_8libarrow_StreamWrapFunc> >  (PyObject *, PyObject *)" at 0x0000029E0466E900>'
    'maybe_unbox_memory_pool': None, # (!) real value is '<capsule object " arrow::MemoryPool *(struct __pyx_obj_7pyarrow_3lib_MemoryPool *)" at 0x0000029E0466E750>'
    'native_transcoding_input_stream': None, # (!) real value is '<capsule object "std::shared_ptr< arrow::io::InputStream>  (std::shared_ptr< arrow::io::InputStream> , PyObject *, PyObject *)" at 0x0000029E0466E8D0>'
    'pyarrow_internal_check_status': None, # (!) real value is '<capsule object "int (arrow::Status const &)" at 0x0000029E0466EF90>'
    'pyarrow_internal_convert_status': None, # (!) real value is '<capsule object "PyObject *(arrow::Status const &)" at 0x0000029E0466EFC0>'
    'pyarrow_is_array': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x0000029E0467A120>'
    'pyarrow_is_batch': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x0000029E0467A2D0>'
    'pyarrow_is_buffer': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x0000029E0467A030>'
    'pyarrow_is_chunked_array': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x0000029E0467A150>'
    'pyarrow_is_data_type': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x0000029E0467A060>'
    'pyarrow_is_field': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x0000029E0467A0C0>'
    'pyarrow_is_metadata': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x0000029E0467A090>'
    'pyarrow_is_scalar': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x0000029E0467A180>'
    'pyarrow_is_schema': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x0000029E0467A0F0>'
    'pyarrow_is_sparse_coo_tensor': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x0000029E0467A1E0>'
    'pyarrow_is_sparse_csc_matrix': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x0000029E0467A240>'
    'pyarrow_is_sparse_csf_tensor': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x0000029E0467A270>'
    'pyarrow_is_sparse_csr_matrix': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x0000029E0467A210>'
    'pyarrow_is_table': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x0000029E0467A2A0>'
    'pyarrow_is_tensor': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x0000029E0467A1B0>'
    'pyarrow_unwrap_array': None, # (!) real value is '<capsule object "std::shared_ptr< arrow::Array>  (PyObject *)" at 0x0000029E0466EDE0>'
    'pyarrow_unwrap_batch': None, # (!) real value is '<capsule object "std::shared_ptr< arrow::RecordBatch>  (PyObject *)" at 0x0000029E0466EF30>'
    'pyarrow_unwrap_buffer': None, # (!) real value is '<capsule object "std::shared_ptr< arrow::Buffer>  (PyObject *)" at 0x0000029E0466ECF0>'
    'pyarrow_unwrap_chunked_array': None, # (!) real value is '<capsule object "std::shared_ptr< arrow::ChunkedArray>  (PyObject *)" at 0x0000029E0466EE10>'
    'pyarrow_unwrap_data_type': None, # (!) real value is '<capsule object "std::shared_ptr< arrow::DataType>  (PyObject *)" at 0x0000029E0466ED20>'
    'pyarrow_unwrap_field': None, # (!) real value is '<capsule object "std::shared_ptr< arrow::Field>  (PyObject *)" at 0x0000029E0466ED50>'
    'pyarrow_unwrap_metadata': None, # (!) real value is '<capsule object "std::shared_ptr< arrow::KeyValueMetadata const >  (PyObject *)" at 0x0000029E0466E9C0>'
    'pyarrow_unwrap_scalar': None, # (!) real value is '<capsule object "std::shared_ptr< arrow::Scalar>  (PyObject *)" at 0x0000029E0466EDB0>'
    'pyarrow_unwrap_schema': None, # (!) real value is '<capsule object "std::shared_ptr< arrow::Schema>  (PyObject *)" at 0x0000029E0466ED80>'
    'pyarrow_unwrap_sparse_coo_tensor': None, # (!) real value is '<capsule object "std::shared_ptr< arrow::SparseCOOTensor>  (PyObject *)" at 0x0000029E0466EE40>'
    'pyarrow_unwrap_sparse_csc_matrix': None, # (!) real value is '<capsule object "std::shared_ptr< arrow::SparseCSCMatrix>  (PyObject *)" at 0x0000029E0466EE70>'
    'pyarrow_unwrap_sparse_csf_tensor': None, # (!) real value is '<capsule object "std::shared_ptr< arrow::SparseCSFTensor>  (PyObject *)" at 0x0000029E0466EEA0>'
    'pyarrow_unwrap_sparse_csr_matrix': None, # (!) real value is '<capsule object "std::shared_ptr< arrow::SparseCSRMatrix>  (PyObject *)" at 0x0000029E0466EED0>'
    'pyarrow_unwrap_table': None, # (!) real value is '<capsule object "std::shared_ptr< arrow::Table>  (PyObject *)" at 0x0000029E0466EF60>'
    'pyarrow_unwrap_tensor': None, # (!) real value is '<capsule object "std::shared_ptr< arrow::Tensor>  (PyObject *)" at 0x0000029E0466EF00>'
    'pyarrow_wrap_array': None, # (!) real value is '<capsule object "PyObject *(std::shared_ptr< arrow::Array>  const &)" at 0x0000029E0466EB40>'
    'pyarrow_wrap_batch': None, # (!) real value is '<capsule object "PyObject *(std::shared_ptr< arrow::RecordBatch>  const &)" at 0x0000029E0466EC90>'
    'pyarrow_wrap_buffer': None, # (!) real value is '<capsule object "PyObject *(std::shared_ptr< arrow::Buffer>  const &)" at 0x0000029E0466EA20>'
    'pyarrow_wrap_chunked_array': None, # (!) real value is '<capsule object "PyObject *(std::shared_ptr< arrow::ChunkedArray>  const &)" at 0x0000029E0466EB70>'
    'pyarrow_wrap_data_type': None, # (!) real value is '<capsule object "PyObject *(std::shared_ptr< arrow::DataType>  const &)" at 0x0000029E0466EA80>'
    'pyarrow_wrap_field': None, # (!) real value is '<capsule object "PyObject *(std::shared_ptr< arrow::Field>  const &)" at 0x0000029E0466EAB0>'
    'pyarrow_wrap_metadata': None, # (!) real value is '<capsule object "PyObject *(std::shared_ptr< arrow::KeyValueMetadata const >  const &)" at 0x0000029E0466E9F0>'
    'pyarrow_wrap_resizable_buffer': None, # (!) real value is '<capsule object "PyObject *(std::shared_ptr< arrow::ResizableBuffer>  const &)" at 0x0000029E0466EA50>'
    'pyarrow_wrap_scalar': None, # (!) real value is '<capsule object "PyObject *(std::shared_ptr< arrow::Scalar>  const &)" at 0x0000029E0466EB10>'
    'pyarrow_wrap_schema': None, # (!) real value is '<capsule object "PyObject *(std::shared_ptr< arrow::Schema>  const &)" at 0x0000029E0466EAE0>'
    'pyarrow_wrap_sparse_coo_tensor': None, # (!) real value is '<capsule object "PyObject *(std::shared_ptr< arrow::SparseCOOTensor>  const &)" at 0x0000029E0466EBA0>'
    'pyarrow_wrap_sparse_csc_matrix': None, # (!) real value is '<capsule object "PyObject *(std::shared_ptr< arrow::SparseCSCMatrix>  const &)" at 0x0000029E0466EBD0>'
    'pyarrow_wrap_sparse_csf_tensor': None, # (!) real value is '<capsule object "PyObject *(std::shared_ptr< arrow::SparseCSFTensor>  const &)" at 0x0000029E0466EC00>'
    'pyarrow_wrap_sparse_csr_matrix': None, # (!) real value is '<capsule object "PyObject *(std::shared_ptr< arrow::SparseCSRMatrix>  const &)" at 0x0000029E0466EC30>'
    'pyarrow_wrap_table': None, # (!) real value is '<capsule object "PyObject *(std::shared_ptr< arrow::Table>  const &)" at 0x0000029E0466ECC0>'
    'pyarrow_wrap_tensor': None, # (!) real value is '<capsule object "PyObject *(std::shared_ptr< arrow::Tensor>  const &)" at 0x0000029E0466EC60>'
    'string_to_timeunit': None, # (!) real value is '<capsule object "enum  arrow::TimeUnit::type (PyObject *)" at 0x0000029E0466E990>'
    'timeunit_to_string': None, # (!) real value is '<capsule object "PyObject *(enum  arrow::TimeUnit::type)" at 0x0000029E0466E960>'
    'wrap_array_output': None, # (!) real value is '<capsule object "PyObject *(PyObject *)" at 0x0000029E0466E7B0>'
    'wrap_datum': None, # (!) real value is '<capsule object "PyObject *( arrow::Datum const &)" at 0x0000029E0466E7E0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pyarrow.lib', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000029E04641CA0>, origin='C:\\\\Users\\\\hp\\\\PycharmProjects\\\\Text_Summarizer\\\\venv\\\\lib\\\\site-packages\\\\pyarrow\\\\lib.cp38-win_amd64.pyd')"

__test__ = {
    'Array.diff (line 940)': '\n        Compare contents of this array against another one.\n\n        Return a string containing the result of diffing this array\n        (on the left side) against the other array (on the right side).\n\n        Parameters\n        ----------\n        other : Array\n            The other array to compare this array with.\n\n        Returns\n        -------\n        diff : str\n            A human-readable printout of the differences.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> left = pa.array(["one", "two", "three"])\n        >>> right = pa.array(["two", None, "two-and-a-half", "three"])\n        >>> print(left.diff(right)) # doctest: +SKIP\n\n        @@ -0, +0 @@\n        -"one"\n        @@ -2, +1 @@\n        +null\n        +"two-and-a-half"\n\n        ',
    'BaseListArray.value_lengths (line 2117)': '\n        Return integers array with values equal to the respective length of\n        each list element. Null list values are null in the output.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> arr = pa.array([[1, 2, 3], [], None, [4]],\n        ...                type=pa.list_(pa.int32()))\n        >>> arr.value_lengths()\n        <pyarrow.lib.Int32Array object at ...>\n        [\n          3,\n          0,\n          null,\n          1\n        ]\n        ',
    'BaseListArray.value_parent_indices (line 2095)': '\n        Return array of same length as list child values array where each\n        output value is the index of the parent list array slot containing each\n        child value.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> arr = pa.array([[1, 2, 3], [], None, [4]],\n        ...                type=pa.list_(pa.int32()))\n        >>> arr.value_parent_indices()\n        <pyarrow.lib.Int64Array object at ...>\n        [\n          0,\n          0,\n          0,\n          3\n        ]\n        ',
    'ChunkedArray.cast (line 534)': "\n        Cast array values to another data type\n\n        See :func:`pyarrow.compute.cast` for usage.\n\n        Parameters\n        ----------\n        target_type : DataType, None\n            Type to cast array to.\n        safe : boolean, default True\n            Whether to check for conversion errors such as overflow.\n        options : CastOptions, default None\n            Additional checks pass by CastOptions\n\n        Returns\n        -------\n        cast : Array or ChunkedArray\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])\n        >>> n_legs.type\n        DataType(int64)\n\n        Change the data type of an array:\n\n        >>> n_legs_seconds = n_legs.cast(pa.duration('s'))\n        >>> n_legs_seconds.type\n        DurationType(duration[s])\n        ",
    'ChunkedArray.chunk (line 1229)': '\n        Select a chunk by its index.\n\n        Parameters\n        ----------\n        i : int\n\n        Returns\n        -------\n        pyarrow.Array\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.chunked_array([[2, 2, None], [4, 5, 100]])\n        >>> n_legs.chunk(1)\n        <pyarrow.lib.Int64Array object at ...>\n        [\n          4,\n          5,\n          100\n        ]\n        ',
    'ChunkedArray.chunks.__get__ (line 1259)': '\n        Convert to a list of single-chunked arrays.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.chunked_array([[2, 2, None], [4, 5, 100]])\n        >>> n_legs\n        <pyarrow.lib.ChunkedArray object at ...>\n        [\n          [\n            2,\n            2,\n            null\n          ],\n          [\n            4,\n            5,\n            100\n          ]\n        ]\n        >>> n_legs.chunks\n        [<pyarrow.lib.Int64Array object at ...>\n        [\n          2,\n          2,\n          null\n        ], <pyarrow.lib.Int64Array object at ...>\n        [\n          4,\n          5,\n          100\n        ]]\n        ',
    'ChunkedArray.combine_chunks (line 701)': '\n        Flatten this ChunkedArray into a single non-chunked array.\n\n        Parameters\n        ----------\n        memory_pool : MemoryPool, default None\n            For memory allocations, if required, otherwise use default pool\n\n        Returns\n        -------\n        result : Array\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])\n        >>> n_legs\n        <pyarrow.lib.ChunkedArray object at ...>\n        [\n          [\n            2,\n            2,\n            4\n          ],\n          [\n            4,\n            5,\n            100\n          ]\n        ]\n        >>> n_legs.combine_chunks()\n        <pyarrow.lib.Int64Array object at ...>\n        [\n          2,\n          2,\n          4,\n          4,\n          5,\n          100\n        ]\n        ',
    'ChunkedArray.dictionary_encode (line 568)': '\n        Compute dictionary-encoded representation of array.\n\n        See :func:`pyarrow.compute.dictionary_encode` for full usage.\n\n        Parameters\n        ----------\n        null_encoding : str, default "mask"\n            How to handle null entries.\n\n        Returns\n        -------\n        encoded : ChunkedArray\n            A dictionary-encoded version of this array.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> animals = pa.chunked_array((\n        ...             ["Flamingo", "Parrot", "Dog"],\n        ...             ["Horse", "Brittle stars", "Centipede"]\n        ...             ))\n        >>> animals.dictionary_encode()\n        <pyarrow.lib.ChunkedArray object at ...>\n        [\n        ...\n          -- dictionary:\n            [\n              "Flamingo",\n              "Parrot",\n              "Dog",\n              "Horse",\n              "Brittle stars",\n              "Centipede"\n            ]\n          -- indices:\n            [\n              0,\n              1,\n              2\n            ],\n        ...\n          -- dictionary:\n            [\n              "Flamingo",\n              "Parrot",\n              "Dog",\n              "Horse",\n              "Brittle stars",\n              "Centipede"\n            ]\n          -- indices:\n            [\n              3,\n              4,\n              5\n            ]\n        ]\n        ',
    'ChunkedArray.drop_null (line 1046)': '\n        Remove missing values from a chunked array.\n        See :func:`pyarrow.compute.drop_null` for full description.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.chunked_array([[2, 2, None], [4, 5, 100]])\n        >>> n_legs\n        <pyarrow.lib.ChunkedArray object at ...>\n        [\n          [\n            2,\n            2,\n            null\n          ],\n          [\n            4,\n            5,\n            100\n          ]\n        ]\n        >>> n_legs.drop_null()\n        <pyarrow.lib.ChunkedArray object at ...>\n        [\n          [\n            2,\n            2\n          ],\n          [\n            4,\n            5,\n            100\n          ]\n        ]\n        ',
    'ChunkedArray.equals (line 435)': '\n        Return whether the contents of two chunked arrays are equal.\n\n        Parameters\n        ----------\n        other : pyarrow.ChunkedArray\n            Chunked array to compare against.\n\n        Returns\n        -------\n        are_equal : bool\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])\n        >>> animals = pa.chunked_array((\n        ...             ["Flamingo", "Parrot", "Dog"],\n        ...             ["Horse", "Brittle stars", "Centipede"]\n        ...             ))\n        >>> n_legs.equals(n_legs)\n        True\n        >>> n_legs.equals(animals)\n        False\n        ',
    'ChunkedArray.fill_null (line 399)': '\n        Replace each null element in values with fill_value.\n\n        See :func:`pyarrow.compute.fill_null` for full usage.\n\n        Parameters\n        ----------\n        fill_value : any\n            The replacement value for null entries.\n\n        Returns\n        -------\n        result : Array or ChunkedArray\n            A new array with nulls replaced by the given value.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> fill_value = pa.scalar(5, type=pa.int8())\n        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, None, 100]])\n        >>> n_legs.fill_null(fill_value)\n        <pyarrow.lib.ChunkedArray object at ...>\n        [\n          [\n            2,\n            2,\n            4,\n            4,\n            5,\n            100\n          ]\n        ]\n        ',
    'ChunkedArray.filter (line 889)': '\n        Select values from the chunked array.\n\n        See :func:`pyarrow.compute.filter` for full usage.\n\n        Parameters\n        ----------\n        mask : Array or array-like\n            The boolean mask to filter the chunked array with.\n        null_selection_behavior : str, default "drop"\n            How nulls in the mask should be handled.\n\n        Returns\n        -------\n        filtered : Array or ChunkedArray\n            An array of the same type, with only the elements selected by\n            the boolean mask.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])\n        >>> n_legs\n        <pyarrow.lib.ChunkedArray object at ...>\n        [\n          [\n            2,\n            2,\n            4\n          ],\n          [\n            4,\n            5,\n            100\n          ]\n        ]\n        >>> mask = pa.array([True, False, None, True, False, True])\n        >>> n_legs.filter(mask)\n        <pyarrow.lib.ChunkedArray object at ...>\n        [\n          [\n            2\n          ],\n          [\n            4,\n            100\n          ]\n        ]\n        >>> n_legs.filter(mask, null_selection_behavior="emit_null")\n        <pyarrow.lib.ChunkedArray object at ...>\n        [\n          [\n            2,\n            null\n          ],\n          [\n            4,\n            100\n          ]\n        ]\n        ',
    'ChunkedArray.flatten (line 631)': '\n        Flatten this ChunkedArray.  If it has a struct type, the column is\n        flattened into one array per struct field.\n\n        Parameters\n        ----------\n        memory_pool : MemoryPool, default None\n            For memory allocations, if required, otherwise use default pool\n\n        Returns\n        -------\n        result : list of ChunkedArray\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])\n        >>> c_arr = pa.chunked_array(n_legs.value_counts())\n        >>> c_arr\n        <pyarrow.lib.ChunkedArray object at ...>\n        [\n          -- is_valid: all not null\n          -- child 0 type: int64\n            [\n              2,\n              4,\n              5,\n              100\n            ]\n          -- child 1 type: int64\n            [\n              2,\n              2,\n              1,\n              1\n            ]\n        ]\n        >>> c_arr.flatten()\n        [<pyarrow.lib.ChunkedArray object at ...>\n        [\n          [\n            2,\n            4,\n            5,\n            100\n          ]\n        ], <pyarrow.lib.ChunkedArray object at ...>\n        [\n          [\n            2,\n            2,\n            1,\n            1\n          ]\n        ]]\n        >>> c_arr.type\n        StructType(struct<values: int64, counts: int64>)\n        >>> n_legs.type\n        DataType(int64)\n        ',
    'ChunkedArray.get_total_buffer_size (line 256)': '\n        The sum of bytes in each buffer referenced by the chunked array.\n\n        An array may only reference a portion of a buffer.\n        This method will overestimate in this case and return the\n        byte size of the entire buffer.\n\n        If a buffer is referenced multiple times then it will\n        only be counted once.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, None, 100]])\n        >>> n_legs.get_total_buffer_size()\n        49\n        ',
    'ChunkedArray.index (line 953)': '\n        Find the first index of a value.\n\n        See :func:`pyarrow.compute.index` for full usage.\n\n        Parameters\n        ----------\n        value : Scalar or object\n            The value to look for in the array.\n        start : int, optional\n            The start index where to look for `value`.\n        end : int, optional\n            The end index where to look for `value`.\n        memory_pool : MemoryPool, optional\n            A memory pool for potential memory allocations.\n\n        Returns\n        -------\n        index : Int64Scalar\n            The index of the value in the array (-1 if not found).\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])\n        >>> n_legs\n        <pyarrow.lib.ChunkedArray object at ...>\n        [\n          [\n            2,\n            2,\n            4\n          ],\n          [\n            4,\n            5,\n            100\n          ]\n        ]\n        >>> n_legs.index(4)\n        <pyarrow.Int64Scalar: 2>\n        >>> n_legs.index(4, start=3)\n        <pyarrow.Int64Scalar: 3>\n        ',
    'ChunkedArray.is_nan (line 344)': '\n        Return boolean array indicating the NaN values.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import numpy as np\n        >>> arr = pa.chunked_array([[2, np.nan, 4], [4, None, 100]])\n        >>> arr.is_nan()\n        <pyarrow.lib.ChunkedArray object at ...>\n        [\n          [\n            false,\n            true,\n            false,\n            false,\n            null,\n            false\n          ]\n        ]\n        ',
    'ChunkedArray.is_null (line 311)': '\n        Return boolean array indicating the null values.\n\n        Parameters\n        ----------\n        nan_is_null : bool (optional, default False)\n            Whether floating-point NaN values should also be considered null.\n\n        Returns\n        -------\n        array : boolean Array or ChunkedArray\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, None, 100]])\n        >>> n_legs.is_null()\n        <pyarrow.lib.ChunkedArray object at ...>\n        [\n          [\n            false,\n            false,\n            false,\n            false,\n            true,\n            false\n          ]\n        ]\n        ',
    'ChunkedArray.is_valid (line 368)': '\n        Return boolean array indicating the non-null values.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, None, 100]])\n        >>> n_legs.is_valid()\n        <pyarrow.lib.ChunkedArray object at ...>\n        [\n          [\n            true,\n            true,\n            true\n          ],\n          [\n            true,\n            false,\n            true\n          ]\n        ]\n        ',
    'ChunkedArray.iterchunks (line 1296)': '\n        Convert to an iterator of ChunkArrays.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, None, 100]])\n        >>> for i in n_legs.iterchunks():\n        ...     print(i.null_count)\n        ...\n        0\n        1\n\n        ',
    'ChunkedArray.length (line 96)': '\n        Return length of a ChunkedArray.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])\n        >>> n_legs.length()\n        6\n        ',
    'ChunkedArray.nbytes.__get__ (line 226)': '\n        Total number of bytes consumed by the elements of the chunked array.\n\n        In other words, the sum of bytes from all buffer ranges referenced.\n\n        Unlike `get_total_buffer_size` this method will account for array\n        offsets.\n\n        If buffers are shared between arrays then the shared\n        portion will only be counted multiple times.\n\n        The dictionary of dictionary arrays will always be counted in their\n        entirety even if the array only references a portion of the dictionary.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, None, 100]])\n        >>> n_legs.nbytes\n        49\n        ',
    'ChunkedArray.null_count.__get__ (line 208)': '\n        Number of null entries\n\n        Returns\n        -------\n        int\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, None, 100]])\n        >>> n_legs.null_count\n        1\n        ',
    'ChunkedArray.num_chunks.__get__ (line 1212)': '\n        Number of underlying chunks.\n\n        Returns\n        -------\n        int\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.chunked_array([[2, 2, None], [4, 5, 100]])\n        >>> n_legs.num_chunks\n        2\n        ',
    'ChunkedArray.slice (line 831)': '\n        Compute zero-copy slice of this ChunkedArray\n\n        Parameters\n        ----------\n        offset : int, default 0\n            Offset from start of array to slice\n        length : int, default None\n            Length of slice (default is until end of batch starting from\n            offset)\n\n        Returns\n        -------\n        sliced : ChunkedArray\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])\n        >>> n_legs\n        <pyarrow.lib.ChunkedArray object at ...>\n        [\n          [\n            2,\n            2,\n            4\n          ],\n          [\n            4,\n            5,\n            100\n          ]\n        ]\n        >>> n_legs.slice(2,2)\n        <pyarrow.lib.ChunkedArray object at ...>\n        [\n          [\n            4\n          ],\n          [\n            4\n          ]\n        ]\n        ',
    'ChunkedArray.take (line 1000)': '\n        Select values from the chunked array.\n\n        See :func:`pyarrow.compute.take` for full usage.\n\n        Parameters\n        ----------\n        indices : Array or array-like\n            The indices in the array whose values will be returned.\n\n        Returns\n        -------\n        taken : Array or ChunkedArray\n            An array with the same datatype, containing the taken values.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])\n        >>> n_legs\n        <pyarrow.lib.ChunkedArray object at ...>\n        [\n          [\n            2,\n            2,\n            4\n          ],\n          [\n            4,\n            5,\n            100\n          ]\n        ]\n        >>> n_legs.take([1,4,5])\n        <pyarrow.lib.ChunkedArray object at ...>\n        [\n          [\n            2,\n            5,\n            100\n          ]\n        ]\n        ',
    'ChunkedArray.to_numpy (line 477)': "\n        Return a NumPy copy of this array (experimental).\n\n        Parameters\n        ----------\n        zero_copy_only : bool, default False\n            Introduced for signature consistence with pyarrow.Array.to_numpy.\n            This must be False here since NumPy arrays' buffer must be contiguous.\n\n        Returns\n        -------\n        array : numpy.ndarray\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])\n        >>> n_legs.to_numpy()\n        array([  2,   2,   4,   4,   5, 100])\n        ",
    'ChunkedArray.to_pylist (line 1314)': '\n        Convert to a list of native Python objects.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, None, 100]])\n        >>> n_legs.to_pylist()\n        [2, 2, 4, 4, None, 100]\n        ',
    'ChunkedArray.to_string (line 116)': '\n        Render a "pretty-printed" string representation of the ChunkedArray\n\n        Parameters\n        ----------\n        indent : int\n            How much to indent right the content of the array,\n            by default ``0``.\n        window : int\n            How many items to preview within each chunk at the begin and end\n            of the chunk when the chunk is bigger than the window.\n            The other elements will be ellipsed.\n        container_window : int\n            How many chunks to preview at the begin and end\n            of the array when the array is bigger than the window.\n            The other elements will be ellipsed.\n            This setting also applies to list columns.\n        skip_new_lines : bool\n            If the array should be rendered as a single line of text\n            or if each element should be on its own line.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])\n        >>> n_legs.to_string(skip_new_lines=True)\n        \'[[2,2,4],[4,5,100]]\'\n        ',
    'ChunkedArray.type.__get__ (line 83)': '\n        Return data type of a ChunkedArray.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])\n        >>> n_legs.type\n        DataType(int64)\n        ',
    'ChunkedArray.unify_dictionaries (line 1108)': '\n        Unify dictionaries across all chunks.\n\n        This method returns an equivalent chunked array, but where all\n        chunks share the same dictionary values.  Dictionary indices are\n        transposed accordingly.\n\n        If there are no dictionaries in the chunked array, it is returned\n        unchanged.\n\n        Parameters\n        ----------\n        memory_pool : MemoryPool, default None\n            For memory allocations, if required, otherwise use default pool\n\n        Returns\n        -------\n        result : ChunkedArray\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> arr_1 = pa.array(["Flamingo", "Parrot", "Dog"]).dictionary_encode()\n        >>> arr_2 = pa.array(["Horse", "Brittle stars", "Centipede"]).dictionary_encode()\n        >>> c_arr = pa.chunked_array([arr_1, arr_2])\n        >>> c_arr\n        <pyarrow.lib.ChunkedArray object at ...>\n        [\n        ...\n          -- dictionary:\n            [\n              "Flamingo",\n              "Parrot",\n              "Dog"\n            ]\n          -- indices:\n            [\n              0,\n              1,\n              2\n            ],\n        ...\n          -- dictionary:\n            [\n              "Horse",\n              "Brittle stars",\n              "Centipede"\n            ]\n          -- indices:\n            [\n              0,\n              1,\n              2\n            ]\n        ]\n        >>> c_arr.unify_dictionaries()\n        <pyarrow.lib.ChunkedArray object at ...>\n        [\n        ...\n          -- dictionary:\n            [\n              "Flamingo",\n              "Parrot",\n              "Dog",\n              "Horse",\n              "Brittle stars",\n              "Centipede"\n            ]\n          -- indices:\n            [\n              0,\n              1,\n              2\n            ],\n        ...\n          -- dictionary:\n            [\n              "Flamingo",\n              "Parrot",\n              "Dog",\n              "Horse",\n              "Brittle stars",\n              "Centipede"\n            ]\n          -- indices:\n            [\n              3,\n              4,\n              5\n            ]\n        ]\n        ',
    'ChunkedArray.unique (line 748)': '\n        Compute distinct elements in array\n\n        Returns\n        -------\n        pyarrow.Array\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])\n        >>> n_legs\n        <pyarrow.lib.ChunkedArray object at ...>\n        [\n          [\n            2,\n            2,\n            4\n          ],\n          [\n            4,\n            5,\n            100\n          ]\n        ]\n        >>> n_legs.unique()\n        <pyarrow.lib.Int64Array object at ...>\n        [\n          2,\n          4,\n          5,\n          100\n        ]\n        ',
    'ChunkedArray.value_counts (line 785)': '\n        Compute counts of unique elements in array.\n\n        Returns\n        -------\n        An array of  <input type "Values", int64_t "Counts"> structs\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])\n        >>> n_legs\n        <pyarrow.lib.ChunkedArray object at ...>\n        [\n          [\n            2,\n            2,\n            4\n          ],\n          [\n            4,\n            5,\n            100\n          ]\n        ]\n        >>> n_legs.value_counts()\n        <pyarrow.lib.StructArray object at ...>\n        -- is_valid: all not null\n        -- child 0 type: int64\n          [\n            2,\n            4,\n            5,\n            100\n          ]\n        -- child 1 type: int64\n          [\n            2,\n            2,\n            1,\n            1\n          ]\n        ',
    'DataType.bit_width.__get__ (line 222)': '\n        Bit width for fixed width type.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> pa.int64()\n        DataType(int64)\n        >>> pa.int64().bit_width\n        64\n        ',
    'DataType.equals (line 296)': '\n        Return true if type is equivalent to passed value.\n\n        Parameters\n        ----------\n        other : DataType or string convertible to DataType\n        check_metadata : bool\n            Whether nested Field metadata equality should be checked as well.\n\n        Returns\n        -------\n        is_equal : bool\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> pa.int64().equals(pa.string())\n        False\n        >>> pa.int64().equals(pa.int64())\n        True\n        ',
    'DataType.num_buffers.__get__ (line 263)': '\n        Number of data buffers required to construct Array type\n        excluding children.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> pa.int64().num_buffers\n        2\n        >>> pa.string().num_buffers\n        3\n        ',
    'DataType.num_fields.__get__ (line 241)': "\n        The number of child fields.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> pa.int64()\n        DataType(int64)\n        >>> pa.int64().num_fields\n        0\n        >>> pa.list_(pa.string())\n        ListType(list<item: string>)\n        >>> pa.list_(pa.string()).num_fields\n        1\n        >>> struct = pa.struct({'x': pa.int32(), 'y': pa.string()})\n        >>> struct.num_fields\n        2\n        ",
    'DataType.to_pandas_dtype (line 326)': "\n        Return the equivalent NumPy / Pandas dtype.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> pa.int64().to_pandas_dtype()\n        <class 'numpy.int64'>\n        ",
    'Decimal128Type.precision.__get__ (line 1266)': '\n        The decimal precision, in number of decimal digits (an integer).\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> t = pa.decimal128(5, 2)\n        >>> t.precision\n        5\n        ',
    'Decimal128Type.scale.__get__ (line 1280)': '\n        The decimal scale (an integer).\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> t = pa.decimal128(5, 2)\n        >>> t.scale\n        2\n        ',
    'Decimal256Type.precision.__get__ (line 1315)': '\n        The decimal precision, in number of decimal digits (an integer).\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> t = pa.decimal256(76, 38)\n        >>> t.precision\n        76\n        ',
    'Decimal256Type.scale.__get__ (line 1329)': '\n        The decimal scale (an integer).\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> t = pa.decimal256(76, 38)\n        >>> t.scale\n        38\n        ',
    'DictionaryType.index_type.__get__ (line 446)': '\n        The data type of dictionary indices (a signed integer type).\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> pa.dictionary(pa.int16(), pa.utf8()).index_type\n        DataType(int16)\n        ',
    'DictionaryType.ordered.__get__ (line 432)': '\n        Whether the dictionary is ordered, i.e. whether the ordering of values\n        in the dictionary is important.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> pa.dictionary(pa.int64(), pa.utf8()).ordered\n        False\n        ',
    'DictionaryType.value_type.__get__ (line 459)': '\n        The dictionary value type.\n\n        The dictionary values are found in an instance of DictionaryArray.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> pa.dictionary(pa.int16(), pa.utf8()).value_type\n        DataType(string)\n        ',
    'DurationType.unit.__get__ (line 1195)': "\n        The duration unit ('s', 'ms', 'us' or 'ns').\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> t = pa.duration('s')\n        >>> t.unit\n        's'\n        ",
    'Field.equals (line 2104)': "\n        Test if this field is equal to the other\n\n        Parameters\n        ----------\n        other : pyarrow.Field\n        check_metadata : bool, default False\n            Whether Field metadata equality should be checked as well.\n\n        Returns\n        -------\n        is_equal : bool\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> f1 = pa.field('key', pa.int32())\n        >>> f2 = pa.field('key', pa.int32(), nullable=False)\n        >>> f1.equals(f2)\n        False\n        >>> f1.equals(f1)\n        True\n        ",
    'Field.flatten (line 2365)': '\n        Flatten this field.  If a struct field, individual child fields\n        will be returned with their names prefixed by the parent\'s name.\n\n        Returns\n        -------\n        fields : List[pyarrow.Field]\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> f1 = pa.field(\'bar\', pa.float64(), nullable=False)\n        >>> f2 = pa.field(\'foo\', pa.int32()).with_metadata({"key": "Something important"})\n        >>> ff = pa.field(\'ff\', pa.struct([f1, f2]), nullable=False)\n\n        Flatten a struct field:\n\n        >>> ff\n        pyarrow.Field<ff: struct<bar: double not null, foo: int32> not null>\n        >>> ff.flatten()\n        [pyarrow.Field<ff.bar: double not null>, pyarrow.Field<ff.foo: int32>]\n        ',
    'Field.metadata.__get__ (line 2181)': '\n        The field metadata.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> field = pa.field(\'key\', pa.int32(),\n        ...                  metadata={"key": "Something important"})\n        >>> field.metadata\n        {b\'key\': b\'Something important\'}\n        ',
    'Field.name.__get__ (line 2167)': "\n        The field name.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> field = pa.field('key', pa.int32())\n        >>> field.name\n        'key'\n        ",
    'Field.nullable.__get__ (line 2150)': "\n        The field nullability.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> f1 = pa.field('key', pa.int32())\n        >>> f2 = pa.field('key', pa.int32(), nullable=False)\n        >>> f1.nullable\n        True\n        >>> f2.nullable\n        False\n        ",
    'Field.remove_metadata (line 2233)': '\n        Create new field without metadata, if any\n\n        Returns\n        -------\n        field : pyarrow.Field\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> field = pa.field(\'key\', pa.int32(),\n        ...                  metadata={"key": "Something important"})\n        >>> field.metadata\n        {b\'key\': b\'Something important\'}\n\n        Create new field by removing the metadata from the existing one:\n\n        >>> field_new = field.remove_metadata()\n        >>> field_new.metadata\n        ',
    'Field.with_metadata (line 2199)': '\n        Add metadata as dict of string keys and values to Field\n\n        Parameters\n        ----------\n        metadata : dict\n            Keys and values must be string-like / coercible to bytes\n\n        Returns\n        -------\n        field : pyarrow.Field\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> field = pa.field(\'key\', pa.int32())\n\n        Create new field by adding metadata to existing one:\n\n        >>> field_new = field.with_metadata({"key": "Something important"})\n        >>> field_new\n        pyarrow.Field<key: int32>\n        >>> field_new.metadata\n        {b\'key\': b\'Something important\'}\n        ',
    'Field.with_name (line 2294)': "\n        A copy of this field with the replaced name\n\n        Parameters\n        ----------\n        name : str\n\n        Returns\n        -------\n        field : pyarrow.Field\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> field = pa.field('key', pa.int32())\n        >>> field\n        pyarrow.Field<key: int32>\n\n        Create new field by replacing the name of an existing one:\n\n        >>> field_new = field.with_name('lock')\n        >>> field_new\n        pyarrow.Field<lock: int32>\n        ",
    'Field.with_nullable (line 2326)': "\n        A copy of this field with the replaced nullability\n\n        Parameters\n        ----------\n        nullable : bool\n\n        Returns\n        -------\n        field: pyarrow.Field\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> field = pa.field('key', pa.int32())\n        >>> field\n        pyarrow.Field<key: int32>\n        >>> field.nullable\n        True\n\n        Create new field by replacing the nullability of an existing one:\n\n        >>> field_new = field.with_nullable(False)\n        >>> field_new\n        pyarrow.Field<key: int32 not null>\n        >>> field_new.nullable\n        False\n        ",
    'Field.with_type (line 2259)': "\n        A copy of this field with the replaced type\n\n        Parameters\n        ----------\n        new_type : pyarrow.DataType\n\n        Returns\n        -------\n        field : pyarrow.Field\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> field = pa.field('key', pa.int32())\n        >>> field\n        pyarrow.Field<key: int32>\n\n        Create new field by replacing type of an existing one:\n\n        >>> field_new = field.with_type(pa.int64())\n        >>> field_new\n        pyarrow.Field<key: int64>\n        ",
    'FixedShapeTensorArray.from_numpy_ndarray (line 3587)': '\n        Convert numpy tensors (ndarrays) to a fixed shape tensor extension array.\n        The first dimension of ndarray will become the length of the fixed\n        shape tensor array.\n\n        Numpy array needs to be C-contiguous in memory\n        (``obj.flags["C_CONTIGUOUS"]==True``).\n\n        Parameters\n        ----------\n        obj : numpy.ndarray\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import numpy as np\n        >>> arr = np.array(\n        ...         [[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]],\n        ...         dtype=np.float32)\n        >>> pa.FixedShapeTensorArray.from_numpy_ndarray(arr)\n        <pyarrow.lib.FixedShapeTensorArray object at ...>\n        [\n          [\n            1,\n            2,\n            3,\n            4,\n            5,\n            6\n          ],\n          [\n            1,\n            2,\n            3,\n            4,\n            5,\n            6\n          ]\n        ]\n        ',
    'FixedSizeBinaryType.byte_width.__get__ (line 1231)': '\n        The binary size in bytes.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> t = pa.binary(3)\n        >>> t.byte_width\n        3\n        ',
    'FixedSizeListArray.from_arrays (line 2602)': '\n        Construct FixedSizeListArray from array of values and a list length.\n\n        Parameters\n        ----------\n        values : Array (any type)\n        list_size : int\n            The fixed length of the lists.\n        type : DataType, optional\n            If not specified, a default ListType with the values\' type and\n            `list_size` length is used.\n        mask : Array (boolean type), optional\n            Indicate which values are null (True) or not null (False).\n\n\n        Returns\n        -------\n        FixedSizeListArray\n\n        Examples\n        --------\n\n        Create from a values array and a list size:\n\n        >>> import pyarrow as pa\n        >>> values = pa.array([1, 2, 3, 4])\n        >>> arr = pa.FixedSizeListArray.from_arrays(values, 2)\n        >>> arr\n        <pyarrow.lib.FixedSizeListArray object at ...>\n        [\n          [\n            1,\n            2\n          ],\n          [\n            3,\n            4\n          ]\n        ]\n\n        Or create from a values array, list size and matching type:\n\n        >>> typ = pa.list_(pa.field("values", pa.int64()), 2)\n        >>> arr = pa.FixedSizeListArray.from_arrays(values,type=typ)\n        >>> arr\n        <pyarrow.lib.FixedSizeListArray object at ...>\n        [\n          [\n            1,\n            2\n          ],\n          [\n            3,\n            4\n          ]\n        ]\n        ',
    'FixedSizeListArray.values.__get__ (line 2687)': '\n        Return the underlying array of values which backs the\n        FixedSizeListArray.\n\n        Note even null elements are included.\n\n        Compare with :meth:`flatten`, which returns only the non-null\n        sub-list values.\n\n        Returns\n        -------\n        values : Array\n\n        See Also\n        --------\n        FixedSizeListArray.flatten : ...\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> array = pa.array(\n        ...     [[1, 2], None, [3, None]],\n        ...     type=pa.list_(pa.int32(), 2)\n        ... )\n        >>> array.values\n        <pyarrow.lib.Int32Array object at ...>\n        [\n          1,\n          2,\n          null,\n          null,\n          3,\n          null\n        ]\n\n        ',
    'FixedSizeListType.list_size.__get__ (line 695)': '\n        The size of the fixed size lists.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> pa.list_(pa.int32(), 2).list_size\n        2\n        ',
    'FixedSizeListType.value_field.__get__ (line 669)': '\n        The field for list values.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> pa.list_(pa.int32(), 2).value_field\n        pyarrow.Field<item: int32>\n        ',
    'FixedSizeListType.value_type.__get__ (line 682)': '\n        The data type of large list values.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> pa.list_(pa.int32(), 2).value_type\n        DataType(int32)\n        ',
    'LargeListArray.values.__get__ (line 2376)': "\n        Return the underlying array of values which backs the LargeListArray\n        ignoring the array's offset.\n\n        If any of the list elements are null, but are backed by a\n        non-empty sub-list, those elements will be included in the\n        output.\n\n        Compare with :meth:`flatten`, which returns only the non-null\n        values taking into consideration the array's offset.\n\n        Returns\n        -------\n        values : Array\n\n        See Also\n        --------\n        LargeListArray.flatten : ...\n\n        Examples\n        --------\n\n        The values include null elements from the sub-lists:\n\n        >>> import pyarrow as pa\n        >>> array = pa.array(\n        ...     [[1, 2], None, [3, 4, None, 6]],\n        ...     type=pa.large_list(pa.int32()),\n        ... )\n        >>> array.values\n        <pyarrow.lib.Int32Array object at ...>\n        [\n          1,\n          2,\n          3,\n          4,\n          null,\n          6\n        ]\n\n        If an array is sliced, the slice still uses the same\n        underlying data as the original array, just with an\n        offset. Since values ignores the offset, the values are the\n        same:\n\n        >>> sliced = array.slice(1, 2)\n        >>> sliced\n        <pyarrow.lib.LargeListArray object at ...>\n        [\n          null,\n          [\n            3,\n            4,\n            null,\n            6\n          ]\n        ]\n        >>> sliced.values\n        <pyarrow.lib.Int32Array object at ...>\n        [\n          1,\n          2,\n          3,\n          4,\n          null,\n          6\n        ]\n        ",
    'LargeListType.value_type.__get__ (line 547)': '\n        The data type of large list values.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> pa.large_list(pa.string()).value_type\n        DataType(string)\n        ',
    'ListArray.from_arrays (line 2145)': "\n        Construct ListArray from arrays of int32 offsets and values.\n\n        Parameters\n        ----------\n        offsets : Array (int32 type)\n        values : Array (any type)\n        type : DataType, optional\n            If not specified, a default ListType with the values' type is\n            used.\n        pool : MemoryPool, optional\n        mask : Array (boolean type), optional\n            Indicate which values are null (True) or not null (False).\n\n        Returns\n        -------\n        list_array : ListArray\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> values = pa.array([1, 2, 3, 4])\n        >>> offsets = pa.array([0, 2, 4])\n        >>> pa.ListArray.from_arrays(offsets, values)\n        <pyarrow.lib.ListArray object at ...>\n        [\n          [\n            1,\n            2\n          ],\n          [\n            3,\n            4\n          ]\n        ]\n        >>> # nulls in the offsets array become null lists\n        >>> offsets = pa.array([0, None, 2, 4])\n        >>> pa.ListArray.from_arrays(offsets, values)\n        <pyarrow.lib.ListArray object at ...>\n        [\n          [\n            1,\n            2\n          ],\n          null,\n          [\n            3,\n            4\n          ]\n        ]\n        ",
    'ListArray.offsets.__get__ (line 2294)': '\n        Return the list offsets as an int32 array.\n\n        The returned array will not have a validity bitmap, so you cannot\n        expect to pass it to `ListArray.from_arrays` and get back the same\n        list array if the original one has nulls.\n\n        Returns\n        -------\n        offsets : Int32Array\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> array = pa.array([[1, 2], None, [3, 4, 5]])\n        >>> array.offsets\n        <pyarrow.lib.Int32Array object at ...>\n        [\n          0,\n          2,\n          2,\n          5\n        ]\n        ',
    'ListArray.values.__get__ (line 2223)': "\n        Return the underlying array of values which backs the ListArray\n        ignoring the array's offset.\n\n        If any of the list elements are null, but are backed by a\n        non-empty sub-list, those elements will be included in the\n        output.\n\n        Compare with :meth:`flatten`, which returns only the non-null\n        values taking into consideration the array's offset.\n\n        Returns\n        -------\n        values : Array\n\n        See Also\n        --------\n        ListArray.flatten : ...\n\n        Examples\n        --------\n\n        The values include null elements from sub-lists:\n\n        >>> import pyarrow as pa\n        >>> array = pa.array([[1, 2], None, [3, 4, None, 6]])\n        >>> array.values\n        <pyarrow.lib.Int64Array object at ...>\n        [\n          1,\n          2,\n          3,\n          4,\n          null,\n          6\n        ]\n\n        If an array is sliced, the slice still uses the same\n        underlying data as the original array, just with an\n        offset. Since values ignores the offset, the values are the\n        same:\n\n        >>> sliced = array.slice(1, 2)\n        >>> sliced\n        <pyarrow.lib.ListArray object at ...>\n        [\n          null,\n          [\n            3,\n            4,\n            null,\n            6\n          ]\n        ]\n        >>> sliced.values\n        <pyarrow.lib.Int64Array object at ...>\n        [\n          1,\n          2,\n          3,\n          4,\n          null,\n          6\n        ]\n\n        ",
    'ListType.value_field.__get__ (line 495)': '\n        The field for list values.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> pa.list_(pa.string()).value_field\n        pyarrow.Field<item: string>\n        ',
    'ListType.value_type.__get__ (line 508)': '\n        The data type of list values.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> pa.list_(pa.string()).value_type\n        DataType(string)\n        ',
    'MapArray.from_arrays (line 2470)': '\n        Construct MapArray from arrays of int32 offsets and key, item arrays.\n\n        Parameters\n        ----------\n        offsets : array-like or sequence (int32 type)\n        keys : array-like or sequence (any type)\n        items : array-like or sequence (any type)\n        type : DataType, optional\n            If not specified, a default MapArray with the keys\' and items\' type is used.\n        pool : MemoryPool\n\n        Returns\n        -------\n        map_array : MapArray\n\n        Examples\n        --------\n        First, let\'s understand the structure of our dataset when viewed in a rectangular data model.\n        The total of 5 respondents answered the question "How much did you like the movie x?".\n        The value -1 in the integer array means that the value is missing. The boolean array\n        represents the null bitmask corresponding to the missing values in the integer array.\n\n        >>> import pyarrow as pa\n        >>> movies_rectangular = np.ma.masked_array([\n        ...     [10, -1, -1],\n        ...     [8, 4, 5],\n        ...     [-1, 10, 3],\n        ...     [-1, -1, -1],\n        ...     [-1, -1, -1]\n        ... ],\n        ... [\n        ...     [False, True, True],\n        ...     [False, False, False],\n        ...     [True, False, False],\n        ...     [True, True, True],\n        ...     [True, True, True],\n        ... ])\n\n        To represent the same data with the MapArray and from_arrays, the data is\n        formed like this:\n\n        >>> offsets = [\n        ...     0, #  -- row 1 start\n        ...     1, #  -- row 2 start\n        ...     4, #  -- row 3 start\n        ...     6, #  -- row 4 start\n        ...     6, #  -- row 5 start\n        ...     6, #  -- row 5 end\n        ... ]\n        >>> movies = [\n        ...     "Dark Knight", #  ---------------------------------- row 1\n        ...     "Dark Knight", "Meet the Parents", "Superman", #  -- row 2\n        ...     "Meet the Parents", "Superman", #  ----------------- row 3\n        ... ]\n        >>> likings = [\n        ...     10, #  -------- row 1\n        ...     8, 4, 5, #  --- row 2\n        ...     10, 3 #  ------ row 3\n        ... ]\n        >>> pa.MapArray.from_arrays(offsets, movies, likings).to_pandas()\n        0                                  [(Dark Knight, 10)]\n        1    [(Dark Knight, 8), (Meet the Parents, 4), (Sup...\n        2              [(Meet the Parents, 10), (Superman, 3)]\n        3                                                   []\n        4                                                   []\n        dtype: object\n\n        If the data in the empty rows needs to be marked as missing, it\'s possible\n        to do so by modifying the offsets argument, so that we specify `None` as\n        the starting positions of the rows we want marked as missing. The end row\n        offset still has to refer to the existing value from keys (and values):\n\n        >>> offsets = [\n        ...     0, #  ----- row 1 start\n        ...     1, #  ----- row 2 start\n        ...     4, #  ----- row 3 start\n        ...     None, #  -- row 4 start\n        ...     None, #  -- row 5 start\n        ...     6, #  ----- row 5 end\n        ... ]\n        >>> pa.MapArray.from_arrays(offsets, movies, likings).to_pandas()\n        0                                  [(Dark Knight, 10)]\n        1    [(Dark Knight, 8), (Meet the Parents, 4), (Sup...\n        2              [(Meet the Parents, 10), (Superman, 3)]\n        3                                                 None\n        4                                                 None\n        dtype: object\n        ',
    'MapType.item_field.__get__ (line 609)': '\n        The field for items in the map entries.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> pa.map_(pa.string(), pa.int32()).item_field\n        pyarrow.Field<value: int32>\n        ',
    'MapType.item_type.__get__ (line 622)': '\n        The data type of items in the map entries.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> pa.map_(pa.string(), pa.int32()).item_type\n        DataType(int32)\n        ',
    'MapType.key_field.__get__ (line 583)': '\n        The field for keys in the map entries.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> pa.map_(pa.string(), pa.int32()).key_field\n        pyarrow.Field<key: string not null>\n        ',
    'MapType.key_type.__get__ (line 596)': '\n        The data type of keys in the map entries.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> pa.map_(pa.string(), pa.int32()).key_type\n        DataType(string)\n        ',
    'MapType.keys_sorted.__get__ (line 635)': '\n        Should the entries be sorted according to keys.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> pa.map_(pa.string(), pa.int32(), keys_sorted=True).keys_sorted\n        True\n        ',
    'RecordBatch.equals (line 2582)': '\n        Check if contents of two record batches are equal.\n\n        Parameters\n        ----------\n        other : pyarrow.RecordBatch\n            RecordBatch to compare against.\n        check_metadata : bool, default False\n            Whether schema metadata equality should be checked as well.\n\n        Returns\n        -------\n        are_equal : bool\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])\n        >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])\n        >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],\n        ...                                     names=["n_legs", "animals"])\n        >>> batch_0 = pa.record_batch([])\n        >>> batch_1 = pa.RecordBatch.from_arrays([n_legs, animals],\n        ...                                       names=["n_legs", "animals"],\n        ...                                       metadata={"n_legs": "Number of legs per animal"})\n        >>> batch.equals(batch)\n        True\n        >>> batch.equals(batch_0)\n        False\n        >>> batch.equals(batch_1)\n        True\n        >>> batch.equals(batch_1, check_metadata=True)\n        False\n        ',
    'RecordBatch.filter (line 2530)': '\n        Select rows from the record batch.\n\n        See :func:`pyarrow.compute.filter` for full usage.\n\n        Parameters\n        ----------\n        mask : Array or array-like\n            The boolean mask to filter the record batch with.\n        null_selection_behavior : str, default "drop"\n            How nulls in the mask should be handled.\n\n        Returns\n        -------\n        filtered : RecordBatch\n            A record batch of the same schema, with only the rows selected\n            by the boolean mask.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])\n        >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])\n        >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],\n        ...                                     names=["n_legs", "animals"])\n        >>> batch.to_pandas()\n           n_legs        animals\n        0       2       Flamingo\n        1       2         Parrot\n        2       4            Dog\n        3       4          Horse\n        4       5  Brittle stars\n        5     100      Centipede\n\n        Define a mask and select rows:\n\n        >>> mask=[True, True, False, True, False, None]\n        >>> batch.filter(mask).to_pandas()\n           n_legs   animals\n        0       2  Flamingo\n        1       2    Parrot\n        2       4     Horse\n        >>> batch.filter(mask, null_selection_behavior=\'emit_null\').to_pandas()\n           n_legs   animals\n        0     2.0  Flamingo\n        1     2.0    Parrot\n        2     4.0     Horse\n        3     NaN      None\n        ',
    'RecordBatch.from_arrays (line 2783)': '\n        Construct a RecordBatch from multiple pyarrow.Arrays\n\n        Parameters\n        ----------\n        arrays : list of pyarrow.Array\n            One for each field in RecordBatch\n        names : list of str, optional\n            Names for the batch fields. If not passed, schema must be passed\n        schema : Schema, default None\n            Schema for the created batch. If not passed, names must be passed\n        metadata : dict or Mapping, default None\n            Optional metadata for the schema (if inferred).\n\n        Returns\n        -------\n        pyarrow.RecordBatch\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])\n        >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])\n        >>> names = ["n_legs", "animals"]\n\n        Construct a RecordBatch from pyarrow Arrays using names:\n\n        >>> pa.RecordBatch.from_arrays([n_legs, animals], names=names)\n        pyarrow.RecordBatch\n        n_legs: int64\n        animals: string\n        ----\n        n_legs: [2,2,4,4,5,100]\n        animals: ["Flamingo","Parrot","Dog","Horse","Brittle stars","Centipede"]\n        >>> pa.RecordBatch.from_arrays([n_legs, animals], names=names).to_pandas()\n           n_legs        animals\n        0       2       Flamingo\n        1       2         Parrot\n        2       4            Dog\n        3       4          Horse\n        4       5  Brittle stars\n        5     100      Centipede\n\n        Construct a RecordBatch from pyarrow Arrays using schema:\n\n        >>> my_schema = pa.schema([\n        ...     pa.field(\'n_legs\', pa.int64()),\n        ...     pa.field(\'animals\', pa.string())],\n        ...     metadata={"n_legs": "Number of legs per animal"})\n        >>> pa.RecordBatch.from_arrays([n_legs, animals], schema=my_schema).to_pandas()\n           n_legs        animals\n        0       2       Flamingo\n        1       2         Parrot\n        2       4            Dog\n        3       4          Horse\n        4       5  Brittle stars\n        5     100      Centipede\n        >>> pa.RecordBatch.from_arrays([n_legs, animals], schema=my_schema).schema\n        n_legs: int64\n        animals: string\n        -- schema metadata --\n        n_legs: \'Number of legs per animal\'\n        ',
    'RecordBatch.from_pandas (line 2688)': '\n        Convert pandas.DataFrame to an Arrow RecordBatch\n\n        Parameters\n        ----------\n        df : pandas.DataFrame\n        schema : pyarrow.Schema, optional\n            The expected schema of the RecordBatch. This can be used to\n            indicate the type of columns if we cannot infer it automatically.\n            If passed, the output will have exactly this schema. Columns\n            specified in the schema that are not found in the DataFrame columns\n            or its index will raise an error. Additional columns or index\n            levels in the DataFrame which are not specified in the schema will\n            be ignored.\n        preserve_index : bool, optional\n            Whether to store the index as an additional column in the resulting\n            ``RecordBatch``. The default of None will store the index as a\n            column, except for RangeIndex which is stored as metadata only. Use\n            ``preserve_index=True`` to force it to be stored as a column.\n        nthreads : int, default None\n            If greater than 1, convert columns to Arrow in parallel using\n            indicated number of threads. By default, this follows\n            :func:`pyarrow.cpu_count` (may use up to system CPU count threads).\n        columns : list, optional\n           List of column to be converted. If None, use all columns.\n\n        Returns\n        -------\n        pyarrow.RecordBatch\n\n\n        Examples\n        --------\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'year\': [2020, 2022, 2021, 2022],\n        ...                    \'month\': [3, 5, 7, 9],\n        ...                    \'day\': [1, 5, 9, 13],\n        ...                    \'n_legs\': [2, 4, 5, 100],\n        ...                    \'animals\': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})\n\n        Convert pandas DataFrame to RecordBatch:\n\n        >>> import pyarrow as pa\n        >>> pa.RecordBatch.from_pandas(df)\n        pyarrow.RecordBatch\n        year: int64\n        month: int64\n        day: int64\n        n_legs: int64\n        animals: string\n        ----\n        year: [2020,2022,2021,2022]\n        month: [3,5,7,9]\n        day: [1,5,9,13]\n        n_legs: [2,4,5,100]\n        animals: ["Flamingo","Horse","Brittle stars","Centipede"]\n\n        Convert pandas DataFrame to RecordBatch using schema:\n\n        >>> my_schema = pa.schema([\n        ...     pa.field(\'n_legs\', pa.int64()),\n        ...     pa.field(\'animals\', pa.string())],\n        ...     metadata={"n_legs": "Number of legs per animal"})\n        >>> pa.RecordBatch.from_pandas(df, schema=my_schema)\n        pyarrow.RecordBatch\n        n_legs: int64\n        animals: string\n        ----\n        n_legs: [2,4,5,100]\n        animals: ["Flamingo","Horse","Brittle stars","Centipede"]\n\n        Convert pandas DataFrame to RecordBatch specifying columns:\n\n        >>> pa.RecordBatch.from_pandas(df, columns=["n_legs"])\n        pyarrow.RecordBatch\n        n_legs: int64\n        ----\n        n_legs: [2,4,5,100]\n        ',
    'RecordBatch.from_struct_array (line 2882)': "\n        Construct a RecordBatch from a StructArray.\n\n        Each field in the StructArray will become a column in the resulting\n        ``RecordBatch``.\n\n        Parameters\n        ----------\n        struct_array : StructArray\n            Array to construct the record batch from.\n\n        Returns\n        -------\n        pyarrow.RecordBatch\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> struct = pa.array([{'n_legs': 2, 'animals': 'Parrot'},\n        ...                    {'year': 2022, 'n_legs': 4}])\n        >>> pa.RecordBatch.from_struct_array(struct).to_pandas()\n          animals  n_legs    year\n        0  Parrot       2     NaN\n        1    None       4  2022.0\n        ",
    'RecordBatch.get_total_buffer_size (line 2395)': '\n        The sum of bytes in each buffer referenced by the record batch\n\n        An array may only reference a portion of a buffer.\n        This method will overestimate in this case and return the\n        byte size of the entire buffer.\n\n        If a buffer is referenced multiple times then it will\n        only be counted once.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])\n        >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])\n        >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],\n        ...                                     names=["n_legs", "animals"])\n        >>> batch.get_total_buffer_size()\n        120\n        ',
    'RecordBatch.nbytes.__get__ (line 2362)': '\n        Total number of bytes consumed by the elements of the record batch.\n\n        In other words, the sum of bytes from all buffer ranges referenced.\n\n        Unlike `get_total_buffer_size` this method will account for array\n        offsets.\n\n        If buffers are shared between arrays then the shared\n        portion will only be counted multiple times.\n\n        The dictionary of dictionary arrays will always be counted in their\n        entirety even if the array only references a portion of the dictionary.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])\n        >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])\n        >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],\n        ...                                     names=["n_legs", "animals"])\n        >>> batch.nbytes\n        116\n        ',
    'RecordBatch.num_columns.__get__ (line 2274)': '\n        Number of columns\n\n        Returns\n        -------\n        int\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])\n        >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])\n        >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],\n        ...                                     names=["n_legs", "animals"])\n        >>> batch.num_columns\n        2\n        ',
    'RecordBatch.num_rows.__get__ (line 2295)': '\n        Number of rows\n\n        Due to the definition of a RecordBatch, all columns have the same\n        number of rows.\n\n        Returns\n        -------\n        int\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])\n        >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])\n        >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],\n        ...                                     names=["n_legs", "animals"])\n        >>> batch.num_rows\n        6\n        ',
    'RecordBatch.replace_schema_metadata (line 2227)': '\n        Create shallow copy of record batch by replacing schema\n        key-value metadata with the indicated new metadata (which may be None,\n        which deletes any existing metadata\n\n        Parameters\n        ----------\n        metadata : dict, default None\n\n        Returns\n        -------\n        shallow_copy : RecordBatch\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])\n\n        Constructing a RecordBatch with schema and metadata:\n\n        >>> my_schema = pa.schema([\n        ...     pa.field(\'n_legs\', pa.int64())],\n        ...     metadata={"n_legs": "Number of legs per animal"})\n        >>> batch = pa.RecordBatch.from_arrays([n_legs], schema=my_schema)\n        >>> batch.schema\n        n_legs: int64\n        -- schema metadata --\n        n_legs: \'Number of legs per animal\'\n\n        Shallow copy of a RecordBatch with deleted schema metadata:\n\n        >>> batch.replace_schema_metadata().schema\n        n_legs: int64\n        ',
    'RecordBatch.schema.__get__ (line 2319)': '\n        Schema of the RecordBatch and its columns\n\n        Returns\n        -------\n        pyarrow.Schema\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])\n        >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])\n        >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],\n        ...                                     names=["n_legs", "animals"])\n        >>> batch.schema\n        n_legs: int64\n        animals: string\n        ',
    'RecordBatch.select (line 2630)': '\n        Select columns of the RecordBatch.\n\n        Returns a new RecordBatch with the specified columns, and metadata\n        preserved.\n\n        Parameters\n        ----------\n        columns : list-like\n            The column names or integer indices to select.\n\n        Returns\n        -------\n        RecordBatch\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])\n        >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])\n        >>> batch = pa.record_batch([n_legs, animals],\n        ...                          names=["n_legs", "animals"])\n\n        Select columns my indices:\n\n        >>> batch.select([1])\n        pyarrow.RecordBatch\n        animals: string\n        ----\n        animals: ["Flamingo","Parrot","Dog","Horse","Brittle stars","Centipede"]\n\n        Select columns by names:\n\n        >>> batch.select(["n_legs"])\n        pyarrow.RecordBatch\n        n_legs: int64\n        ----\n        n_legs: [2,2,4,4,5,100]\n        ',
    'RecordBatch.serialize (line 2425)': '\n        Write RecordBatch to Buffer as encapsulated IPC message, which does not\n        include a Schema.\n\n        To reconstruct a RecordBatch from the encapsulated IPC message Buffer\n        returned by this function, a Schema must be passed separately. See\n        Examples.\n\n        Parameters\n        ----------\n        memory_pool : MemoryPool, default None\n            Uses default memory pool if not specified\n\n        Returns\n        -------\n        serialized : Buffer\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])\n        >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])\n        >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],\n        ...                                     names=["n_legs", "animals"])\n        >>> buf = batch.serialize()\n        >>> buf\n        <pyarrow.Buffer address=0x... size=... is_cpu=True is_mutable=True>\n\n        Reconstruct RecordBatch from IPC message Buffer and original Schema\n\n        >>> pa.ipc.read_record_batch(buf, batch.schema)\n        pyarrow.RecordBatch\n        n_legs: int64\n        animals: string\n        ----\n        n_legs: [2,2,4,4,5,100]\n        animals: ["Flamingo","Parrot","Dog","Horse","Brittle stars","Centipede"]\n        ',
    'RecordBatch.slice (line 2473)': '\n        Compute zero-copy slice of this RecordBatch\n\n        Parameters\n        ----------\n        offset : int, default 0\n            Offset from start of record batch to slice\n        length : int, default None\n            Length of slice (default is until end of batch starting from\n            offset)\n\n        Returns\n        -------\n        sliced : RecordBatch\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])\n        >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])\n        >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],\n        ...                                     names=["n_legs", "animals"])\n        >>> batch.to_pandas()\n           n_legs        animals\n        0       2       Flamingo\n        1       2         Parrot\n        2       4            Dog\n        3       4          Horse\n        4       5  Brittle stars\n        5     100      Centipede\n        >>> batch.slice(offset=3).to_pandas()\n           n_legs        animals\n        0       4          Horse\n        1       5  Brittle stars\n        2     100      Centipede\n        >>> batch.slice(length=2).to_pandas()\n           n_legs   animals\n        0       2  Flamingo\n        1       2    Parrot\n        >>> batch.slice(offset=3, length=1).to_pandas()\n           n_legs animals\n        0       4   Horse\n        ',
    'Schema.append (line 2912)': "\n        Append a field at the end of the schema.\n\n        In contrast to Python's ``list.append()`` it does return a new\n        object, leaving the original Schema unmodified.\n\n        Parameters\n        ----------\n        field : Field\n\n        Returns\n        -------\n        schema: Schema\n            New object with appended field.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> schema = pa.schema([\n        ...     pa.field('n_legs', pa.int64()),\n        ...     pa.field('animals', pa.string())])\n\n        Append a field 'extra' at the end of the schema:\n\n        >>> schema_new = schema.append(pa.field('extra', pa.bool_()))\n        >>> schema_new\n        n_legs: int64\n        animals: string\n        extra: bool\n\n        Original schema is unmodified:\n\n        >>> schema\n        n_legs: int64\n        animals: string\n        ",
    'Schema.empty_table (line 2647)': "\n        Provide an empty table according to the schema.\n\n        Returns\n        -------\n        table: pyarrow.Table\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> schema = pa.schema([\n        ...     pa.field('n_legs', pa.int64()),\n        ...     pa.field('animals', pa.string())])\n\n        Create an empty table with schema's fields:\n\n        >>> schema.empty_table()\n        pyarrow.Table\n        n_legs: int64\n        animals: string\n        ----\n        n_legs: [[]]\n        animals: [[]]\n        ",
    'Schema.equals (line 2675)': '\n        Test if this schema is equal to the other\n\n        Parameters\n        ----------\n        other :  pyarrow.Schema\n        check_metadata : bool, default False\n            Key/value metadata must be equal too\n\n        Returns\n        -------\n        is_equal : bool\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> schema1 = pa.schema([\n        ...     pa.field(\'n_legs\', pa.int64()),\n        ...     pa.field(\'animals\', pa.string())],\n        ...     metadata={"n_legs": "Number of legs per animal"})\n        >>> schema2 = pa.schema([\n        ...     (\'some_int\', pa.int32()),\n        ...     (\'some_string\', pa.string())\n        ... ])\n\n        Test two equal schemas:\n\n        >>> schema1.equals(schema1)\n        True\n\n        Test two unequal schemas:\n\n        >>> schema1.equals(schema2)\n        False\n        ',
    'Schema.field (line 2760)': "\n        Select a field by its column name or numeric index.\n\n        Parameters\n        ----------\n        i : int or string\n\n        Returns\n        -------\n        pyarrow.Field\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> schema = pa.schema([\n        ...     pa.field('n_legs', pa.int64()),\n        ...     pa.field('animals', pa.string())])\n\n        Select the second field:\n\n        >>> schema.field(1)\n        pyarrow.Field<animals: string>\n\n        Select the field of the column named 'n_legs':\n\n        >>> schema.field('n_legs')\n        pyarrow.Field<n_legs: int64>\n        ",
    'Schema.from_pandas (line 2715)': '\n        Returns implied schema from dataframe\n\n        Parameters\n        ----------\n        df : pandas.DataFrame\n        preserve_index : bool, default True\n            Whether to store the index as an additional column (or columns, for\n            MultiIndex) in the resulting `Table`.\n            The default of None will store the index as a column, except for\n            RangeIndex which is stored as metadata only. Use\n            ``preserve_index=True`` to force it to be stored as a column.\n\n        Returns\n        -------\n        pyarrow.Schema\n\n        Examples\n        --------\n        >>> import pandas as pd\n        >>> import pyarrow as pa\n        >>> df = pd.DataFrame({\n        ...     \'int\': [1, 2],\n        ...     \'str\': [\'a\', \'b\']\n        ... })\n\n        Create an Arrow Schema from the schema of a pandas dataframe:\n\n        >>> pa.Schema.from_pandas(df)\n        int: int64\n        str: string\n        -- schema metadata --\n        pandas: \'{"index_columns": [{"kind": "range", "name": null, ...\n        ',
    'Schema.get_all_field_indices (line 2884)': '\n        Return sorted list of indices for the fields with the given name.\n\n        Parameters\n        ----------\n        name : str\n            The name of the field to look up.\n\n        Returns\n        -------\n        indices : List[int]\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> schema = pa.schema([\n        ...     pa.field(\'n_legs\', pa.int64()),\n        ...     pa.field(\'animals\', pa.string()),\n        ...     pa.field(\'animals\', pa.bool_())])\n\n        Get the indexes of the fields named \'animals\':\n\n        >>> schema.get_all_field_indices("animals")\n        [1, 2]\n        ',
    'Schema.get_field_index (line 2844)': '\n        Return index of the unique field with the given name.\n\n        Parameters\n        ----------\n        name : str\n            The name of the field to look up.\n\n        Returns\n        -------\n        index : int\n            The index of the field with the given name; -1 if the\n            name isn\'t found or there are several fields with the given\n            name.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> schema = pa.schema([\n        ...     pa.field(\'n_legs\', pa.int64()),\n        ...     pa.field(\'animals\', pa.string())])\n\n        Get the index of the field named \'animals\':\n\n        >>> schema.get_field_index("animals")\n        1\n\n        Index in case of several fields with the given name:\n\n        >>> schema = pa.schema([\n        ...     pa.field(\'n_legs\', pa.int64()),\n        ...     pa.field(\'animals\', pa.string()),\n        ...     pa.field(\'animals\', pa.bool_())],\n        ...     metadata={"n_legs": "Number of legs per animal"})\n        >>> schema.get_field_index("animals")\n        -1\n        ',
    'Schema.insert (line 2951)': "\n        Add a field at position i to the schema.\n\n        Parameters\n        ----------\n        i : int\n        field : Field\n\n        Returns\n        -------\n        schema: Schema\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> schema = pa.schema([\n        ...     pa.field('n_legs', pa.int64()),\n        ...     pa.field('animals', pa.string())])\n\n        Insert a new field on the second position:\n\n        >>> schema.insert(1, pa.field('extra', pa.bool_()))\n        n_legs: int64\n        extra: bool\n        animals: string\n        ",
    'Schema.metadata.__get__ (line 2614)': '\n        The schema\'s metadata.\n\n        Returns\n        -------\n        metadata: dict\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> schema = pa.schema([\n        ...     pa.field(\'n_legs\', pa.int64()),\n        ...     pa.field(\'animals\', pa.string())],\n        ...     metadata={"n_legs": "Number of legs per animal"})\n\n        Get the metadata of the schema\'s fields:\n\n        >>> schema.metadata\n        {b\'n_legs\': b\'Number of legs per animal\'}\n        ',
    'Schema.names.__get__ (line 2563)': "\n        The schema's field names.\n\n        Returns\n        -------\n        list of str\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> schema = pa.schema([\n        ...     pa.field('n_legs', pa.int64()),\n        ...     pa.field('animals', pa.string())])\n\n        Get the names of the schema's fields:\n\n        >>> schema.names\n        ['n_legs', 'animals']\n        ",
    'Schema.pandas_metadata.__get__ (line 2537)': '\n        Return deserialized-from-JSON pandas metadata field (if it exists)\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'n_legs\': [2, 4, 5, 100],\n        ...                    \'animals\': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})\n        >>> schema = pa.Table.from_pandas(df).schema\n\n        Select pandas metadata field from Arrow Schema:\n\n        >>> schema.pandas_metadata\n        {\'index_columns\': [{\'kind\': \'range\', \'name\': None, \'start\': 0, \'stop\': 4, \'step\': 1}], ...\n        ',
    'Schema.remove (line 2989)': "\n        Remove the field at index i from the schema.\n\n        Parameters\n        ----------\n        i : int\n\n        Returns\n        -------\n        schema: Schema\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> schema = pa.schema([\n        ...     pa.field('n_legs', pa.int64()),\n        ...     pa.field('animals', pa.string())])\n\n        Remove the second field of the schema:\n\n        >>> schema.remove(1)\n        n_legs: int64\n        ",
    'Schema.remove_metadata (line 3140)': '\n        Create new schema without metadata, if any\n\n        Returns\n        -------\n        schema : pyarrow.Schema\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> schema = pa.schema([\n        ...     pa.field(\'n_legs\', pa.int64()),\n        ...     pa.field(\'animals\', pa.string())],\n        ...     metadata={"n_legs": "Number of legs per animal"})\n        >>> schema\n        n_legs: int64\n        animals: string\n        -- schema metadata --\n        n_legs: \'Number of legs per animal\'\n\n        Create a new schema with removing the metadata from the original:\n\n        >>> schema.remove_metadata()\n        n_legs: int64\n        animals: string\n        ',
    'Schema.serialize (line 3106)': "\n        Write Schema to Buffer as encapsulated IPC message\n\n        Parameters\n        ----------\n        memory_pool : MemoryPool, default None\n            Uses default memory pool if not specified\n\n        Returns\n        -------\n        serialized : Buffer\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> schema = pa.schema([\n        ...     pa.field('n_legs', pa.int64()),\n        ...     pa.field('animals', pa.string())])\n\n        Write schema to Buffer:\n\n        >>> schema.serialize()\n        <pyarrow.Buffer address=0x... size=... is_cpu=True is_mutable=True>\n        ",
    'Schema.set (line 3020)': "\n        Replace a field at position i in the schema.\n\n        Parameters\n        ----------\n        i : int\n        field : Field\n\n        Returns\n        -------\n        schema: Schema\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> schema = pa.schema([\n        ...     pa.field('n_legs', pa.int64()),\n        ...     pa.field('animals', pa.string())])\n\n        Replace the second field of the schema with a new field 'extra':\n\n        >>> schema.set(1, pa.field('replaced', pa.bool_()))\n        n_legs: int64\n        replaced: bool\n        ",
    'Schema.types.__get__ (line 2591)': "\n        The schema's field types.\n\n        Returns\n        -------\n        list of DataType\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> schema = pa.schema([\n        ...     pa.field('n_legs', pa.int64()),\n        ...     pa.field('animals', pa.string())])\n\n        Get the types of the schema's fields:\n\n        >>> schema.types\n        [DataType(int64), DataType(string)]\n        ",
    'Schema.with_metadata (line 3070)': '\n        Add metadata as dict of string keys and values to Schema\n\n        Parameters\n        ----------\n        metadata : dict\n            Keys and values must be string-like / coercible to bytes\n\n        Returns\n        -------\n        schema : pyarrow.Schema\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> schema = pa.schema([\n        ...     pa.field(\'n_legs\', pa.int64()),\n        ...     pa.field(\'animals\', pa.string())])\n\n        Add metadata to existing schema field:\n\n        >>> schema.with_metadata({"n_legs": "Number of legs per animal"})\n        n_legs: int64\n        animals: string\n        -- schema metadata --\n        n_legs: \'Number of legs per animal\'\n        ',
    'StructType.field (line 810)': "\n        Select a field by its column name or numeric index.\n\n        Parameters\n        ----------\n        i : int or str\n\n        Returns\n        -------\n        pyarrow.Field\n\n        Examples\n        --------\n\n        >>> import pyarrow as pa\n        >>> struct_type = pa.struct({'x': pa.int32(), 'y': pa.string()})\n\n        Select the second field:\n\n        >>> struct_type.field(1)\n        pyarrow.Field<y: string>\n\n        Select the field named 'x':\n\n        >>> struct_type.field('x')\n        pyarrow.Field<x: int32>\n        ",
    'StructType.get_all_field_indices (line 845)': "\n        Return sorted list of indices for the fields with the given name.\n\n        Parameters\n        ----------\n        name : str\n            The name of the field to look up.\n\n        Returns\n        -------\n        indices : List[int]\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> struct_type = pa.struct({'x': pa.int32(), 'y': pa.string()})\n        >>> struct_type.get_all_field_indices('x')\n        [0]\n        ",
    'StructType.get_field_index (line 777)': "\n        Return index of the unique field with the given name.\n\n        Parameters\n        ----------\n        name : str\n            The name of the field to look up.\n\n        Returns\n        -------\n        index : int\n            The index of the field with the given name; -1 if the\n            name isn't found or there are several fields with the given\n            name.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> struct_type = pa.struct({'x': pa.int32(), 'y': pa.string()})\n\n        Index of the field with a name 'y':\n\n        >>> struct_type.get_field_index('y')\n        1\n\n        Index of the field that does not exist:\n\n        >>> struct_type.get_field_index('z')\n        -1\n        ",
    'Table.add_column (line 4431)': '\n        Add column to Table at position.\n\n        A new table is returned with the column added, the original table\n        object is left unchanged.\n\n        Parameters\n        ----------\n        i : int\n            Index to place the column at.\n        field_ : str or Field\n            If a string is passed then the type is deduced from the column\n            data.\n        column : Array, list of Array, or values coercible to arrays\n            Column data.\n\n        Returns\n        -------\n        Table\n            New table with the passed column added.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'n_legs\': [2, 4, 5, 100],\n        ...                    \'animals\': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})\n        >>> table = pa.Table.from_pandas(df)\n\n        Add column:\n\n        >>> year = [2021, 2022, 2019, 2021]\n        >>> table.add_column(0,"year", [year])\n        pyarrow.Table\n        year: int64\n        n_legs: int64\n        animals: string\n        ----\n        year: [[2021,2022,2019,2021]]\n        n_legs: [[2,4,5,100]]\n        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]\n\n        Original table is left unchanged:\n\n        >>> table\n        pyarrow.Table\n        n_legs: int64\n        animals: string\n        ----\n        n_legs: [[2,4,5,100]]\n        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]\n        ',
    'Table.append_column (line 4505)': '\n        Append column at end of columns.\n\n        Parameters\n        ----------\n        field_ : str or Field\n            If a string is passed then the type is deduced from the column\n            data.\n        column : Array, list of Array, or values coercible to arrays\n            Column data.\n\n        Returns\n        -------\n        Table\n            New table with the passed column added.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'n_legs\': [2, 4, 5, 100],\n        ...                    \'animals\': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})\n        >>> table = pa.Table.from_pandas(df)\n\n        Append column at the end:\n\n        >>> year = [2021, 2022, 2019, 2021]\n        >>> table.append_column(\'year\', [year])\n        pyarrow.Table\n        n_legs: int64\n        animals: string\n        year: int64\n        ----\n        n_legs: [[2,4,5,100]]\n        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]\n        year: [[2021,2022,2019,2021]]\n        ',
    'Table.cast (line 3748)': '\n        Cast table values to another schema.\n\n        Parameters\n        ----------\n        target_schema : Schema\n            Schema to cast to, the names and order of fields must match.\n        safe : bool, default True\n            Check for overflows or other unsafe conversions.\n        options : CastOptions, default None\n            Additional checks pass by CastOptions\n\n        Returns\n        -------\n        Table\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'n_legs\': [2, 4, 5, 100],\n        ...                    \'animals\': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})\n        >>> table = pa.Table.from_pandas(df)\n        >>> table.schema\n        n_legs: int64\n        animals: string\n        -- schema metadata --\n        pandas: \'{"index_columns": [{"kind": "range", "name": null, "start": 0, ...\n\n        Define new schema and cast table values:\n\n        >>> my_schema = pa.schema([\n        ...     pa.field(\'n_legs\', pa.duration(\'s\')),\n        ...     pa.field(\'animals\', pa.string())]\n        ...     )\n        >>> table.cast(target_schema=my_schema)\n        pyarrow.Table\n        n_legs: duration[s]\n        animals: string\n        ----\n        n_legs: [[2,4,5,100]]\n        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]\n        ',
    'Table.combine_chunks (line 3595)': '\n        Make a new table by combining the chunks this table has.\n\n        All the underlying chunks in the ChunkedArray of each column are\n        concatenated into zero or one chunk.\n\n        Parameters\n        ----------\n        memory_pool : MemoryPool, default None\n            For memory allocations, if required, otherwise use default pool.\n\n        Returns\n        -------\n        Table\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])\n        >>> animals = pa.chunked_array([["Flamingo", "Parrot", "Dog"], ["Horse", "Brittle stars", "Centipede"]])\n        >>> names = ["n_legs", "animals"]\n        >>> table = pa.table([n_legs, animals], names=names)\n        >>> table\n        pyarrow.Table\n        n_legs: int64\n        animals: string\n        ----\n        n_legs: [[2,2,4],[4,5,100]]\n        animals: [["Flamingo","Parrot","Dog"],["Horse","Brittle stars","Centipede"]]\n        >>> table.combine_chunks()\n        pyarrow.Table\n        n_legs: int64\n        animals: string\n        ----\n        n_legs: [[2,2,4,4,5,100]]\n        animals: [["Flamingo","Parrot","Dog","Horse","Brittle stars","Centipede"]]\n        ',
    'Table.drop_columns (line 4679)': '\n        Drop one or more columns and return a new table.\n\n        Parameters\n        ----------\n        columns : str or list[str]\n            Field name(s) referencing existing column(s).\n\n        Raises\n        ------\n        KeyError\n            If any of the passed column names do not exist.\n\n        Returns\n        -------\n        Table\n            New table without the column(s).\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'n_legs\': [2, 4, 5, 100],\n        ...                    \'animals\': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})\n        >>> table = pa.Table.from_pandas(df)\n\n        Drop one column:\n\n        >>> table.drop_columns("animals")\n        pyarrow.Table\n        n_legs: int64\n        ----\n        n_legs: [[2,4,5,100]]\n\n        Drop one or more columns:\n\n        >>> table.drop_columns(["n_legs", "animals"])\n        pyarrow.Table\n        ...\n        ----\n        ',
    'Table.equals (line 3700)': '\n        Check if contents of two tables are equal.\n\n        Parameters\n        ----------\n        other : pyarrow.Table\n            Table to compare against.\n        check_metadata : bool, default False\n            Whether schema metadata equality should be checked as well.\n\n        Returns\n        -------\n        bool\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])\n        >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])\n        >>> names=["n_legs", "animals"]\n        >>> table = pa.Table.from_arrays([n_legs, animals], names=names)\n        >>> table_0 = pa.Table.from_arrays([])\n        >>> table_1 = pa.Table.from_arrays([n_legs, animals],\n        ...                                 names=names,\n        ...                                 metadata={"n_legs": "Number of legs per animal"})\n        >>> table.equals(table)\n        True\n        >>> table.equals(table_0)\n        False\n        >>> table.equals(table_1)\n        True\n        >>> table.equals(table_1, check_metadata=True)\n        False\n        ',
    'Table.filter (line 3344)': '\n        Select rows from the table.\n\n        The Table can be filtered based on a mask, which will be passed to\n        :func:`pyarrow.compute.filter` to perform the filtering, or it can\n        be filtered through a boolean :class:`.Expression`\n\n        Parameters\n        ----------\n        mask : Array or array-like or .Expression\n            The boolean mask or the :class:`.Expression` to filter the table with.\n        null_selection_behavior : str, default "drop"\n            How nulls in the mask should be handled, does nothing if\n            an :class:`.Expression` is used.\n\n        Returns\n        -------\n        filtered : Table\n            A table of the same schema, with only the rows selected\n            by applied filtering\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'year\': [2020, 2022, 2019, 2021],\n        ...                    \'n_legs\': [2, 4, 5, 100],\n        ...                    \'animals\': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})\n        >>> table = pa.Table.from_pandas(df)\n\n        Define an expression and select rows:\n\n        >>> import pyarrow.compute as pc\n        >>> expr = pc.field("year") <= 2020\n        >>> table.filter(expr)\n        pyarrow.Table\n        year: int64\n        n_legs: int64\n        animals: string\n        ----\n        year: [[2020,2019]]\n        n_legs: [[2,5]]\n        animals: [["Flamingo","Brittle stars"]]\n\n        Define a mask and select rows:\n\n        >>> mask=[True, True, False, None]\n        >>> table.filter(mask)\n        pyarrow.Table\n        year: int64\n        n_legs: int64\n        animals: string\n        ----\n        year: [[2020,2022]]\n        n_legs: [[2,4]]\n        animals: [["Flamingo","Horse"]]\n        >>> table.filter(mask, null_selection_behavior=\'emit_null\')\n        pyarrow.Table\n        year: int64\n        n_legs: int64\n        animals: string\n        ----\n        year: [[2020,2022,null]]\n        n_legs: [[2,4,null]]\n        animals: [["Flamingo","Horse",null]]\n        ',
    'Table.flatten (line 3530)': '\n        Flatten this Table.\n\n        Each column with a struct type is flattened\n        into one column per struct field.  Other columns are left unchanged.\n\n        Parameters\n        ----------\n        memory_pool : MemoryPool, default None\n            For memory allocations, if required, otherwise use default pool\n\n        Returns\n        -------\n        Table\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> struct = pa.array([{\'n_legs\': 2, \'animals\': \'Parrot\'},\n        ...                    {\'year\': 2022, \'n_legs\': 4}])\n        >>> month = pa.array([4, 6])\n        >>> table = pa.Table.from_arrays([struct,month],\n        ...                              names = ["a", "month"])\n        >>> table\n        pyarrow.Table\n        a: struct<animals: string, n_legs: int64, year: int64>\n          child 0, animals: string\n          child 1, n_legs: int64\n          child 2, year: int64\n        month: int64\n        ----\n        a: [\n          -- is_valid: all not null\n          -- child 0 type: string\n        ["Parrot",null]\n          -- child 1 type: int64\n        [2,4]\n          -- child 2 type: int64\n        [null,2022]]\n        month: [[4,6]]\n\n        Flatten the columns with struct field:\n\n        >>> table.flatten()\n        pyarrow.Table\n        a.animals: string\n        a.n_legs: int64\n        a.year: int64\n        month: int64\n        ----\n        a.animals: [["Parrot",null]]\n        a.n_legs: [[2,4]]\n        a.year: [[null,2022]]\n        month: [[4,6]]\n        ',
    'Table.from_arrays (line 3892)': '\n        Construct a Table from Arrow arrays.\n\n        Parameters\n        ----------\n        arrays : list of pyarrow.Array or pyarrow.ChunkedArray\n            Equal-length arrays that should form the table.\n        names : list of str, optional\n            Names for the table columns. If not passed, schema must be passed.\n        schema : Schema, default None\n            Schema for the created table. If not passed, names must be passed.\n        metadata : dict or Mapping, default None\n            Optional metadata for the schema (if inferred).\n\n        Returns\n        -------\n        Table\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.array([2, 4, 5, 100])\n        >>> animals = pa.array(["Flamingo", "Horse", "Brittle stars", "Centipede"])\n        >>> names = ["n_legs", "animals"]\n\n        Construct a Table from arrays:\n\n        >>> pa.Table.from_arrays([n_legs, animals], names=names)\n        pyarrow.Table\n        n_legs: int64\n        animals: string\n        ----\n        n_legs: [[2,4,5,100]]\n        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]\n\n        Construct a Table from arrays with metadata:\n\n        >>> my_metadata={"n_legs": "Number of legs per animal"}\n        >>> pa.Table.from_arrays([n_legs, animals],\n        ...                       names=names,\n        ...                       metadata=my_metadata)\n        pyarrow.Table\n        n_legs: int64\n        animals: string\n        ----\n        n_legs: [[2,4,5,100]]\n        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]\n        >>> pa.Table.from_arrays([n_legs, animals],\n        ...                       names=names,\n        ...                       metadata=my_metadata).schema\n        n_legs: int64\n        animals: string\n        -- schema metadata --\n        n_legs: \'Number of legs per animal\'\n\n        Construct a Table from arrays with pyarrow schema:\n\n        >>> my_schema = pa.schema([\n        ...     pa.field(\'n_legs\', pa.int64()),\n        ...     pa.field(\'animals\', pa.string())],\n        ...     metadata={"animals": "Name of the animal species"})\n        >>> pa.Table.from_arrays([n_legs, animals],\n        ...                       schema=my_schema)\n        pyarrow.Table\n        n_legs: int64\n        animals: string\n        ----\n        n_legs: [[2,4,5,100]]\n        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]\n        >>> pa.Table.from_arrays([n_legs, animals],\n        ...                       schema=my_schema).schema\n        n_legs: int64\n        animals: string\n        -- schema metadata --\n        animals: \'Name of the animal species\'\n        ',
    'Table.from_batches (line 4049)': '\n        Construct a Table from a sequence or iterator of Arrow RecordBatches.\n\n        Parameters\n        ----------\n        batches : sequence or iterator of RecordBatch\n            Sequence of RecordBatch to be converted, all schemas must be equal.\n        schema : Schema, default None\n            If not passed, will be inferred from the first RecordBatch.\n\n        Returns\n        -------\n        Table\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> n_legs = pa.array([2, 4, 5, 100])\n        >>> animals = pa.array(["Flamingo", "Horse", "Brittle stars", "Centipede"])\n        >>> names = ["n_legs", "animals"]\n        >>> batch = pa.record_batch([n_legs, animals], names=names)\n        >>> batch.to_pandas()\n           n_legs        animals\n        0       2       Flamingo\n        1       4          Horse\n        2       5  Brittle stars\n        3     100      Centipede\n\n        Construct a Table from a RecordBatch:\n\n        >>> pa.Table.from_batches([batch])\n        pyarrow.Table\n        n_legs: int64\n        animals: string\n        ----\n        n_legs: [[2,4,5,100]]\n        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]\n\n        Construct a Table from a sequence of RecordBatches:\n\n        >>> pa.Table.from_batches([batch, batch])\n        pyarrow.Table\n        n_legs: int64\n        animals: string\n        ----\n        n_legs: [[2,4,5,100],[2,4,5,100]]\n        animals: [["Flamingo","Horse","Brittle stars","Centipede"],["Flamingo","Horse","Brittle stars","Centipede"]]\n        ',
    'Table.from_pandas (line 3812)': '\n        Convert pandas.DataFrame to an Arrow Table.\n\n        The column types in the resulting Arrow Table are inferred from the\n        dtypes of the pandas.Series in the DataFrame. In the case of non-object\n        Series, the NumPy dtype is translated to its Arrow equivalent. In the\n        case of `object`, we need to guess the datatype by looking at the\n        Python objects in this Series.\n\n        Be aware that Series of the `object` dtype don\'t carry enough\n        information to always lead to a meaningful Arrow type. In the case that\n        we cannot infer a type, e.g. because the DataFrame is of length 0 or\n        the Series only contains None/nan objects, the type is set to\n        null. This behavior can be avoided by constructing an explicit schema\n        and passing it to this function.\n\n        Parameters\n        ----------\n        df : pandas.DataFrame\n        schema : pyarrow.Schema, optional\n            The expected schema of the Arrow Table. This can be used to\n            indicate the type of columns if we cannot infer it automatically.\n            If passed, the output will have exactly this schema. Columns\n            specified in the schema that are not found in the DataFrame columns\n            or its index will raise an error. Additional columns or index\n            levels in the DataFrame which are not specified in the schema will\n            be ignored.\n        preserve_index : bool, optional\n            Whether to store the index as an additional column in the resulting\n            ``Table``. The default of None will store the index as a column,\n            except for RangeIndex which is stored as metadata only. Use\n            ``preserve_index=True`` to force it to be stored as a column.\n        nthreads : int, default None\n            If greater than 1, convert columns to Arrow in parallel using\n            indicated number of threads. By default, this follows\n            :func:`pyarrow.cpu_count` (may use up to system CPU count threads).\n        columns : list, optional\n           List of column to be converted. If None, use all columns.\n        safe : bool, default True\n           Check for overflows or other unsafe conversions.\n\n        Returns\n        -------\n        Table\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'n_legs\': [2, 4, 5, 100],\n        ...                    \'animals\': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})\n        >>> pa.Table.from_pandas(df)\n        pyarrow.Table\n        n_legs: int64\n        animals: string\n        ----\n        n_legs: [[2,4,5,100]]\n        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]\n        ',
    'Table.from_struct_array (line 3995)': "\n        Construct a Table from a StructArray.\n\n        Each field in the StructArray will become a column in the resulting\n        ``Table``.\n\n        Parameters\n        ----------\n        struct_array : StructArray or ChunkedArray\n            Array to construct the table from.\n\n        Returns\n        -------\n        pyarrow.Table\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> struct = pa.array([{'n_legs': 2, 'animals': 'Parrot'},\n        ...                    {'year': 2022, 'n_legs': 4}])\n        >>> pa.Table.from_struct_array(struct).to_pandas()\n          animals  n_legs    year\n        0  Parrot       2     NaN\n        1    None       4  2022.0\n        ",
    'Table.get_total_buffer_size (line 4401)': '\n        The sum of bytes in each buffer referenced by the table.\n\n        An array may only reference a portion of a buffer.\n        This method will overestimate in this case and return the\n        byte size of the entire buffer.\n\n        If a buffer is referenced multiple times then it will\n        only be counted once.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'n_legs\': [None, 4, 5, None],\n        ...                    \'animals\': ["Flamingo", "Horse", None, "Centipede"]})\n        >>> table = pa.Table.from_pandas(df)\n        >>> table.get_total_buffer_size()\n        76\n        ',
    'Table.group_by (line 4758)': '\n        Declare a grouping over the columns of the table.\n\n        Resulting grouping can then be used to perform aggregations\n        with a subsequent ``aggregate()`` method.\n\n        Parameters\n        ----------\n        keys : str or list[str]\n            Name of the columns that should be used as the grouping key.\n        use_threads : bool, default True\n            Whether to use multithreading or not. When set to True (the\n            default), no stable ordering of the output is guaranteed.\n\n        Returns\n        -------\n        TableGroupBy\n\n        See Also\n        --------\n        TableGroupBy.aggregate\n\n        Examples\n        --------\n        >>> import pandas as pd\n        >>> import pyarrow as pa\n        >>> df = pd.DataFrame({\'year\': [2020, 2022, 2021, 2022, 2019, 2021],\n        ...                    \'n_legs\': [2, 2, 4, 4, 5, 100],\n        ...                    \'animal\': ["Flamingo", "Parrot", "Dog", "Horse",\n        ...                    "Brittle stars", "Centipede"]})\n        >>> table = pa.Table.from_pandas(df)\n        >>> table.group_by(\'year\').aggregate([(\'n_legs\', \'sum\')])\n        pyarrow.Table\n        year: int64\n        n_legs_sum: int64\n        ----\n        year: [[2020,2022,2021,2019]]\n        n_legs_sum: [[2,6,104,5]]\n        ',
    'Table.join (line 4800)': '\n        Perform a join between this table and another one.\n\n        Result of the join will be a new Table, where further\n        operations can be applied.\n\n        Parameters\n        ----------\n        right_table : Table\n            The table to join to the current one, acting as the right table\n            in the join operation.\n        keys : str or list[str]\n            The columns from current table that should be used as keys\n            of the join operation left side.\n        right_keys : str or list[str], default None\n            The columns from the right_table that should be used as keys\n            on the join operation right side.\n            When ``None`` use the same key names as the left table.\n        join_type : str, default "left outer"\n            The kind of join that should be performed, one of\n            ("left semi", "right semi", "left anti", "right anti",\n            "inner", "left outer", "right outer", "full outer")\n        left_suffix : str, default None\n            Which suffix to add to left column names. This prevents confusion\n            when the columns in left and right tables have colliding names.\n        right_suffix : str, default None\n            Which suffix to add to the right column names. This prevents confusion\n            when the columns in left and right tables have colliding names.\n        coalesce_keys : bool, default True\n            If the duplicated keys should be omitted from one of the sides\n            in the join result.\n        use_threads : bool, default True\n            Whether to use multithreading or not.\n\n        Returns\n        -------\n        Table\n\n        Examples\n        --------\n        >>> import pandas as pd\n        >>> import pyarrow as pa\n        >>> df1 = pd.DataFrame({\'id\': [1, 2, 3],\n        ...                     \'year\': [2020, 2022, 2019]})\n        >>> df2 = pd.DataFrame({\'id\': [3, 4],\n        ...                     \'n_legs\': [5, 100],\n        ...                     \'animal\': ["Brittle stars", "Centipede"]})\n        >>> t1 = pa.Table.from_pandas(df1)\n        >>> t2 = pa.Table.from_pandas(df2)\n\n        Left outer join:\n\n        >>> t1.join(t2, \'id\').combine_chunks().sort_by(\'year\')\n        pyarrow.Table\n        id: int64\n        year: int64\n        n_legs: int64\n        animal: string\n        ----\n        id: [[3,1,2]]\n        year: [[2019,2020,2022]]\n        n_legs: [[5,null,null]]\n        animal: [["Brittle stars",null,null]]\n\n        Full outer join:\n\n        >>> t1.join(t2, \'id\', join_type="full outer").combine_chunks().sort_by(\'year\')\n        pyarrow.Table\n        id: int64\n        year: int64\n        n_legs: int64\n        animal: string\n        ----\n        id: [[3,1,2,4]]\n        year: [[2019,2020,2022,null]]\n        n_legs: [[5,null,null,100]]\n        animal: [["Brittle stars",null,null,"Centipede"]]\n\n        Right outer join:\n\n        >>> t1.join(t2, \'id\', join_type="right outer").combine_chunks().sort_by(\'year\')\n        pyarrow.Table\n        year: int64\n        id: int64\n        n_legs: int64\n        animal: string\n        ----\n        year: [[2019,null]]\n        id: [[3,4]]\n        n_legs: [[5,100]]\n        animal: [["Brittle stars","Centipede"]]\n\n        Right anti join\n\n        >>> t1.join(t2, \'id\', join_type="right anti")\n        pyarrow.Table\n        id: int64\n        n_legs: int64\n        animal: string\n        ----\n        id: [[4]]\n        n_legs: [[100]]\n        animal: [["Centipede"]]\n        ',
    'Table.nbytes.__get__ (line 4368)': '\n        Total number of bytes consumed by the elements of the table.\n\n        In other words, the sum of bytes from all buffer ranges referenced.\n\n        Unlike `get_total_buffer_size` this method will account for array\n        offsets.\n\n        If buffers are shared between arrays then the shared\n        portion will only be counted multiple times.\n\n        The dictionary of dictionary arrays will always be counted in their\n        entirety even if the array only references a portion of the dictionary.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'n_legs\': [None, 4, 5, None],\n        ...                    \'animals\': ["Flamingo", "Horse", None, "Centipede"]})\n        >>> table = pa.Table.from_pandas(df)\n        >>> table.nbytes\n        72\n        ',
    'Table.num_columns.__get__ (line 4301)': '\n        Number of columns in this table.\n\n        Returns\n        -------\n        int\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'n_legs\': [None, 4, 5, None],\n        ...                    \'animals\': ["Flamingo", "Horse", None, "Centipede"]})\n        >>> table = pa.Table.from_pandas(df)\n        >>> table.num_columns\n        2\n        ',
    'Table.num_rows.__get__ (line 4322)': '\n        Number of rows in this table.\n\n        Due to the definition of a table, all columns have the same number of\n        rows.\n\n        Returns\n        -------\n        int\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'n_legs\': [None, 4, 5, None],\n        ...                    \'animals\': ["Flamingo", "Horse", None, "Centipede"]})\n        >>> table = pa.Table.from_pandas(df)\n        >>> table.num_rows\n        4\n        ',
    'Table.remove_column (line 4545)': '\n        Create new Table with the indicated column removed.\n\n        Parameters\n        ----------\n        i : int\n            Index of column to remove.\n\n        Returns\n        -------\n        Table\n            New table without the column.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'n_legs\': [2, 4, 5, 100],\n        ...                    \'animals\': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})\n        >>> table = pa.Table.from_pandas(df)\n        >>> table.remove_column(1)\n        pyarrow.Table\n        n_legs: int64\n        ----\n        n_legs: [[2,4,5,100]]\n        ',
    'Table.rename_columns (line 4638)': '\n        Create new table with columns renamed to provided names.\n\n        Parameters\n        ----------\n        names : list of str\n            List of new column names.\n\n        Returns\n        -------\n        Table\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'n_legs\': [2, 4, 5, 100],\n        ...                    \'animals\': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})\n        >>> table = pa.Table.from_pandas(df)\n        >>> new_names = ["n", "name"]\n        >>> table.rename_columns(new_names)\n        pyarrow.Table\n        n: int64\n        name: string\n        ----\n        n: [[2,4,5,100]]\n        name: [["Flamingo","Horse","Brittle stars","Centipede"]]\n        ',
    'Table.replace_schema_metadata (line 3467)': '\n        Create shallow copy of table by replacing schema\n        key-value metadata with the indicated new metadata (which may be None),\n        which deletes any existing metadata.\n\n        Parameters\n        ----------\n        metadata : dict, default None\n\n        Returns\n        -------\n        Table\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'year\': [2020, 2022, 2019, 2021],\n        ...                    \'n_legs\': [2, 4, 5, 100],\n        ...                    \'animals\': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})\n        >>> table = pa.Table.from_pandas(df)\n\n        Constructing a Table with pyarrow schema and metadata:\n\n        >>> my_schema = pa.schema([\n        ...     pa.field(\'n_legs\', pa.int64()),\n        ...     pa.field(\'animals\', pa.string())],\n        ...     metadata={"n_legs": "Number of legs per animal"})\n        >>> table= pa.table(df, my_schema)\n        >>> table.schema\n        n_legs: int64\n        animals: string\n        -- schema metadata --\n        n_legs: \'Number of legs per animal\'\n        pandas: ...\n\n        Create a shallow copy of a Table with deleted schema metadata:\n\n        >>> table.replace_schema_metadata().schema\n        n_legs: int64\n        animals: string\n\n        Create a shallow copy of a Table with new schema metadata:\n\n        >>> metadata={"animals": "Which animal"}\n        >>> table.replace_schema_metadata(metadata = metadata).schema\n        n_legs: int64\n        animals: string\n        -- schema metadata --\n        animals: \'Which animal\'\n        ',
    'Table.schema.__get__ (line 4258)': '\n        Schema of the table and its columns.\n\n        Returns\n        -------\n        Schema\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'n_legs\': [2, 4, 5, 100],\n        ...                    \'animals\': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})\n        >>> table = pa.Table.from_pandas(df)\n        >>> table.schema\n        n_legs: int64\n        animals: string\n        -- schema metadata --\n        pandas: \'{"index_columns": [{"kind": "range", "name": null, "start": 0, "\' ...\n        ',
    'Table.select (line 3416)': '\n        Select columns of the Table.\n\n        Returns a new Table with the specified columns, and metadata\n        preserved.\n\n        Parameters\n        ----------\n        columns : list-like\n            The column names or integer indices to select.\n\n        Returns\n        -------\n        Table\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'year\': [2020, 2022, 2019, 2021],\n        ...                    \'n_legs\': [2, 4, 5, 100],\n        ...                    \'animals\': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})\n        >>> table = pa.Table.from_pandas(df)\n        >>> table.select([0,1])\n        pyarrow.Table\n        year: int64\n        n_legs: int64\n        ----\n        year: [[2020,2022,2019,2021]]\n        n_legs: [[2,4,5,100]]\n        >>> table.select(["year"])\n        pyarrow.Table\n        year: int64\n        ----\n        year: [[2020,2022,2019,2021]]\n        ',
    'Table.set_column (line 4579)': '\n        Replace column in Table at position.\n\n        Parameters\n        ----------\n        i : int\n            Index to place the column at.\n        field_ : str or Field\n            If a string is passed then the type is deduced from the column\n            data.\n        column : Array, list of Array, or values coercible to arrays\n            Column data.\n\n        Returns\n        -------\n        Table\n            New table with the passed column set.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'n_legs\': [2, 4, 5, 100],\n        ...                    \'animals\': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})\n        >>> table = pa.Table.from_pandas(df)\n\n        Replace a column:\n\n        >>> year = [2021, 2022, 2019, 2021]\n        >>> table.set_column(1,\'year\', [year])\n        pyarrow.Table\n        n_legs: int64\n        year: int64\n        ----\n        n_legs: [[2,4,5,100]]\n        year: [[2021,2022,2019,2021]]\n        ',
    'Table.shape.__get__ (line 4346)': '\n        Dimensions of the table: (#rows, #columns).\n\n        Returns\n        -------\n        (int, int)\n            Number of rows and number of columns.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'n_legs\': [None, 4, 5, None],\n        ...                    \'animals\': ["Flamingo", "Horse", None, "Centipede"]})\n        >>> table = pa.Table.from_pandas(df)\n        >>> table.shape\n        (4, 2)\n        ',
    'Table.slice (line 3279)': '\n        Compute zero-copy slice of this Table.\n\n        Parameters\n        ----------\n        offset : int, default 0\n            Offset from start of table to slice.\n        length : int, default None\n            Length of slice (default is until end of table starting from\n            offset).\n\n        Returns\n        -------\n        Table\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'year\': [2020, 2022, 2019, 2021],\n        ...                    \'n_legs\': [2, 4, 5, 100],\n        ...                    \'animals\': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})\n        >>> table = pa.Table.from_pandas(df)\n        >>> table.slice(length=3)\n        pyarrow.Table\n        year: int64\n        n_legs: int64\n        animals: string\n        ----\n        year: [[2020,2022,2019]]\n        n_legs: [[2,4,5]]\n        animals: [["Flamingo","Horse","Brittle stars"]]\n        >>> table.slice(offset=2)\n        pyarrow.Table\n        year: int64\n        n_legs: int64\n        animals: string\n        ----\n        year: [[2019,2021]]\n        n_legs: [[5,100]]\n        animals: [["Brittle stars","Centipede"]]\n        >>> table.slice(offset=2, length=1)\n        pyarrow.Table\n        year: int64\n        n_legs: int64\n        animals: string\n        ----\n        year: [[2019]]\n        n_legs: [[5]]\n        animals: [["Brittle stars"]]\n        ',
    'Table.to_batches (line 4121)': '\n        Convert Table to a list of RecordBatch objects.\n\n        Note that this method is zero-copy, it merely exposes the same data\n        under a different API.\n\n        Parameters\n        ----------\n        max_chunksize : int, default None\n            Maximum size for RecordBatch chunks. Individual chunks may be\n            smaller depending on the chunk layout of individual columns.\n\n        Returns\n        -------\n        list[RecordBatch]\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'n_legs\': [2, 4, 5, 100],\n        ...                    \'animals\': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})\n        >>> table = pa.Table.from_pandas(df)\n\n        Convert a Table to a RecordBatch:\n\n        >>> table.to_batches()[0].to_pandas()\n           n_legs        animals\n        0       2       Flamingo\n        1       4          Horse\n        2       5  Brittle stars\n        3     100      Centipede\n\n        Convert a Table to a list of RecordBatches:\n\n        >>> table.to_batches(max_chunksize=2)[0].to_pandas()\n           n_legs   animals\n        0       2  Flamingo\n        1       4     Horse\n        >>> table.to_batches(max_chunksize=2)[1].to_pandas()\n           n_legs        animals\n        0       5  Brittle stars\n        1     100      Centipede\n        ',
    'Table.to_reader (line 4189)': '\n        Convert the Table to a RecordBatchReader.\n\n        Note that this method is zero-copy, it merely exposes the same data\n        under a different API.\n\n        Parameters\n        ----------\n        max_chunksize : int, default None\n            Maximum size for RecordBatch chunks. Individual chunks may be\n            smaller depending on the chunk layout of individual columns.\n\n        Returns\n        -------\n        RecordBatchReader\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'n_legs\': [2, 4, 5, 100],\n        ...                    \'animals\': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})\n        >>> table = pa.Table.from_pandas(df)\n\n        Convert a Table to a RecordBatchReader:\n\n        >>> table.to_reader()\n        <pyarrow.lib.RecordBatchReader object at ...>\n\n        >>> reader = table.to_reader()\n        >>> reader.schema\n        n_legs: int64\n        animals: string\n        -- schema metadata --\n        pandas: \'{"index_columns": [{"kind": "range", "name": null, "start": 0, ...\n        >>> reader.read_all()\n        pyarrow.Table\n        n_legs: int64\n        animals: string\n        ----\n        n_legs: [[2,4,5,100]]\n        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]\n        ',
    'Table.unify_dictionaries (line 3642)': '\n        Unify dictionaries across all chunks.\n\n        This method returns an equivalent table, but where all chunks of\n        each column share the same dictionary values.  Dictionary indices\n        are transposed accordingly.\n\n        Columns without dictionaries are returned unchanged.\n\n        Parameters\n        ----------\n        memory_pool : MemoryPool, default None\n            For memory allocations, if required, otherwise use default pool\n\n        Returns\n        -------\n        Table\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> arr_1 = pa.array(["Flamingo", "Parrot", "Dog"]).dictionary_encode()\n        >>> arr_2 = pa.array(["Horse", "Brittle stars", "Centipede"]).dictionary_encode()\n        >>> c_arr = pa.chunked_array([arr_1, arr_2])\n        >>> table = pa.table([c_arr], names=["animals"])\n        >>> table\n        pyarrow.Table\n        animals: dictionary<values=string, indices=int32, ordered=0>\n        ----\n        animals: [  -- dictionary:\n        ["Flamingo","Parrot","Dog"]  -- indices:\n        [0,1,2],  -- dictionary:\n        ["Horse","Brittle stars","Centipede"]  -- indices:\n        [0,1,2]]\n\n        Unify dictionaries across both chunks:\n\n        >>> table.unify_dictionaries()\n        pyarrow.Table\n        animals: dictionary<values=string, indices=int32, ordered=0>\n        ----\n        animals: [  -- dictionary:\n        ["Flamingo","Parrot","Dog","Horse","Brittle stars","Centipede"]  -- indices:\n        [0,1,2],  -- dictionary:\n        ["Flamingo","Parrot","Dog","Horse","Brittle stars","Centipede"]  -- indices:\n        [3,4,5]]\n        ',
    'TableGroupBy.aggregate (line 5449)': '\n        Perform an aggregation over the grouped columns of the table.\n\n        Parameters\n        ----------\n        aggregations : list[tuple(str, str)] or list[tuple(str, str, FunctionOptions)]\n            List of tuples, where each tuple is one aggregation specification\n            and consists of: aggregation column name followed\n            by function name and optionally aggregation function option.\n            Pass empty list to get a single row for each group.\n            The column name can be a string, an empty list or a list of\n            column names, for unary, nullary and n-ary aggregation functions\n            respectively.\n\n            For the list of function names and respective aggregation\n            function options see :ref:`py-grouped-aggrs`.\n\n        Returns\n        -------\n        Table\n            Results of the aggregation functions.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> t = pa.table([\n        ...       pa.array(["a", "a", "b", "b", "c"]),\n        ...       pa.array([1, 2, 3, 4, 5]),\n        ... ], names=["keys", "values"])\n\n        Sum the column "values" over the grouped column "keys":\n\n        >>> t.group_by("keys").aggregate([("values", "sum")])\n        pyarrow.Table\n        keys: string\n        values_sum: int64\n        ----\n        keys: [["a","b","c"]]\n        values_sum: [[3,7,5]]\n\n        Count the rows over the grouped column "keys":\n\n        >>> t.group_by("keys").aggregate([([], "count_all")])\n        pyarrow.Table\n        keys: string\n        count_all: int64\n        ----\n        keys: [["a","b","c"]]\n        count_all: [[2,2,1]]\n\n        Do multiple aggregations:\n\n        >>> t.group_by("keys").aggregate([\n        ...    ("values", "sum"),\n        ...    ("keys", "count")\n        ... ])\n        pyarrow.Table\n        keys: string\n        values_sum: int64\n        keys_count: int64\n        ----\n        keys: [["a","b","c"]]\n        values_sum: [[3,7,5]]\n        keys_count: [[2,2,1]]\n\n        Count the number of non-null values for column "values"\n        over the grouped column "keys":\n\n        >>> import pyarrow.compute as pc\n        >>> t.group_by(["keys"]).aggregate([\n        ...    ("values", "count", pc.CountOptions(mode="only_valid"))\n        ... ])\n        pyarrow.Table\n        keys: string\n        values_count: int64\n        ----\n        keys: [["a","b","c"]]\n        values_count: [[2,2,1]]\n\n        Get a single row for each group in column "keys":\n\n        >>> t.group_by("keys").aggregate([])\n        pyarrow.Table\n        keys: string\n        ----\n        keys: [["a","b","c"]]\n        ',
    'Tensor.dim_name (line 134)': '\n        Returns the name of the i-th tensor dimension.\n\n        Parameters\n        ----------\n        i : int\n            The physical index of the tensor dimension.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import numpy as np\n        >>> x = np.array([[2, 2, 4], [4, 5, 100]], np.int32)\n        >>> tensor = pa.Tensor.from_numpy(x, dim_names=["dim1","dim2"])\n        >>> tensor.dim_name(0)\n        \'dim1\'\n        >>> tensor.dim_name(1)\n        \'dim2\'\n        ',
    'Tensor.dim_names.__get__ (line 157)': '\n        Names of this tensor dimensions.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import numpy as np\n        >>> x = np.array([[2, 2, 4], [4, 5, 100]], np.int32)\n        >>> tensor = pa.Tensor.from_numpy(x, dim_names=["dim1","dim2"])\n        >>> tensor.dim_names\n        [\'dim1\', \'dim2\']\n        ',
    'Tensor.equals (line 104)': '\n        Return true if the tensors contains exactly equal data.\n\n        Parameters\n        ----------\n        other : Tensor\n            The other tensor to compare for equality.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import numpy as np\n        >>> x = np.array([[2, 2, 4], [4, 5, 100]], np.int32)\n        >>> tensor = pa.Tensor.from_numpy(x, dim_names=["dim1","dim2"])\n        >>> y = np.array([[2, 2, 4], [4, 5, 10]], np.int32)\n        >>> tensor2 = pa.Tensor.from_numpy(y, dim_names=["a","b"])\n        >>> tensor.equals(tensor)\n        True\n        >>> tensor.equals(tensor2)\n        False\n        ',
    'Tensor.from_numpy (line 51)': '\n        Create a Tensor from a numpy array.\n\n        Parameters\n        ----------\n        obj : numpy.ndarray\n            The source numpy array\n        dim_names : list, optional\n            Names of each dimension of the Tensor.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import numpy as np\n        >>> x = np.array([[2, 2, 4], [4, 5, 100]], np.int32)\n        >>> pa.Tensor.from_numpy(x, dim_names=["dim1","dim2"])\n        <pyarrow.Tensor>\n        type: int32\n        shape: (2, 3)\n        strides: (12, 4)\n        ',
    'Tensor.is_contiguous.__get__ (line 189)': '\n        Is this tensor contiguous in memory.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import numpy as np\n        >>> x = np.array([[2, 2, 4], [4, 5, 100]], np.int32)\n        >>> tensor = pa.Tensor.from_numpy(x, dim_names=["dim1","dim2"])\n        >>> tensor.is_contiguous\n        True\n        ',
    'Tensor.is_mutable.__get__ (line 173)': '\n        Is this tensor mutable or immutable.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import numpy as np\n        >>> x = np.array([[2, 2, 4], [4, 5, 100]], np.int32)\n        >>> tensor = pa.Tensor.from_numpy(x, dim_names=["dim1","dim2"])\n        >>> tensor.is_mutable\n        True\n        ',
    'Tensor.ndim.__get__ (line 205)': '\n        The dimension (n) of this tensor.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import numpy as np\n        >>> x = np.array([[2, 2, 4], [4, 5, 100]], np.int32)\n        >>> tensor = pa.Tensor.from_numpy(x, dim_names=["dim1","dim2"])\n        >>> tensor.ndim\n        2\n        ',
    'Tensor.shape.__get__ (line 237)': '\n        The shape of this tensor.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import numpy as np\n        >>> x = np.array([[2, 2, 4], [4, 5, 100]], np.int32)\n        >>> tensor = pa.Tensor.from_numpy(x, dim_names=["dim1","dim2"])\n        >>> tensor.shape\n        (2, 3)\n        ',
    'Tensor.size.__get__ (line 221)': '\n        The size of this tensor.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import numpy as np\n        >>> x = np.array([[2, 2, 4], [4, 5, 100]], np.int32)\n        >>> tensor = pa.Tensor.from_numpy(x, dim_names=["dim1","dim2"])\n        >>> tensor.size\n        6\n        ',
    'Tensor.strides.__get__ (line 254)': '\n        Strides of this tensor.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import numpy as np\n        >>> x = np.array([[2, 2, 4], [4, 5, 100]], np.int32)\n        >>> tensor = pa.Tensor.from_numpy(x, dim_names=["dim1","dim2"])\n        >>> tensor.strides\n        (12, 4)\n        ',
    'Tensor.to_numpy (line 85)': '\n        Convert arrow::Tensor to numpy.ndarray with zero copy\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import numpy as np\n        >>> x = np.array([[2, 2, 4], [4, 5, 100]], np.int32)\n        >>> tensor = pa.Tensor.from_numpy(x, dim_names=["dim1","dim2"])\n        >>> tensor.to_numpy()\n        array([[  2,   2,   4],\n               [  4,   5, 100]], dtype=int32)\n        ',
    'Time32Type.unit.__get__ (line 1128)': "\n        The time unit ('s' or 'ms').\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> t = pa.time32('ms')\n        >>> t.unit\n        'ms'\n        ",
    'Time64Type.unit.__get__ (line 1163)': "\n        The time unit ('us' or 'ns').\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> t = pa.time64('us')\n        >>> t.unit\n        'us'\n        ",
    'TimestampType.tz.__get__ (line 1087)': "\n        The timestamp time zone, if any, or None.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> t = pa.timestamp('s', tz='UTC')\n        >>> t.tz\n        'UTC'\n        ",
    'TimestampType.unit.__get__ (line 1073)': "\n        The timestamp unit ('s', 'ms', 'us' or 'ns').\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> t = pa.timestamp('us')\n        >>> t.unit\n        'us'\n        ",
    'UnionType.field (line 973)': "\n        Return a child field by its numeric index.\n\n        Parameters\n        ----------\n        i : int\n\n        Returns\n        -------\n        pyarrow.Field\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> union = pa.sparse_union([pa.field('a', pa.binary(10)), pa.field('b', pa.string())])\n        >>> union[0]\n        pyarrow.Field<a: fixed_size_binary[10]>\n        ",
    'UnionType.mode.__get__ (line 926)': '\n        The mode of the union ("dense" or "sparse").\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> union = pa.sparse_union([pa.field(\'a\', pa.binary(10)), pa.field(\'b\', pa.string())])\n        >>> union.mode\n        \'sparse\'\n        ',
    'UnionType.type_codes.__get__ (line 946)': "\n        The type code to indicate each data type in this union.\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> union = pa.sparse_union([pa.field('a', pa.binary(10)), pa.field('b', pa.string())])\n        >>> union.type_codes\n        [0, 1]\n        ",
    '_PandasConvertible.to_pandas (line 704)': '\n        Convert to a pandas-compatible NumPy array or DataFrame, as appropriate\n\n        Parameters\n        ----------\n        memory_pool : MemoryPool, default None\n            Arrow MemoryPool to use for allocations. Uses the default memory\n            pool if not passed.\n        categories : list, default empty\n            List of fields that should be returned as pandas.Categorical. Only\n            applies to table-like data structures.\n        strings_to_categorical : bool, default False\n            Encode string (UTF8) and binary types to pandas.Categorical.\n        zero_copy_only : bool, default False\n            Raise an ArrowException if this function call would require copying\n            the underlying data.\n        integer_object_nulls : bool, default False\n            Cast integers with nulls to objects\n        date_as_object : bool, default True\n            Cast dates to objects. If False, convert to datetime64 dtype with\n            the equivalent time unit (if supported). Note: in pandas version\n            < 2.0, only datetime64[ns] conversion is supported.\n        timestamp_as_object : bool, default False\n            Cast non-nanosecond timestamps (np.datetime64) to objects. This is\n            useful in pandas version 1.x if you have timestamps that don\'t fit\n            in the normal date range of nanosecond timestamps (1678 CE-2262 CE).\n            Non-nanosecond timestamps are supported in pandas version 2.0.\n            If False, all timestamps are converted to datetime64 dtype.\n        use_threads : bool, default True\n            Whether to parallelize the conversion using multiple threads.\n        deduplicate_objects : bool, default True\n            Do not create multiple copies Python objects when created, to save\n            on memory use. Conversion will be slower.\n        ignore_metadata : bool, default False\n            If True, do not use the \'pandas\' metadata to reconstruct the\n            DataFrame index, if present\n        safe : bool, default True\n            For certain data types, a cast is needed in order to store the\n            data in a pandas DataFrame or Series (e.g. timestamps are always\n            stored as nanoseconds in pandas). This option controls whether it\n            is a safe cast or not.\n        split_blocks : bool, default False\n            If True, generate one internal "block" for each column when\n            creating a pandas.DataFrame from a RecordBatch or Table. While this\n            can temporarily reduce memory note that various pandas operations\n            can trigger "consolidation" which may balloon memory use.\n        self_destruct : bool, default False\n            EXPERIMENTAL: If True, attempt to deallocate the originating Arrow\n            memory while converting the Arrow object to pandas. If you use the\n            object after calling to_pandas with this option it will crash your\n            program.\n\n            Note that you may not see always memory usage improvements. For\n            example, if multiple columns share an underlying allocation,\n            memory can\'t be freed until all columns are converted.\n        maps_as_pydicts : str, optional, default `None`\n            Valid values are `None`, \'lossy\', or \'strict\'.\n            The default behavior (`None`), is to convert Arrow Map arrays to\n            Python association lists (list-of-tuples) in the same order as the\n            Arrow Map, as in [(key1, value1), (key2, value2), ...].\n\n            If \'lossy\' or \'strict\', convert Arrow Map arrays to native Python dicts.\n            This can change the ordering of (key, value) pairs, and will\n            deduplicate multiple keys, resulting in a possible loss of data.\n\n            If \'lossy\', this key deduplication results in a warning printed\n            when detected. If \'strict\', this instead results in an exception\n            being raised when detected.\n        types_mapper : function, default None\n            A function mapping a pyarrow DataType to a pandas ExtensionDtype.\n            This can be used to override the default pandas type for conversion\n            of built-in pyarrow types or in absence of pandas_metadata in the\n            Table schema. The function receives a pyarrow DataType and is\n            expected to return a pandas ExtensionDtype or ``None`` if the\n            default conversion should be used for that type. If you have\n            a dictionary mapping, you can pass ``dict.get`` as function.\n        coerce_temporal_nanoseconds : bool, default False\n            Only applicable to pandas version >= 2.0.\n            A legacy option to coerce date32, date64, duration, and timestamp\n            time units to nanoseconds when converting to pandas. This is the\n            default behavior in pandas version 1.x. Set this option to True if\n            you\'d like to use this coercion when using pandas version >= 2.0\n            for backwards compatibility (not recommended otherwise).\n\n        Returns\n        -------\n        pandas.Series or pandas.DataFrame depending on type of object\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n\n        Convert a Table to pandas DataFrame:\n\n        >>> table = pa.table([\n        ...    pa.array([2, 4, 5, 100]),\n        ...    pa.array(["Flamingo", "Horse", "Brittle stars", "Centipede"])\n        ...    ], names=[\'n_legs\', \'animals\'])\n        >>> table.to_pandas()\n           n_legs        animals\n        0       2       Flamingo\n        1       4          Horse\n        2       5  Brittle stars\n        3     100      Centipede\n        >>> isinstance(table.to_pandas(), pd.DataFrame)\n        True\n\n        Convert a RecordBatch to pandas DataFrame:\n\n        >>> import pyarrow as pa\n        >>> n_legs = pa.array([2, 4, 5, 100])\n        >>> animals = pa.array(["Flamingo", "Horse", "Brittle stars", "Centipede"])\n        >>> batch = pa.record_batch([n_legs, animals],\n        ...                         names=["n_legs", "animals"])\n        >>> batch\n        pyarrow.RecordBatch\n        n_legs: int64\n        animals: string\n        ----\n        n_legs: [2,4,5,100]\n        animals: ["Flamingo","Horse","Brittle stars","Centipede"]\n        >>> batch.to_pandas()\n           n_legs        animals\n        0       2       Flamingo\n        1       4          Horse\n        2       5  Brittle stars\n        3     100      Centipede\n        >>> isinstance(batch.to_pandas(), pd.DataFrame)\n        True\n\n        Convert a Chunked Array to pandas Series:\n\n        >>> import pyarrow as pa\n        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])\n        >>> n_legs.to_pandas()\n        0      2\n        1      2\n        2      4\n        3      4\n        4      5\n        5    100\n        dtype: int64\n        >>> isinstance(n_legs.to_pandas(), pd.Series)\n        True\n        ',
    '_Tabular.column (line 1576)': '\n        Select single column from Table or RecordBatch.\n\n        Parameters\n        ----------\n        i : int or string\n            The index or name of the column to retrieve.\n\n        Returns\n        -------\n        column : Array (for RecordBatch) or ChunkedArray (for Table)\n\n        Examples\n        --------\n        Table (works similarly for RecordBatch)\n\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'n_legs\': [2, 4, 5, 100],\n        ...                    \'animals\': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})\n        >>> table = pa.Table.from_pandas(df)\n\n        Select a column by numeric index:\n\n        >>> table.column(0)\n        <pyarrow.lib.ChunkedArray object at ...>\n        [\n          [\n            2,\n            4,\n            5,\n            100\n          ]\n        ]\n\n        Select a column by its name:\n\n        >>> table.column("animals")\n        <pyarrow.lib.ChunkedArray object at ...>\n        [\n          [\n            "Flamingo",\n            "Horse",\n            "Brittle stars",\n            "Centipede"\n          ]\n        ]\n        ',
    '_Tabular.column_names.__get__ (line 1628)': '\n        Names of the Table or RecordBatch columns.\n\n        Returns\n        -------\n        list of str\n\n        Examples\n        --------\n        Table (works similarly for RecordBatch)\n\n        >>> import pyarrow as pa\n        >>> table = pa.Table.from_arrays([[2, 4, 5, 100],\n        ...                               ["Flamingo", "Horse", "Brittle stars", "Centipede"]],\n        ...                               names=[\'n_legs\', \'animals\'])\n        >>> table.column_names\n        [\'n_legs\', \'animals\']\n        ',
    '_Tabular.columns.__get__ (line 1650)': '\n        List of all columns in numerical order.\n\n        Returns\n        -------\n        columns : list of Array (for RecordBatch) or list of ChunkedArray (for Table)\n\n        Examples\n        --------\n        Table (works similarly for RecordBatch)\n\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'n_legs\': [None, 4, 5, None],\n        ...                    \'animals\': ["Flamingo", "Horse", None, "Centipede"]})\n        >>> table = pa.Table.from_pandas(df)\n        >>> table.columns\n        [<pyarrow.lib.ChunkedArray object at ...>\n        [\n          [\n            null,\n            4,\n            5,\n            null\n          ]\n        ], <pyarrow.lib.ChunkedArray object at ...>\n        [\n          [\n            "Flamingo",\n            "Horse",\n            null,\n            "Centipede"\n          ]\n        ]]\n        ',
    '_Tabular.drop_null (line 1688)': '\n        Remove rows that contain missing values from a Table or RecordBatch.\n\n        See :func:`pyarrow.compute.drop_null` for full usage.\n\n        Returns\n        -------\n        Table or RecordBatch\n            A tabular object with the same schema, with rows containing\n            no missing values.\n\n        Examples\n        --------\n        Table (works similarly for RecordBatch)\n\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'year\': [None, 2022, 2019, 2021],\n        ...                   \'n_legs\': [2, 4, 5, 100],\n        ...                   \'animals\': ["Flamingo", "Horse", None, "Centipede"]})\n        >>> table = pa.Table.from_pandas(df)\n        >>> table.drop_null()\n        pyarrow.Table\n        year: double\n        n_legs: int64\n        animals: string\n        ----\n        year: [[2022,2021]]\n        n_legs: [[4,100]]\n        animals: [["Horse","Centipede"]]\n        ',
    '_Tabular.field (line 1722)': '\n        Select a schema field by its column name or numeric index.\n\n        Parameters\n        ----------\n        i : int or string\n            The index or name of the field to retrieve.\n\n        Returns\n        -------\n        Field\n\n        Examples\n        --------\n        Table (works similarly for RecordBatch)\n\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'n_legs\': [2, 4, 5, 100],\n        ...                    \'animals\': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})\n        >>> table = pa.Table.from_pandas(df)\n        >>> table.field(0)\n        pyarrow.Field<n_legs: int64>\n        >>> table.field(1)\n        pyarrow.Field<animals: string>\n        ',
    '_Tabular.from_pydict (line 1752)': '\n        Construct a Table or RecordBatch from Arrow arrays or columns.\n\n        Parameters\n        ----------\n        mapping : dict or Mapping\n            A mapping of strings to Arrays or Python lists.\n        schema : Schema, default None\n            If not passed, will be inferred from the Mapping values.\n        metadata : dict or Mapping, default None\n            Optional metadata for the schema (if inferred).\n\n        Returns\n        -------\n        Table or RecordBatch\n\n        Examples\n        --------\n        Table (works similarly for RecordBatch)\n\n        >>> import pyarrow as pa\n        >>> n_legs = pa.array([2, 4, 5, 100])\n        >>> animals = pa.array(["Flamingo", "Horse", "Brittle stars", "Centipede"])\n        >>> pydict = {\'n_legs\': n_legs, \'animals\': animals}\n\n        Construct a Table from a dictionary of arrays:\n\n        >>> pa.Table.from_pydict(pydict)\n        pyarrow.Table\n        n_legs: int64\n        animals: string\n        ----\n        n_legs: [[2,4,5,100]]\n        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]\n        >>> pa.Table.from_pydict(pydict).schema\n        n_legs: int64\n        animals: string\n\n        Construct a Table from a dictionary of arrays with metadata:\n\n        >>> my_metadata={"n_legs": "Number of legs per animal"}\n        >>> pa.Table.from_pydict(pydict, metadata=my_metadata).schema\n        n_legs: int64\n        animals: string\n        -- schema metadata --\n        n_legs: \'Number of legs per animal\'\n\n        Construct a Table from a dictionary of arrays with pyarrow schema:\n\n        >>> my_schema = pa.schema([\n        ...     pa.field(\'n_legs\', pa.int64()),\n        ...     pa.field(\'animals\', pa.string())],\n        ...     metadata={"n_legs": "Number of legs per animal"})\n        >>> pa.Table.from_pydict(pydict, schema=my_schema).schema\n        n_legs: int64\n        animals: string\n        -- schema metadata --\n        n_legs: \'Number of legs per animal\'\n        ',
    '_Tabular.from_pylist (line 1819)': '\n        Construct a Table or RecordBatch from list of rows / dictionaries.\n\n        Parameters\n        ----------\n        mapping : list of dicts of rows\n            A mapping of strings to row values.\n        schema : Schema, default None\n            If not passed, will be inferred from the first row of the\n            mapping values.\n        metadata : dict or Mapping, default None\n            Optional metadata for the schema (if inferred).\n\n        Returns\n        -------\n        Table or RecordBatch\n\n        Examples\n        --------\n        Table (works similarly for RecordBatch)\n\n        >>> import pyarrow as pa\n        >>> pylist = [{\'n_legs\': 2, \'animals\': \'Flamingo\'},\n        ...           {\'n_legs\': 4, \'animals\': \'Dog\'}]\n\n        Construct a Table from a list of rows:\n\n        >>> pa.Table.from_pylist(pylist)\n        pyarrow.Table\n        n_legs: int64\n        animals: string\n        ----\n        n_legs: [[2,4]]\n        animals: [["Flamingo","Dog"]]\n\n        Construct a Table from a list of rows with metadata:\n\n        >>> my_metadata={"n_legs": "Number of legs per animal"}\n        >>> pa.Table.from_pylist(pylist, metadata=my_metadata).schema\n        n_legs: int64\n        animals: string\n        -- schema metadata --\n        n_legs: \'Number of legs per animal\'\n\n        Construct a Table from a list of rows with pyarrow schema:\n\n        >>> my_schema = pa.schema([\n        ...     pa.field(\'n_legs\', pa.int64()),\n        ...     pa.field(\'animals\', pa.string())],\n        ...     metadata={"n_legs": "Number of legs per animal"})\n        >>> pa.Table.from_pylist(pylist, schema=my_schema).schema\n        n_legs: int64\n        animals: string\n        -- schema metadata --\n        n_legs: \'Number of legs per animal\'\n        ',
    '_Tabular.itercolumns (line 1882)': '\n        Iterator over all columns in their numerical order.\n\n        Yields\n        ------\n        Array (for RecordBatch) or ChunkedArray (for Table)\n\n        Examples\n        --------\n        Table (works similarly for RecordBatch)\n\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'n_legs\': [None, 4, 5, None],\n        ...                    \'animals\': ["Flamingo", "Horse", None, "Centipede"]})\n        >>> table = pa.Table.from_pandas(df)\n        >>> for i in table.itercolumns():\n        ...     print(i.null_count)\n        ...\n        2\n        1\n        ',
    '_Tabular.sort_by (line 1920)': '\n        Sort the Table or RecordBatch by one or multiple columns.\n\n        Parameters\n        ----------\n        sorting : str or list[tuple(name, order)]\n            Name of the column to use to sort (ascending), or\n            a list of multiple sorting conditions where\n            each entry is a tuple with column name\n            and sorting order ("ascending" or "descending")\n        **kwargs : dict, optional\n            Additional sorting options.\n            As allowed by :class:`SortOptions`\n\n        Returns\n        -------\n        Table or RecordBatch\n            A new tabular object sorted according to the sort keys.\n\n        Examples\n        --------\n        Table (works similarly for RecordBatch)\n\n        >>> import pandas as pd\n        >>> import pyarrow as pa\n        >>> df = pd.DataFrame({\'year\': [2020, 2022, 2021, 2022, 2019, 2021],\n        ...                    \'n_legs\': [2, 2, 4, 4, 5, 100],\n        ...                    \'animal\': ["Flamingo", "Parrot", "Dog", "Horse",\n        ...                    "Brittle stars", "Centipede"]})\n        >>> table = pa.Table.from_pandas(df)\n        >>> table.sort_by(\'animal\')\n        pyarrow.Table\n        year: int64\n        n_legs: int64\n        animal: string\n        ----\n        year: [[2019,2021,2021,2020,2022,2022]]\n        n_legs: [[5,100,4,2,4,2]]\n        animal: [["Brittle stars","Centipede","Dog","Flamingo","Horse","Parrot"]]\n        ',
    '_Tabular.take (line 1970)': '\n        Select rows from a Table or RecordBatch.\n\n        See :func:`pyarrow.compute.take` for full usage.\n\n        Parameters\n        ----------\n        indices : Array or array-like\n            The indices in the tabular object whose rows will be returned.\n\n        Returns\n        -------\n        Table or RecordBatch\n            A tabular object with the same schema, containing the taken rows.\n\n        Examples\n        --------\n        Table (works similarly for RecordBatch)\n\n        >>> import pyarrow as pa\n        >>> import pandas as pd\n        >>> df = pd.DataFrame({\'year\': [2020, 2022, 2019, 2021],\n        ...                    \'n_legs\': [2, 4, 5, 100],\n        ...                    \'animals\': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})\n        >>> table = pa.Table.from_pandas(df)\n        >>> table.take([1,3])\n        pyarrow.Table\n        year: int64\n        n_legs: int64\n        animals: string\n        ----\n        year: [[2022,2021]]\n        n_legs: [[4,100]]\n        animals: [["Horse","Centipede"]]\n        ',
    '_Tabular.to_pydict (line 2008)': '\n        Convert the Table or RecordBatch to a dict or OrderedDict.\n\n        Returns\n        -------\n        dict\n\n        Examples\n        --------\n        Table (works similarly for RecordBatch)\n\n        >>> import pyarrow as pa\n        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])\n        >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])\n        >>> table = pa.Table.from_arrays([n_legs, animals], names=["n_legs", "animals"])\n        >>> table.to_pydict()\n        {\'n_legs\': [2, 2, 4, 4, 5, 100], \'animals\': [\'Flamingo\', \'Parrot\', ..., \'Centipede\']}\n        ',
    '_Tabular.to_pylist (line 2034)': '\n        Convert the Table or RecordBatch to a list of rows / dictionaries.\n\n        Returns\n        -------\n        list\n\n        Examples\n        --------\n        Table (works similarly for RecordBatch)\n\n        >>> import pyarrow as pa\n        >>> data = [[2, 4, 5, 100],\n        ...         ["Flamingo", "Horse", "Brittle stars", "Centipede"]]\n        >>> table = pa.table(data, names=["n_legs", "animals"])\n        >>> table.to_pylist()\n        [{\'n_legs\': 2, \'animals\': \'Flamingo\'}, {\'n_legs\': 4, \'animals\': \'Horse\'}, ...\n        ',
    'array (line 122)': '\n    Create pyarrow.Array instance from a Python object.\n\n    Parameters\n    ----------\n    obj : sequence, iterable, ndarray, pandas.Series, Arrow-compatible array\n        If both type and size are specified may be a single use iterable. If\n        not strongly-typed, Arrow type will be inferred for resulting array.\n        Any Arrow-compatible array that implements the Arrow PyCapsule Protocol\n        (has an ``__arrow_c_array__`` method) can be passed as well.\n    type : pyarrow.DataType\n        Explicit type to attempt to coerce to, otherwise will be inferred from\n        the data.\n    mask : array[bool], optional\n        Indicate which values are null (True) or not null (False).\n    size : int64, optional\n        Size of the elements. If the input is larger than size bail at this\n        length. For iterators, if size is larger than the input iterator this\n        will be treated as a "max size", but will involve an initial allocation\n        of size followed by a resize to the actual size (so if you know the\n        exact size specifying it correctly will give you better performance).\n    from_pandas : bool, default None\n        Use pandas\'s semantics for inferring nulls from values in\n        ndarray-like data. If passed, the mask tasks precedence, but\n        if a value is unmasked (not-null), but still null according to\n        pandas semantics, then it is null. Defaults to False if not\n        passed explicitly by user, or True if a pandas object is\n        passed in.\n    safe : bool, default True\n        Check for overflows or other unsafe conversions.\n    memory_pool : pyarrow.MemoryPool, optional\n        If not passed, will allocate memory from the currently-set default\n        memory pool.\n\n    Returns\n    -------\n    array : pyarrow.Array or pyarrow.ChunkedArray\n        A ChunkedArray instead of an Array is returned if:\n\n        - the object data overflowed binary storage.\n        - the object\'s ``__arrow_array__`` protocol method returned a chunked\n          array.\n\n    Notes\n    -----\n    Timezone will be preserved in the returned array for timezone-aware data,\n    else no timezone will be returned for naive timestamps.\n    Internally, UTC values are stored for timezone-aware data with the\n    timezone set in the data type.\n\n    Pandas\'s DateOffsets and dateutil.relativedelta.relativedelta are by\n    default converted as MonthDayNanoIntervalArray. relativedelta leapdays\n    are ignored as are all absolute fields on both objects. datetime.timedelta\n    can also be converted to MonthDayNanoIntervalArray but this requires\n    passing MonthDayNanoIntervalType explicitly.\n\n    Converting to dictionary array will promote to a wider integer type for\n    indices if the number of distinct values cannot be represented, even if\n    the index type was explicitly set. This means that if there are more than\n    127 values the returned dictionary array\'s index type will be at least\n    pa.int16() even if pa.int8() was passed to the function. Note that an\n    explicit index type will not be demoted even if it is wider than required.\n\n    Examples\n    --------\n    >>> import pandas as pd\n    >>> import pyarrow as pa\n    >>> pa.array(pd.Series([1, 2]))\n    <pyarrow.lib.Int64Array object at ...>\n    [\n      1,\n      2\n    ]\n\n    >>> pa.array(["a", "b", "a"], type=pa.dictionary(pa.int8(), pa.string()))\n    <pyarrow.lib.DictionaryArray object at ...>\n    ...\n    -- dictionary:\n      [\n        "a",\n        "b"\n      ]\n    -- indices:\n      [\n        0,\n        1,\n        0\n      ]\n\n    >>> import numpy as np\n    >>> pa.array(pd.Series([1, 2]), mask=np.array([0, 1], dtype=bool))\n    <pyarrow.lib.Int64Array object at ...>\n    [\n      1,\n      null\n    ]\n\n    >>> arr = pa.array(range(1024), type=pa.dictionary(pa.int8(), pa.int64()))\n    >>> arr.type.index_type\n    DataType(int16)\n    ',
    'binary (line 4241)': "\n    Create variable-length or fixed size binary type.\n\n    Parameters\n    ----------\n    length : int, optional, default -1\n        If length == -1 then return a variable length binary type. If length is\n        greater than or equal to 0 then return a fixed size binary type of\n        width `length`.\n\n    Examples\n    --------\n    Create an instance of a variable-length binary type:\n\n    >>> import pyarrow as pa\n    >>> pa.binary()\n    DataType(binary)\n\n    and use the variable-length binary type to create an array:\n\n    >>> pa.array(['foo', 'bar', 'baz'], type=pa.binary())\n    <pyarrow.lib.BinaryArray object at ...>\n    [\n      666F6F,\n      626172,\n      62617A\n    ]\n\n    Create an instance of a fixed-size binary type:\n\n    >>> pa.binary(3)\n    FixedSizeBinaryType(fixed_size_binary[3])\n\n    and use the fixed-length binary type to create an array:\n\n    >>> pa.array(['foo', 'bar', 'baz'], type=pa.binary(3))\n    <pyarrow.lib.FixedSizeBinaryArray object at ...>\n    [\n      666F6F,\n      626172,\n      62617A\n    ]\n    ",
    'bool_ (line 3451)': "\n    Create instance of boolean type.\n\n    Examples\n    --------\n    Create an instance of a boolean type:\n\n    >>> import pyarrow as pa\n    >>> pa.bool_()\n    DataType(bool)\n    >>> print(pa.bool_())\n    bool\n\n    Create a ``Field`` type with a boolean type\n    and a name:\n\n    >>> pa.field('bool_field', pa.bool_())\n    pyarrow.Field<bool_field: bool>\n    ",
    'chunked_array (line 1331)': '\n    Construct chunked array from list of array-like objects\n\n    Parameters\n    ----------\n    arrays : Array, list of Array, or array-like\n        Must all be the same data type. Can be empty only if type also passed.\n    type : DataType or string coercible to DataType\n\n    Returns\n    -------\n    ChunkedArray\n\n    Examples\n    --------\n    >>> import pyarrow as pa\n    >>> pa.chunked_array([], type=pa.int8())\n    <pyarrow.lib.ChunkedArray object at ...>\n    [\n    ...\n    ]\n\n    >>> pa.chunked_array([[2, 2, 4], [4, 5, 100]])\n    <pyarrow.lib.ChunkedArray object at ...>\n    [\n      [\n        2,\n        2,\n        4\n      ],\n      [\n        4,\n        5,\n        100\n      ]\n    ]\n    ',
    'concat_arrays (line 3729)': '\n    Concatenate the given arrays.\n\n    The contents of the input arrays are copied into the returned array.\n\n    Raises\n    ------\n    ArrowInvalid\n        If not all of the arrays have the same type.\n\n    Parameters\n    ----------\n    arrays : iterable of pyarrow.Array\n        Arrays to concatenate, must be identically typed.\n    memory_pool : MemoryPool, default None\n        For memory allocations. If None, the default pool is used.\n\n    Examples\n    --------\n    >>> import pyarrow as pa\n    >>> arr1 = pa.array([2, 4, 5, 100])\n    >>> arr2 = pa.array([2, 4])\n    >>> pa.concat_arrays([arr1, arr2])\n    <pyarrow.lib.Int64Array object at ...>\n    [\n      2,\n      4,\n      5,\n      100,\n      2,\n      4\n    ]\n\n    ',
    'concat_tables (line 5232)': '\n    Concatenate pyarrow.Table objects.\n\n    If promote_options="none", a zero-copy concatenation will be performed. The schemas\n    of all the Tables must be the same (except the metadata), otherwise an\n    exception will be raised. The result Table will share the metadata with the\n    first table.\n\n    If promote_options="default", any null type arrays will be casted to the type of other\n    arrays in the column of the same name. If a table is missing a particular\n    field, null values of the appropriate type will be generated to take the\n    place of the missing field. The new schema will share the metadata with the\n    first table. Each field in the new schema will share the metadata with the\n    first table which has the field defined. Note that type promotions may\n    involve additional allocations on the given ``memory_pool``.\n\n    If promote_options="permissive", the behavior of default plus types will be promoted\n    to the common denominator that fits all the fields.\n\n    Parameters\n    ----------\n    tables : iterable of pyarrow.Table objects\n        Pyarrow tables to concatenate into a single Table.\n    memory_pool : MemoryPool, default None\n        For memory allocations, if required, otherwise use default pool.\n    promote_options : str, default none\n        Accepts strings "none", "default" and "permissive".\n    **kwargs : dict, optional\n\n    Examples\n    --------\n    >>> import pyarrow as pa\n    >>> t1 = pa.table([\n    ...     pa.array([2, 4, 5, 100]),\n    ...     pa.array(["Flamingo", "Horse", "Brittle stars", "Centipede"])\n    ...     ], names=[\'n_legs\', \'animals\'])\n    >>> t2 = pa.table([\n    ...     pa.array([2, 4]),\n    ...     pa.array(["Parrot", "Dog"])\n    ...     ], names=[\'n_legs\', \'animals\'])\n    >>> pa.concat_tables([t1,t2])\n    pyarrow.Table\n    n_legs: int64\n    animals: string\n    ----\n    n_legs: [[2,4,5,100],[2,4]]\n    animals: [["Flamingo","Horse","Brittle stars","Centipede"],["Parrot","Dog"]]\n\n    ',
    'create_memory_map (line 1063)': "\n    Create a file of the given size and memory-map it.\n\n    Parameters\n    ----------\n    path : str\n        The file path to create, on the local filesystem.\n    size : int\n        The file size to create.\n\n    Returns\n    -------\n    mmap : MemoryMappedFile\n\n    Examples\n    --------\n    Create a file with a memory map:\n\n    >>> import pyarrow as pa\n    >>> with pa.create_memory_map('example_mmap_create.dat', 27) as mmap:\n    ...     mmap.write(b'Create a memory-mapped file')\n    ...     mmap.read_at(10, 9)\n    ...\n    27\n    b'memory-map'\n    ",
    'date32 (line 3979)': '\n    Create instance of 32-bit date (days since UNIX epoch 1970-01-01).\n\n    Examples\n    --------\n    Create an instance of 32-bit date type:\n\n    >>> import pyarrow as pa\n    >>> pa.date32()\n    DataType(date32[day])\n\n    Create a scalar with 32-bit date type:\n\n    >>> from datetime import date\n    >>> pa.scalar(date(2012, 1, 1), type=pa.date32())\n    <pyarrow.Date32Scalar: datetime.date(2012, 1, 1)>\n    ',
    'date64 (line 4000)': '\n    Create instance of 64-bit date (milliseconds since UNIX epoch 1970-01-01).\n\n    Examples\n    --------\n    Create an instance of 64-bit date type:\n\n    >>> import pyarrow as pa\n    >>> pa.date64()\n    DataType(date64[ms])\n\n    Create a scalar with 64-bit date type:\n\n    >>> from datetime import datetime\n    >>> pa.scalar(datetime(2012, 1, 1), type=pa.date64())\n    <pyarrow.Date64Scalar: datetime.date(2012, 1, 1)>\n    ',
    'decimal128 (line 4105)': "\n    Create decimal type with precision and scale and 128-bit width.\n\n    Arrow decimals are fixed-point decimal numbers encoded as a scaled\n    integer.  The precision is the number of significant digits that the\n    decimal type can represent; the scale is the number of digits after\n    the decimal point (note the scale can be negative).\n\n    As an example, ``decimal128(7, 3)`` can exactly represent the numbers\n    1234.567 and -1234.567 (encoded internally as the 128-bit integers\n    1234567 and -1234567, respectively), but neither 12345.67 nor 123.4567.\n\n    ``decimal128(5, -3)`` can exactly represent the number 12345000\n    (encoded internally as the 128-bit integer 12345), but neither\n    123450000 nor 1234500.\n\n    If you need a precision higher than 38 significant digits, consider\n    using ``decimal256``.\n\n    Parameters\n    ----------\n    precision : int\n        Must be between 1 and 38\n    scale : int\n\n    Returns\n    -------\n    decimal_type : Decimal128Type\n\n    Examples\n    --------\n    Create an instance of decimal type:\n\n    >>> import pyarrow as pa\n    >>> pa.decimal128(5, 2)\n    Decimal128Type(decimal128(5, 2))\n\n    Create an array with decimal type:\n\n    >>> import decimal\n    >>> a = decimal.Decimal('123.45')\n    >>> pa.array([a], pa.decimal128(5, 2))\n    <pyarrow.lib.Decimal128Array object at ...>\n    [\n      123.45\n    ]\n    ",
    'default_memory_pool (line 124)': '\n    Return the process-global memory pool.\n\n    Examples\n    --------\n    >>> default_memory_pool()\n    <pyarrow.MemoryPool backend_name=... bytes_allocated=0 max_memory=...>\n    ',
    'dictionary (line 4576)': '\n    Dictionary (categorical, or simply encoded) type.\n\n    Parameters\n    ----------\n    index_type : DataType\n    value_type : DataType\n    ordered : bool\n\n    Returns\n    -------\n    type : DictionaryType\n\n    Examples\n    --------\n    Create an instance of dictionary type:\n\n    >>> import pyarrow as pa\n    >>> pa.dictionary(pa.int64(), pa.utf8())\n    DictionaryType(dictionary<values=string, indices=int64, ordered=0>)\n\n    Use dictionary type to create an array:\n\n    >>> pa.array(["a", "b", None, "d"], pa.dictionary(pa.int64(), pa.utf8()))\n    <pyarrow.lib.DictionaryArray object at ...>\n    ...\n    -- dictionary:\n      [\n        "a",\n        "b",\n        "d"\n      ]\n    -- indices:\n      [\n        0,\n        1,\n        null,\n        2\n      ]\n    ',
    'duration (line 3908)': "\n    Create instance of a duration type with unit resolution.\n\n    Parameters\n    ----------\n    unit : str\n        One of 's' [second], 'ms' [millisecond], 'us' [microsecond], or\n        'ns' [nanosecond].\n\n    Returns\n    -------\n    type : pyarrow.DurationType\n\n    Examples\n    --------\n    Create an instance of duration type:\n\n    >>> import pyarrow as pa\n    >>> pa.duration('us')\n    DurationType(duration[us])\n    >>> pa.duration('s')\n    DurationType(duration[s])\n\n    Create an array with duration type:\n\n    >>> pa.array([0, 1, 2], type=pa.duration('s'))\n    <pyarrow.lib.DurationArray object at ...>\n    [\n      0,\n      1,\n      2\n    ]\n    ",
    'field (line 3353)': '\n    Create a pyarrow.Field instance.\n\n    Parameters\n    ----------\n    name : str or bytes\n        Name of the field.\n    type : pyarrow.DataType\n        Arrow datatype of the field.\n    nullable : bool, default True\n        Whether the field\'s values are nullable.\n    metadata : dict, default None\n        Optional field metadata, the keys and values must be coercible to\n        bytes.\n\n    Returns\n    -------\n    field : pyarrow.Field\n\n    Examples\n    --------\n    Create an instance of pyarrow.Field:\n\n    >>> import pyarrow as pa\n    >>> pa.field(\'key\', pa.int32())\n    pyarrow.Field<key: int32>\n    >>> pa.field(\'key\', pa.int32(), nullable=False)\n    pyarrow.Field<key: int32 not null>\n\n    >>> field = pa.field(\'key\', pa.int32(),\n    ...                  metadata={"key": "Something important"})\n    >>> field\n    pyarrow.Field<key: int32>\n    >>> field.metadata\n    {b\'key\': b\'Something important\'}\n\n    Use the field to create a struct type:\n\n    >>> pa.struct([field])\n    StructType(struct<key: int32>)\n    ',
    'fixed_shape_tensor (line 4857)': '\n    Create instance of fixed shape tensor extension type with shape and optional\n    names of tensor dimensions and indices of the desired logical\n    ordering of dimensions.\n\n    Parameters\n    ----------\n    value_type : DataType\n        Data type of individual tensor elements.\n    shape : tuple or list of integers\n        The physical shape of the contained tensors.\n    dim_names : tuple or list of strings, default None\n        Explicit names to tensor dimensions.\n    permutation : tuple or list integers, default None\n        Indices of the desired ordering of the original dimensions.\n        The indices contain a permutation of the values ``[0, 1, .., N-1]`` where\n        N is the number of dimensions. The permutation indicates which dimension\n        of the logical layout corresponds to which dimension of the physical tensor.\n        For more information on this parameter see\n        :ref:`fixed_shape_tensor_extension`.\n\n    Examples\n    --------\n    Create an instance of fixed shape tensor extension type:\n\n    >>> import pyarrow as pa\n    >>> tensor_type = pa.fixed_shape_tensor(pa.int32(), [2, 2])\n    >>> tensor_type\n    FixedShapeTensorType(extension<arrow.fixed_shape_tensor[value_type=int32, shape=[2,2]]>)\n\n    Inspect the data type:\n\n    >>> tensor_type.value_type\n    DataType(int32)\n    >>> tensor_type.shape\n    [2, 2]\n\n    Create a table with fixed shape tensor extension array:\n\n    >>> arr = [[1, 2, 3, 4], [10, 20, 30, 40], [100, 200, 300, 400]]\n    >>> storage = pa.array(arr, pa.list_(pa.int32(), 4))\n    >>> tensor = pa.ExtensionArray.from_storage(tensor_type, storage)\n    >>> pa.table([tensor], names=["tensor_array"])\n    pyarrow.Table\n    tensor_array: extension<arrow.fixed_shape_tensor[value_type=int32, shape=[2,2]]>\n    ----\n    tensor_array: [[[1,2,3,4],[10,20,30,40],[100,200,300,400]]]\n\n    Create an instance of fixed shape tensor extension type with names\n    of tensor dimensions:\n\n    >>> tensor_type = pa.fixed_shape_tensor(pa.int8(), (2, 2, 3),\n    ...                                     dim_names=[\'C\', \'H\', \'W\'])\n    >>> tensor_type.dim_names\n    [\'C\', \'H\', \'W\']\n\n    Create an instance of fixed shape tensor extension type with\n    permutation:\n\n    >>> tensor_type = pa.fixed_shape_tensor(pa.int8(), (2, 2, 3),\n    ...                                     permutation=[0, 2, 1])\n    >>> tensor_type.permutation\n    [0, 2, 1]\n\n    Returns\n    -------\n    type : FixedShapeTensorType\n    ',
    'float16 (line 4021)': '\n    Create half-precision floating point type.\n\n    Examples\n    --------\n    Create an instance of float16 type:\n\n    >>> import pyarrow as pa\n    >>> pa.float16()\n    DataType(halffloat)\n    >>> print(pa.float16())\n    halffloat\n\n    Create an array with float16 type:\n\n    >>> arr = np.array([1.5, np.nan], dtype=np.float16)\n    >>> a = pa.array(arr, type=pa.float16())\n    >>> a\n    <pyarrow.lib.HalfFloatArray object at ...>\n    [\n      15872,\n      32256\n    ]\n    >>> a.to_pylist()\n    [1.5, nan]\n    ',
    'float32 (line 4051)': '\n    Create single-precision floating point type.\n\n    Examples\n    --------\n    Create an instance of float32 type:\n\n    >>> import pyarrow as pa\n    >>> pa.float32()\n    DataType(float)\n    >>> print(pa.float32())\n    float\n\n    Create an array with float32 type:\n\n    >>> pa.array([0.0, 1.0, 2.0], type=pa.float32())\n    <pyarrow.lib.FloatArray object at ...>\n    [\n      0,\n      1,\n      2\n    ]\n    ',
    'float64 (line 4078)': '\n    Create double-precision floating point type.\n\n    Examples\n    --------\n    Create an instance of float64 type:\n\n    >>> import pyarrow as pa\n    >>> pa.float64()\n    DataType(double)\n    >>> print(pa.float64())\n    double\n\n    Create an array with float64 type:\n\n    >>> pa.array([0.0, 1.0, 2.0], type=pa.float64())\n    <pyarrow.lib.DoubleArray object at ...>\n    [\n      0,\n      1,\n      2\n    ]\n    ',
    'from_numpy_dtype (line 5119)': "\n    Convert NumPy dtype to pyarrow.DataType.\n\n    Parameters\n    ----------\n    dtype : the numpy dtype to convert\n\n\n    Examples\n    --------\n    Create a pyarrow DataType from NumPy dtype:\n\n    >>> import pyarrow as pa\n    >>> import numpy as np\n    >>> pa.from_numpy_dtype(np.dtype('float16'))\n    DataType(halffloat)\n    >>> pa.from_numpy_dtype('U')\n    DataType(string)\n    >>> pa.from_numpy_dtype(bool)\n    DataType(bool)\n    >>> pa.from_numpy_dtype(np.str_)\n    DataType(string)\n    ",
    'input_stream (line 2615)': '\n    Create an Arrow input stream.\n\n    Parameters\n    ----------\n    source : str, Path, buffer, or file-like object\n        The source to open for reading.\n    compression : str optional, default \'detect\'\n        The compression algorithm to use for on-the-fly decompression.\n        If "detect" and source is a file path, then compression will be\n        chosen based on the file extension.\n        If None, no compression will be applied.\n        Otherwise, a well-known algorithm name must be supplied (e.g. "gzip").\n    buffer_size : int, default None\n        If None or 0, no buffering will happen. Otherwise the size of the\n        temporary read buffer.\n\n    Examples\n    --------\n    Create a readable BufferReader (NativeFile) from a Buffer or a memoryview object:\n\n    >>> import pyarrow as pa\n    >>> buf = memoryview(b"some data")\n    >>> with pa.input_stream(buf) as stream:\n    ...     stream.read(4)\n    ...\n    b\'some\'\n\n    Create a readable OSFile (NativeFile) from a string or file path:\n\n    >>> import gzip\n    >>> with gzip.open(\'example.gz\', \'wb\') as f:\n    ...     f.write(b\'some data\')\n    ...\n    9\n    >>> with pa.input_stream(\'example.gz\') as stream:\n    ...     stream.read()\n    ...\n    b\'some data\'\n\n    Create a readable PythonFile (NativeFile) from a a Python file object:\n\n    >>> with open(\'example.txt\', mode=\'w\') as f:\n    ...     f.write(\'some text\')\n    ...\n    9\n    >>> with pa.input_stream(\'example.txt\') as stream:\n    ...     stream.read(6)\n    ...\n    b\'some t\'\n    ',
    'int16 (line 3555)': '\n    Create instance of signed int16 type.\n\n    Examples\n    --------\n    Create an instance of int16 type:\n\n    >>> import pyarrow as pa\n    >>> pa.int16()\n    DataType(int16)\n    >>> print(pa.int16())\n    int16\n\n    Create an array with int16 type:\n\n    >>> pa.array([0, 1, 2], type=pa.int16())\n    <pyarrow.lib.Int16Array object at ...>\n    [\n      0,\n      1,\n      2\n    ]\n    ',
    'int32 (line 3609)': '\n    Create instance of signed int32 type.\n\n    Examples\n    --------\n    Create an instance of int32 type:\n\n    >>> import pyarrow as pa\n    >>> pa.int32()\n    DataType(int32)\n    >>> print(pa.int32())\n    int32\n\n    Create an array with int32 type:\n\n    >>> pa.array([0, 1, 2], type=pa.int32())\n    <pyarrow.lib.Int32Array object at ...>\n    [\n      0,\n      1,\n      2\n    ]\n    ',
    'int64 (line 3663)': '\n    Create instance of signed int64 type.\n\n    Examples\n    --------\n    Create an instance of int64 type:\n\n    >>> import pyarrow as pa\n    >>> pa.int64()\n    DataType(int64)\n    >>> print(pa.int64())\n    int64\n\n    Create an array with int64 type:\n\n    >>> pa.array([0, 1, 2], type=pa.int64())\n    <pyarrow.lib.Int64Array object at ...>\n    [\n      0,\n      1,\n      2\n    ]\n    ',
    'int8 (line 3501)': '\n    Create instance of signed int8 type.\n\n    Examples\n    --------\n    Create an instance of int8 type:\n\n    >>> import pyarrow as pa\n    >>> pa.int8()\n    DataType(int8)\n    >>> print(pa.int8())\n    int8\n\n    Create an array with int8 type:\n\n    >>> pa.array([0, 1, 2], type=pa.int8())\n    <pyarrow.lib.Int8Array object at ...>\n    [\n      0,\n      1,\n      2\n    ]\n    ',
    'large_binary (line 4293)': "\n    Create large variable-length binary type.\n\n    This data type may not be supported by all Arrow implementations.  Unless\n    you need to represent data larger than 2GB, you should prefer binary().\n\n    Examples\n    --------\n    Create an instance of large variable-length binary type:\n\n    >>> import pyarrow as pa\n    >>> pa.large_binary()\n    DataType(large_binary)\n\n    and use the type to create an array:\n\n    >>> pa.array(['foo', 'bar', 'baz'], type=pa.large_binary())\n    <pyarrow.lib.LargeBinaryArray object at ...>\n    [\n      666F6F,\n      626172,\n      62617A\n    ]\n    ",
    'large_list (line 4444)': '\n    Create LargeListType instance from child data type or field.\n\n    This data type may not be supported by all Arrow implementations.\n    Unless you need to represent data larger than 2**31 elements, you should\n    prefer list_().\n\n    Parameters\n    ----------\n    value_type : DataType or Field\n\n    Returns\n    -------\n    list_type : DataType\n\n    Examples\n    --------\n    Create an instance of LargeListType:\n\n    >>> import pyarrow as pa\n    >>> pa.large_list(pa.int8())\n    LargeListType(large_list<item: int8>)\n\n    Use the LargeListType to create an array:\n\n    >>> pa.array([[-1, 3]] * 5, type=pa.large_list(pa.int8()))\n    <pyarrow.lib.LargeListArray object at ...>\n    [\n      [\n        -1,\n        3\n      ],\n      [\n        -1,\n        3\n      ],\n    ...\n    ',
    'large_string (line 4321)': '\n    Create large UTF8 variable-length string type.\n\n    This data type may not be supported by all Arrow implementations.  Unless\n    you need to represent data larger than 2GB, you should prefer string().\n\n    Examples\n    --------\n    Create an instance of large UTF8 variable-length binary type:\n\n    >>> import pyarrow as pa\n    >>> pa.large_string()\n    DataType(large_string)\n\n    and use the type to create an array:\n\n    >>> pa.array([\'foo\', \'bar\'] * 50, type=pa.large_string())\n    <pyarrow.lib.LargeStringArray object at ...>\n    [\n      "foo",\n      "bar",\n      ...\n      "foo",\n      "bar"\n    ]\n    ',
    'large_utf8 (line 4351)': '\n    Alias for large_string().\n\n    Examples\n    --------\n    Create an instance of large UTF8 variable-length binary type:\n\n    >>> import pyarrow as pa\n    >>> pa.large_utf8()\n    DataType(large_string)\n\n    and use the type to create an array:\n\n    >>> pa.array([\'foo\', \'bar\'] * 50, type=pa.large_utf8())\n    <pyarrow.lib.LargeStringArray object at ...>\n    [\n      "foo",\n      "bar",\n      ...\n      "foo",\n      "bar"\n    ]\n    ',
    'list_ (line 4378)': "\n    Create ListType instance from child data type or field.\n\n    Parameters\n    ----------\n    value_type : DataType or Field\n    list_size : int, optional, default -1\n        If length == -1 then return a variable length list type. If length is\n        greater than or equal to 0 then return a fixed size list type.\n\n    Returns\n    -------\n    list_type : DataType\n\n    Examples\n    --------\n    Create an instance of ListType:\n\n    >>> import pyarrow as pa\n    >>> pa.list_(pa.string())\n    ListType(list<item: string>)\n    >>> pa.list_(pa.int32(), 2)\n    FixedSizeListType(fixed_size_list<item: int32>[2])\n\n    Use the ListType to create a scalar:\n\n    >>> pa.scalar(['foo', None], type=pa.list_(pa.string(), 2))\n    <pyarrow.FixedSizeListScalar: ['foo', None]>\n\n    or an array:\n\n    >>> pa.array([[1, 2], [3, 4]], pa.list_(pa.int32(), 2))\n    <pyarrow.lib.FixedSizeListArray object at ...>\n    [\n      [\n        1,\n        2\n      ],\n      [\n        3,\n        4\n      ]\n    ]\n    ",
    'map_ (line 4501)': '\n    Create MapType instance from key and item data types or fields.\n\n    Parameters\n    ----------\n    key_type : DataType or Field\n    item_type : DataType or Field\n    keys_sorted : bool\n\n    Returns\n    -------\n    map_type : DataType\n\n    Examples\n    --------\n    Create an instance of MapType:\n\n    >>> import pyarrow as pa\n    >>> pa.map_(pa.string(), pa.int32())\n    MapType(map<string, int32>)\n    >>> pa.map_(pa.string(), pa.int32(), keys_sorted=True)\n    MapType(map<string, int32, keys_sorted>)\n\n    Use MapType to create an array:\n\n    >>> data = [[{\'key\': \'a\', \'value\': 1}, {\'key\': \'b\', \'value\': 2}], [{\'key\': \'c\', \'value\': 3}]]\n    >>> pa.array(data, type=pa.map_(pa.string(), pa.int32(), keys_sorted=True))\n    <pyarrow.lib.MapArray object at ...>\n    [\n      keys:\n      [\n        "a",\n        "b"\n      ]\n      values:\n      [\n        1,\n        2\n      ],\n      keys:\n      [\n        "c"\n      ]\n      values:\n      [\n        3\n      ]\n    ]\n    ',
    'memory_map (line 1021)': "\n    Open memory map at file path. Size of the memory map cannot change.\n\n    Parameters\n    ----------\n    path : str\n    mode : {'r', 'r+', 'w'}, default 'r'\n        Whether the file is opened for reading ('r'), writing ('w')\n        or both ('r+').\n\n    Returns\n    -------\n    mmap : MemoryMappedFile\n\n    Examples\n    --------\n    Reading from a memory map without any memory allocation or copying:\n\n    >>> import pyarrow as pa\n    >>> with pa.output_stream('example_mmap.txt') as stream:\n    ...     stream.write(b'Constructing a buffer referencing the mapped memory')\n    ...\n    51\n    >>> with pa.memory_map('example_mmap.txt') as mmap:\n    ...     mmap.read_at(6,45)\n    ...\n    b'memory'\n    ",
    'month_day_nano_interval (line 3958)': '\n    Create instance of an interval type representing months, days and\n    nanoseconds between two dates.\n\n    Examples\n    --------\n    Create an instance of an month_day_nano_interval type:\n\n    >>> import pyarrow as pa\n    >>> pa.month_day_nano_interval()\n    DataType(month_day_nano_interval)\n\n    Create a scalar with month_day_nano_interval type:\n\n    >>> pa.scalar((1, 15, -30), type=pa.month_day_nano_interval())\n    <pyarrow.MonthDayNanoIntervalScalar: MonthDayNano(months=1, days=15, nanoseconds=-30)>\n    ',
    'null (line 3429)': "\n    Create instance of null type.\n\n    Examples\n    --------\n    Create an instance of a null type:\n\n    >>> import pyarrow as pa\n    >>> pa.null()\n    DataType(null)\n    >>> print(pa.null())\n    null\n\n    Create a ``Field`` type with a null type and a name:\n\n    >>> pa.field('null_field', pa.null())\n    pyarrow.Field<null_field: null>\n    ",
    'nulls (line 377)': '\n    Create a strongly-typed Array instance with all elements null.\n\n    Parameters\n    ----------\n    size : int\n        Array length.\n    type : pyarrow.DataType, default None\n        Explicit type for the array. By default use NullType.\n    memory_pool : MemoryPool, default None\n        Arrow MemoryPool to use for allocations. Uses the default memory\n        pool if not passed.\n\n    Returns\n    -------\n    arr : Array\n\n    Examples\n    --------\n    >>> import pyarrow as pa\n    >>> pa.nulls(10)\n    <pyarrow.lib.NullArray object at ...>\n    10 nulls\n\n    >>> pa.nulls(3, pa.uint32())\n    <pyarrow.lib.UInt32Array object at ...>\n    [\n      null,\n      null,\n      null\n    ]\n    ',
    'output_stream (line 2701)': '\n    Create an Arrow output stream.\n\n    Parameters\n    ----------\n    source : str, Path, buffer, file-like object\n        The source to open for writing.\n    compression : str optional, default \'detect\'\n        The compression algorithm to use for on-the-fly compression.\n        If "detect" and source is a file path, then compression will be\n        chosen based on the file extension.\n        If None, no compression will be applied.\n        Otherwise, a well-known algorithm name must be supplied (e.g. "gzip").\n    buffer_size : int, default None\n        If None or 0, no buffering will happen. Otherwise the size of the\n        temporary write buffer.\n\n    Examples\n    --------\n    Create a writable NativeFile from a pyarrow Buffer:\n\n    >>> import pyarrow as pa\n    >>> data = b"buffer data"\n    >>> empty_obj = bytearray(11)\n    >>> buf = pa.py_buffer(empty_obj)\n    >>> with pa.output_stream(buf) as stream:\n    ...     stream.write(data)\n    ...\n    11\n    >>> with pa.input_stream(buf) as stream:\n    ...     stream.read(6)\n    ...\n    b\'buffer\'\n\n    or from a memoryview object:\n\n    >>> buf = memoryview(empty_obj)\n    >>> with pa.output_stream(buf) as stream:\n    ...     stream.write(data)\n    ...\n    11\n    >>> with pa.input_stream(buf) as stream:\n    ...     stream.read()\n    ...\n    b\'buffer data\'\n\n    Create a writable NativeFile from a string or file path:\n\n    >>> with pa.output_stream(\'example_second.txt\') as stream:\n    ...     stream.write(b\'Write some data\')\n    ...\n    15\n    >>> with pa.input_stream(\'example_second.txt\') as stream:\n    ...     stream.read()\n    ...\n    b\'Write some data\'\n    ',
    'record_batch (line 4943)': '\n    Create a pyarrow.RecordBatch from another Python data structure or sequence\n    of arrays.\n\n    Parameters\n    ----------\n    data : pandas.DataFrame, list, Arrow-compatible table\n        A DataFrame, list of arrays or chunked arrays, or a tabular object\n        implementing the Arrow PyCapsule Protocol (has an\n        ``__arrow_c_array__`` method).\n    names : list, default None\n        Column names if list of arrays passed as data. Mutually exclusive with\n        \'schema\' argument.\n    schema : Schema, default None\n        The expected schema of the RecordBatch. If not passed, will be inferred\n        from the data. Mutually exclusive with \'names\' argument.\n    metadata : dict or Mapping, default None\n        Optional metadata for the schema (if schema not passed).\n\n    Returns\n    -------\n    RecordBatch\n\n    See Also\n    --------\n    RecordBatch.from_arrays, RecordBatch.from_pandas, table\n\n    Examples\n    --------\n    >>> import pyarrow as pa\n    >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])\n    >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])\n    >>> names = ["n_legs", "animals"]\n\n    Creating a RecordBatch from a list of arrays with names:\n\n    >>> pa.record_batch([n_legs, animals], names=names)\n    pyarrow.RecordBatch\n    n_legs: int64\n    animals: string\n    ----\n    n_legs: [2,2,4,4,5,100]\n    animals: ["Flamingo","Parrot","Dog","Horse","Brittle stars","Centipede"]\n    >>> pa.record_batch([n_legs, animals], names=["n_legs", "animals"]).to_pandas()\n       n_legs        animals\n    0       2       Flamingo\n    1       2         Parrot\n    2       4            Dog\n    3       4          Horse\n    4       5  Brittle stars\n    5     100      Centipede\n\n    Creating a RecordBatch from a list of arrays with names and metadata:\n\n    >>> my_metadata={"n_legs": "How many legs does an animal have?"}\n    >>> pa.record_batch([n_legs, animals],\n    ...                  names=names,\n    ...                  metadata = my_metadata)\n    pyarrow.RecordBatch\n    n_legs: int64\n    animals: string\n    ----\n    n_legs: [2,2,4,4,5,100]\n    animals: ["Flamingo","Parrot","Dog","Horse","Brittle stars","Centipede"]\n    >>> pa.record_batch([n_legs, animals],\n    ...                  names=names,\n    ...                  metadata = my_metadata).schema\n    n_legs: int64\n    animals: string\n    -- schema metadata --\n    n_legs: \'How many legs does an animal have?\'\n\n    Creating a RecordBatch from a pandas DataFrame:\n\n    >>> import pandas as pd\n    >>> df = pd.DataFrame({\'year\': [2020, 2022, 2021, 2022],\n    ...                    \'month\': [3, 5, 7, 9],\n    ...                    \'day\': [1, 5, 9, 13],\n    ...                    \'n_legs\': [2, 4, 5, 100],\n    ...                    \'animals\': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})\n    >>> pa.record_batch(df)\n    pyarrow.RecordBatch\n    year: int64\n    month: int64\n    day: int64\n    n_legs: int64\n    animals: string\n    ----\n    year: [2020,2022,2021,2022]\n    month: [3,5,7,9]\n    day: [1,5,9,13]\n    n_legs: [2,4,5,100]\n    animals: ["Flamingo","Horse","Brittle stars","Centipede"]\n\n    >>> pa.record_batch(df).to_pandas()\n       year  month  day  n_legs        animals\n    0  2020      3    1       2       Flamingo\n    1  2022      5    5       4          Horse\n    2  2021      7    9       5  Brittle stars\n    3  2022      9   13     100      Centipede\n\n    Creating a RecordBatch from a pandas DataFrame with schema:\n\n    >>> my_schema = pa.schema([\n    ...     pa.field(\'n_legs\', pa.int64()),\n    ...     pa.field(\'animals\', pa.string())],\n    ...     metadata={"n_legs": "Number of legs per animal"})\n    >>> pa.record_batch(df, my_schema).schema\n    n_legs: int64\n    animals: string\n    -- schema metadata --\n    n_legs: \'Number of legs per animal\'\n    pandas: ...\n    >>> pa.record_batch(df, my_schema).to_pandas()\n       n_legs        animals\n    0       2       Flamingo\n    1       4          Horse\n    2       5  Brittle stars\n    3     100      Centipede\n    ',
    'register_extension_type (line 1794)': '\n    Register a Python extension type.\n\n    Registration is based on the extension name (so different registered types\n    need unique extension names). Registration needs an extension type\n    instance, but then works for any instance of the same subclass regardless\n    of parametrization of the type.\n\n    Parameters\n    ----------\n    ext_type : BaseExtensionType instance\n        The ExtensionType subclass to register.\n\n    Examples\n    --------\n    Define a UuidType extension type subclassing ExtensionType:\n\n    >>> import pyarrow as pa\n    >>> class UuidType(pa.ExtensionType):\n    ...    def __init__(self):\n    ...       pa.ExtensionType.__init__(self, pa.binary(16), "my_package.uuid")\n    ...    def __arrow_ext_serialize__(self):\n    ...       # since we don\'t have a parameterized type, we don\'t need extra\n    ...       # metadata to be deserialized\n    ...       return b\'\'\n    ...    @classmethod\n    ...    def __arrow_ext_deserialize__(self, storage_type, serialized):\n    ...       # return an instance of this subclass given the serialized\n    ...       # metadata.\n    ...       return UuidType()\n    ...\n\n    Register the extension type:\n\n    >>> pa.register_extension_type(UuidType())\n\n    Unregister the extension type:\n\n    >>> pa.unregister_extension_type("my_package.uuid")\n    ',
    'repeat (line 427)': '\n    Create an Array instance whose slots are the given scalar.\n\n    Parameters\n    ----------\n    value : Scalar-like object\n        Either a pyarrow.Scalar or any python object coercible to a Scalar.\n    size : int\n        Number of times to repeat the scalar in the output Array.\n    memory_pool : MemoryPool, default None\n        Arrow MemoryPool to use for allocations. Uses the default memory\n        pool if not passed.\n\n    Returns\n    -------\n    arr : Array\n\n    Examples\n    --------\n    >>> import pyarrow as pa\n    >>> pa.repeat(10, 3)\n    <pyarrow.lib.Int64Array object at ...>\n    [\n      10,\n      10,\n      10\n    ]\n\n    >>> pa.repeat([1, 2], 2)\n    <pyarrow.lib.ListArray object at ...>\n    [\n      [\n        1,\n        2\n      ],\n      [\n        1,\n        2\n      ]\n    ]\n\n    >>> pa.repeat("string", 3)\n    <pyarrow.lib.StringArray object at ...>\n    [\n      "string",\n      "string",\n      "string"\n    ]\n\n    >>> pa.repeat(pa.scalar({\'a\': 1, \'b\': [1, 2]}), 2)\n    <pyarrow.lib.StructArray object at ...>\n    -- is_valid: all not null\n    -- child 0 type: int64\n      [\n        1,\n        1\n      ]\n    -- child 1 type: list<item: int64>\n      [\n        [\n          1,\n          2\n        ],\n        [\n          1,\n          2\n        ]\n      ]\n    ',
    'scalar (line 1083)': '\n    Create a pyarrow.Scalar instance from a Python object.\n\n    Parameters\n    ----------\n    value : Any\n        Python object coercible to arrow\'s type system.\n    type : pyarrow.DataType\n        Explicit type to attempt to coerce to, otherwise will be inferred from\n        the value.\n    from_pandas : bool, default None\n        Use pandas\'s semantics for inferring nulls from values in\n        ndarray-like data. Defaults to False if not passed explicitly by user,\n        or True if a pandas object is passed in.\n    memory_pool : pyarrow.MemoryPool, optional\n        If not passed, will allocate memory from the currently-set default\n        memory pool.\n\n    Returns\n    -------\n    scalar : pyarrow.Scalar\n\n    Examples\n    --------\n    >>> import pyarrow as pa\n\n    >>> pa.scalar(42)\n    <pyarrow.Int64Scalar: 42>\n\n    >>> pa.scalar("string")\n    <pyarrow.StringScalar: \'string\'>\n\n    >>> pa.scalar([1, 2])\n    <pyarrow.ListScalar: [1, 2]>\n\n    >>> pa.scalar([1, 2], type=pa.list_(pa.int16()))\n    <pyarrow.ListScalar: [1, 2]>\n    ',
    'schema (line 5049)': "\n    Construct pyarrow.Schema from collection of fields.\n\n    Parameters\n    ----------\n    fields : iterable of Fields or tuples, or mapping of strings to DataTypes\n        Can also pass an object that implements the Arrow PyCapsule Protocol\n        for schemas (has an ``__arrow_c_schema__`` method).\n    metadata : dict, default None\n        Keys and values must be coercible to bytes.\n\n    Examples\n    --------\n    Create a Schema from iterable of tuples:\n\n    >>> import pyarrow as pa\n    >>> pa.schema([\n    ...     ('some_int', pa.int32()),\n    ...     ('some_string', pa.string()),\n    ...     pa.field('some_required_string', pa.string(), nullable=False)\n    ... ])\n    some_int: int32\n    some_string: string\n    some_required_string: string not null\n\n    Create a Schema from iterable of Fields:\n\n    >>> pa.schema([\n    ...     pa.field('some_int', pa.int32()),\n    ...     pa.field('some_string', pa.string())\n    ... ])\n    some_int: int32\n    some_string: string\n\n    Returns\n    -------\n    schema : pyarrow.Schema\n    ",
    'string (line 4191)': '\n    Create UTF8 variable-length string type.\n\n    Examples\n    --------\n    Create an instance of a string type:\n\n    >>> import pyarrow as pa\n    >>> pa.string()\n    DataType(string)\n\n    and use the string type to create an array:\n\n    >>> pa.array([\'foo\', \'bar\', \'baz\'], type=pa.string())\n    <pyarrow.lib.StringArray object at ...>\n    [\n      "foo",\n      "bar",\n      "baz"\n    ]\n    ',
    'struct (line 4635)': "\n    Create StructType instance from fields.\n\n    A struct is a nested type parameterized by an ordered sequence of types\n    (which can all be distinct), called its fields.\n\n    Parameters\n    ----------\n    fields : iterable of Fields or tuples, or mapping of strings to DataTypes\n        Each field must have a UTF8-encoded name, and these field names are\n        part of the type metadata.\n\n    Examples\n    --------\n    Create an instance of StructType from an iterable of tuples:\n\n    >>> import pyarrow as pa\n    >>> fields = [\n    ...     ('f1', pa.int32()),\n    ...     ('f2', pa.string()),\n    ... ]\n    >>> struct_type = pa.struct(fields)\n    >>> struct_type\n    StructType(struct<f1: int32, f2: string>)\n\n    Retrieve a field from a StructType:\n\n    >>> struct_type[0]\n    pyarrow.Field<f1: int32>\n    >>> struct_type['f1']\n    pyarrow.Field<f1: int32>\n\n    Create an instance of StructType from an iterable of Fields:\n\n    >>> fields = [\n    ...     pa.field('f1', pa.int32()),\n    ...     pa.field('f2', pa.string(), nullable=False),\n    ... ]\n    >>> pa.struct(fields)\n    StructType(struct<f1: int32, f2: string not null>)\n\n    Returns\n    -------\n    type : DataType\n    ",
    'table (line 5090)': '\n    Create a pyarrow.Table from a Python data structure or sequence of arrays.\n\n    Parameters\n    ----------\n    data : pandas.DataFrame, dict, list\n        A DataFrame, mapping of strings to Arrays or Python lists, or list of\n        arrays or chunked arrays.\n    names : list, default None\n        Column names if list of arrays passed as data. Mutually exclusive with\n        \'schema\' argument.\n    schema : Schema, default None\n        The expected schema of the Arrow Table. If not passed, will be inferred\n        from the data. Mutually exclusive with \'names\' argument.\n        If passed, the output will have exactly this schema (raising an error\n        when columns are not found in the data and ignoring additional data not\n        specified in the schema, when data is a dict or DataFrame).\n    metadata : dict or Mapping, default None\n        Optional metadata for the schema (if schema not passed).\n    nthreads : int, default None\n        For pandas.DataFrame inputs: if greater than 1, convert columns to\n        Arrow in parallel using indicated number of threads. By default,\n        this follows :func:`pyarrow.cpu_count` (may use up to system CPU count\n        threads).\n\n    Returns\n    -------\n    Table\n\n    See Also\n    --------\n    Table.from_arrays, Table.from_pandas, Table.from_pydict\n\n    Examples\n    --------\n    >>> import pyarrow as pa\n    >>> n_legs = pa.array([2, 4, 5, 100])\n    >>> animals = pa.array(["Flamingo", "Horse", "Brittle stars", "Centipede"])\n    >>> names = ["n_legs", "animals"]\n\n    Construct a Table from arrays:\n\n    >>> pa.table([n_legs, animals], names=names)\n    pyarrow.Table\n    n_legs: int64\n    animals: string\n    ----\n    n_legs: [[2,4,5,100]]\n    animals: [["Flamingo","Horse","Brittle stars","Centipede"]]\n\n    Construct a Table from arrays with metadata:\n\n    >>> my_metadata={"n_legs": "Number of legs per animal"}\n    >>> pa.table([n_legs, animals], names=names, metadata = my_metadata).schema\n    n_legs: int64\n    animals: string\n    -- schema metadata --\n    n_legs: \'Number of legs per animal\'\n\n    Construct a Table from pandas DataFrame:\n\n    >>> import pandas as pd\n    >>> df = pd.DataFrame({\'year\': [2020, 2022, 2019, 2021],\n    ...                    \'n_legs\': [2, 4, 5, 100],\n    ...                    \'animals\': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})\n    >>> pa.table(df)\n    pyarrow.Table\n    year: int64\n    n_legs: int64\n    animals: string\n    ----\n    year: [[2020,2022,2019,2021]]\n    n_legs: [[2,4,5,100]]\n    animals: [["Flamingo","Horse","Brittle stars","Centipede"]]\n\n    Construct a Table from pandas DataFrame with pyarrow schema:\n\n    >>> my_schema = pa.schema([\n    ...     pa.field(\'n_legs\', pa.int64()),\n    ...     pa.field(\'animals\', pa.string())],\n    ...     metadata={"n_legs": "Number of legs per animal"})\n    >>> pa.table(df, my_schema).schema\n    n_legs: int64\n    animals: string\n    -- schema metadata --\n    n_legs: \'Number of legs per animal\'\n    pandas: \'{"index_columns": [], "column_indexes": [{"name": null, ...\n\n    Construct a Table from chunked arrays:\n\n    >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])\n    >>> animals = pa.chunked_array([["Flamingo", "Parrot", "Dog"], ["Horse", "Brittle stars", "Centipede"]])\n    >>> table = pa.table([n_legs, animals], names=names)\n    >>> table\n    pyarrow.Table\n    n_legs: int64\n    animals: string\n    ----\n    n_legs: [[2,2,4],[4,5,100]]\n    animals: [["Flamingo","Parrot","Dog"],["Horse","Brittle stars","Centipede"]]\n    ',
    'time32 (line 3822)': "\n    Create instance of 32-bit time (time of day) type with unit resolution.\n\n    Parameters\n    ----------\n    unit : str\n        one of 's' [second], or 'ms' [millisecond]\n\n    Returns\n    -------\n    type : pyarrow.Time32Type\n\n    Examples\n    --------\n    >>> import pyarrow as pa\n    >>> pa.time32('s')\n    Time32Type(time32[s])\n    >>> pa.time32('ms')\n    Time32Type(time32[ms])\n    ",
    'time64 (line 3865)': "\n    Create instance of 64-bit time (time of day) type with unit resolution.\n\n    Parameters\n    ----------\n    unit : str\n        One of 'us' [microsecond], or 'ns' [nanosecond].\n\n    Returns\n    -------\n    type : pyarrow.Time64Type\n\n    Examples\n    --------\n    >>> import pyarrow as pa\n    >>> pa.time64('us')\n    Time64Type(time64[us])\n    >>> pa.time64('ns')\n    Time64Type(time64[ns])\n    ",
    'timestamp (line 3763)': "\n    Create instance of timestamp type with resolution and optional time zone.\n\n    Parameters\n    ----------\n    unit : str\n        one of 's' [second], 'ms' [millisecond], 'us' [microsecond], or 'ns'\n        [nanosecond]\n    tz : str, default None\n        Time zone name. None indicates time zone naive\n\n    Examples\n    --------\n    Create an instance of timestamp type:\n\n    >>> import pyarrow as pa\n    >>> pa.timestamp('us')\n    TimestampType(timestamp[us])\n    >>> pa.timestamp('s', tz='America/New_York')\n    TimestampType(timestamp[s, tz=America/New_York])\n    >>> pa.timestamp('s', tz='+07:30')\n    TimestampType(timestamp[s, tz=+07:30])\n\n    Use timestamp type when creating a scalar object:\n\n    >>> from datetime import datetime\n    >>> pa.scalar(datetime(2012, 1, 1), type=pa.timestamp('s', tz='UTC'))\n    <pyarrow.TimestampScalar: '2012-01-01T00:00:00+0000'>\n    >>> pa.scalar(datetime(2012, 1, 1), type=pa.timestamp('us'))\n    <pyarrow.TimestampScalar: '2012-01-01T00:00:00.000000'>\n\n    Returns\n    -------\n    timestamp_type : TimestampType\n    ",
    'uint16 (line 3528)': '\n    Create instance of unsigned uint16 type.\n\n    Examples\n    --------\n    Create an instance of unsigned int16 type:\n\n    >>> import pyarrow as pa\n    >>> pa.uint16()\n    DataType(uint16)\n    >>> print(pa.uint16())\n    uint16\n\n    Create an array with unsigned int16 type:\n\n    >>> pa.array([0, 1, 2], type=pa.uint16())\n    <pyarrow.lib.UInt16Array object at ...>\n    [\n      0,\n      1,\n      2\n    ]\n    ',
    'uint32 (line 3582)': '\n    Create instance of unsigned uint32 type.\n\n    Examples\n    --------\n    Create an instance of unsigned int32 type:\n\n    >>> import pyarrow as pa\n    >>> pa.uint32()\n    DataType(uint32)\n    >>> print(pa.uint32())\n    uint32\n\n    Create an array with unsigned int32 type:\n\n    >>> pa.array([0, 1, 2], type=pa.uint32())\n    <pyarrow.lib.UInt32Array object at ...>\n    [\n      0,\n      1,\n      2\n    ]\n    ',
    'uint64 (line 3636)': '\n    Create instance of unsigned uint64 type.\n\n    Examples\n    --------\n    Create an instance of unsigned int64 type:\n\n    >>> import pyarrow as pa\n    >>> pa.uint64()\n    DataType(uint64)\n    >>> print(pa.uint64())\n    uint64\n\n    Create an array with unsigned uint64 type:\n\n    >>> pa.array([0, 1, 2], type=pa.uint64())\n    <pyarrow.lib.UInt64Array object at ...>\n    [\n      0,\n      1,\n      2\n    ]\n    ',
    'uint8 (line 3474)': '\n    Create instance of unsigned int8 type.\n\n    Examples\n    --------\n    Create an instance of unsigned int8 type:\n\n    >>> import pyarrow as pa\n    >>> pa.uint8()\n    DataType(uint8)\n    >>> print(pa.uint8())\n    uint8\n\n    Create an array with unsigned int8 type:\n\n    >>> pa.array([0, 1, 2], type=pa.uint8())\n    <pyarrow.lib.UInt8Array object at ...>\n    [\n      0,\n      1,\n      2\n    ]\n    ',
    'unregister_extension_type (line 1849)': '\n    Unregister a Python extension type.\n\n    Parameters\n    ----------\n    type_name : str\n        The name of the ExtensionType subclass to unregister.\n\n    Examples\n    --------\n    Define a UuidType extension type subclassing ExtensionType:\n\n    >>> import pyarrow as pa\n    >>> class UuidType(pa.ExtensionType):\n    ...    def __init__(self):\n    ...       pa.ExtensionType.__init__(self, pa.binary(16), "my_package.uuid")\n    ...    def __arrow_ext_serialize__(self):\n    ...       # since we don\'t have a parameterized type, we don\'t need extra\n    ...       # metadata to be deserialized\n    ...       return b\'\'\n    ...    @classmethod\n    ...    def __arrow_ext_deserialize__(self, storage_type, serialized):\n    ...       # return an instance of this subclass given the serialized\n    ...       # metadata.\n    ...       return UuidType()\n    ...\n\n    Register the extension type:\n\n    >>> pa.register_extension_type(UuidType())\n\n    Unregister the extension type:\n\n    >>> pa.unregister_extension_type("my_package.uuid")\n    ',
    'utf8 (line 4216)': '\n    Alias for string().\n\n    Examples\n    --------\n    Create an instance of a string type:\n\n    >>> import pyarrow as pa\n    >>> pa.utf8()\n    DataType(string)\n\n    and use the string type to create an array:\n\n    >>> pa.array([\'foo\', \'bar\', \'baz\'], type=pa.utf8())\n    <pyarrow.lib.StringArray object at ...>\n    [\n      "foo",\n      "bar",\n      "baz"\n    ]\n    ',
}

