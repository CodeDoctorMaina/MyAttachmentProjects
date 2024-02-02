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


class Fragment(__pyarrow_lib._Weakrefable):
    """
    Fragment()
    Fragment of data from a Dataset.
    """
    def count_rows(self, Expression_filter=None, int_batch_size=None, int_batch_readahead=None, int_fragment_readahead=None, FragmentScanOptions_fragment_scan_options=None, bool_use_threads=True, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
        """
        Fragment.count_rows(self, Expression filter=None, int batch_size=_DEFAULT_BATCH_SIZE, int batch_readahead=_DEFAULT_BATCH_READAHEAD, int fragment_readahead=_DEFAULT_FRAGMENT_READAHEAD, FragmentScanOptions fragment_scan_options=None, bool use_threads=True, MemoryPool memory_pool=None)
        
                Count rows matching the scanner filter.
        
                Parameters
                ----------
                filter : Expression, default None
                    Scan will return only the rows matching the filter.
                    If possible the predicate will be pushed down to exploit the
                    partition information or internal metadata found in the data
                    source, e.g. Parquet statistics. Otherwise filters the loaded
                    RecordBatches before yielding them.
                batch_size : int, default 131_072
                    The maximum row count for scanned record batches. If scanned
                    record batches are overflowing memory then this method can be
                    called to reduce their size.
                batch_readahead : int, default 16
                    The number of batches to read ahead in a file. This might not work
                    for all file formats. Increasing this number will increase
                    RAM usage but could also improve IO utilization.
                fragment_readahead : int, default 4
                    The number of files to read ahead. Increasing this number will increase
                    RAM usage but could also improve IO utilization.
                fragment_scan_options : FragmentScanOptions, default None
                    Options specific to a particular scan and fragment type, which
                    can change between different scans of the same dataset.
                use_threads : bool, default True
                    If enabled, then maximum parallelism will be used determined by
                    the number of available CPU cores.
                memory_pool : MemoryPool, default None
                    For memory allocations, if required. If not specified, uses the
                    default pool.
        
                Returns
                -------
                count : int
        """
        pass

    def head(self, int_num_rows, columns=None, Expression_filter=None, int_batch_size=None, int_batch_readahead=None, int_fragment_readahead=None, FragmentScanOptions_fragment_scan_options=None, bool_use_threads=True, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
        """
        Fragment.head(self, int num_rows, columns=None, Expression filter=None, int batch_size=_DEFAULT_BATCH_SIZE, int batch_readahead=_DEFAULT_BATCH_READAHEAD, int fragment_readahead=_DEFAULT_FRAGMENT_READAHEAD, FragmentScanOptions fragment_scan_options=None, bool use_threads=True, MemoryPool memory_pool=None)
        
                Load the first N rows of the fragment.
        
                Parameters
                ----------
                num_rows : int
                    The number of rows to load.
                columns : list of str, default None
                    The columns to project. This can be a list of column names to
                    include (order and duplicates will be preserved), or a dictionary
                    with {new_column_name: expression} values for more advanced
                    projections.
        
                    The list of columns or expressions may use the special fields
                    `__batch_index` (the index of the batch within the fragment),
                    `__fragment_index` (the index of the fragment within the dataset),
                    `__last_in_fragment` (whether the batch is last in fragment), and
                    `__filename` (the name of the source file or a description of the
                    source fragment).
        
                    The columns will be passed down to Datasets and corresponding data
                    fragments to avoid loading, copying, and deserializing columns
                    that will not be required further down the compute chain.
                    By default all of the available columns are projected. Raises
                    an exception if any of the referenced column names does not exist
                    in the dataset's Schema.
                filter : Expression, default None
                    Scan will return only the rows matching the filter.
                    If possible the predicate will be pushed down to exploit the
                    partition information or internal metadata found in the data
                    source, e.g. Parquet statistics. Otherwise filters the loaded
                    RecordBatches before yielding them.
                batch_size : int, default 131_072
                    The maximum row count for scanned record batches. If scanned
                    record batches are overflowing memory then this method can be
                    called to reduce their size.
                batch_readahead : int, default 16
                    The number of batches to read ahead in a file. This might not work
                    for all file formats. Increasing this number will increase
                    RAM usage but could also improve IO utilization.
                fragment_readahead : int, default 4
                    The number of files to read ahead. Increasing this number will increase
                    RAM usage but could also improve IO utilization.
                fragment_scan_options : FragmentScanOptions, default None
                    Options specific to a particular scan and fragment type, which
                    can change between different scans of the same dataset.
                use_threads : bool, default True
                    If enabled, then maximum parallelism will be used determined by
                    the number of available CPU cores.
                memory_pool : MemoryPool, default None
                    For memory allocations, if required. If not specified, uses the
                    default pool.
        
                Returns
                -------
                Table
        """
        pass

    def scanner(self, Schema_schema=None, columns=None, Expression_filter=None, int_batch_size=None, int_batch_readahead=None, int_fragment_readahead=None, FragmentScanOptions_fragment_scan_options=None, bool_use_threads=True, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
        """
        Fragment.scanner(self, Schema schema=None, columns=None, Expression filter=None, int batch_size=_DEFAULT_BATCH_SIZE, int batch_readahead=_DEFAULT_BATCH_READAHEAD, int fragment_readahead=_DEFAULT_FRAGMENT_READAHEAD, FragmentScanOptions fragment_scan_options=None, bool use_threads=True, MemoryPool memory_pool=None)
        
                Build a scan operation against the fragment.
        
                Data is not loaded immediately. Instead, this produces a Scanner,
                which exposes further operations (e.g. loading all data as a
                table, counting rows).
        
                Parameters
                ----------
                schema : Schema
                    Schema to use for scanning. This is used to unify a Fragment to
                    its Dataset's schema. If not specified this will use the
                    Fragment's physical schema which might differ for each Fragment.
                columns : list of str, default None
                    The columns to project. This can be a list of column names to
                    include (order and duplicates will be preserved), or a dictionary
                    with {new_column_name: expression} values for more advanced
                    projections.
        
                    The list of columns or expressions may use the special fields
                    `__batch_index` (the index of the batch within the fragment),
                    `__fragment_index` (the index of the fragment within the dataset),
                    `__last_in_fragment` (whether the batch is last in fragment), and
                    `__filename` (the name of the source file or a description of the
                    source fragment).
        
                    The columns will be passed down to Datasets and corresponding data
                    fragments to avoid loading, copying, and deserializing columns
                    that will not be required further down the compute chain.
                    By default all of the available columns are projected. Raises
                    an exception if any of the referenced column names does not exist
                    in the dataset's Schema.
                filter : Expression, default None
                    Scan will return only the rows matching the filter.
                    If possible the predicate will be pushed down to exploit the
                    partition information or internal metadata found in the data
                    source, e.g. Parquet statistics. Otherwise filters the loaded
                    RecordBatches before yielding them.
                batch_size : int, default 131_072
                    The maximum row count for scanned record batches. If scanned
                    record batches are overflowing memory then this method can be
                    called to reduce their size.
                batch_readahead : int, default 16
                    The number of batches to read ahead in a file. This might not work
                    for all file formats. Increasing this number will increase
                    RAM usage but could also improve IO utilization.
                fragment_readahead : int, default 4
                    The number of files to read ahead. Increasing this number will increase
                    RAM usage but could also improve IO utilization.
                fragment_scan_options : FragmentScanOptions, default None
                    Options specific to a particular scan and fragment type, which
                    can change between different scans of the same dataset.
                use_threads : bool, default True
                    If enabled, then maximum parallelism will be used determined by
                    the number of available CPU cores.
                memory_pool : MemoryPool, default None
                    For memory allocations, if required. If not specified, uses the
                    default pool.
        
                Returns
                -------
                scanner : Scanner
        """
        pass

    def take(self, indices, columns=None, Expression_filter=None, int_batch_size=None, int_batch_readahead=None, int_fragment_readahead=None, FragmentScanOptions_fragment_scan_options=None, bool_use_threads=True, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
        """
        Fragment.take(self, indices, columns=None, Expression filter=None, int batch_size=_DEFAULT_BATCH_SIZE, int batch_readahead=_DEFAULT_BATCH_READAHEAD, int fragment_readahead=_DEFAULT_FRAGMENT_READAHEAD, FragmentScanOptions fragment_scan_options=None, bool use_threads=True, MemoryPool memory_pool=None)
        
                Select rows of data by index.
        
                Parameters
                ----------
                indices : Array or array-like
                    The indices of row to select in the dataset.
                columns : list of str, default None
                    The columns to project. This can be a list of column names to
                    include (order and duplicates will be preserved), or a dictionary
                    with {new_column_name: expression} values for more advanced
                    projections.
        
                    The list of columns or expressions may use the special fields
                    `__batch_index` (the index of the batch within the fragment),
                    `__fragment_index` (the index of the fragment within the dataset),
                    `__last_in_fragment` (whether the batch is last in fragment), and
                    `__filename` (the name of the source file or a description of the
                    source fragment).
        
                    The columns will be passed down to Datasets and corresponding data
                    fragments to avoid loading, copying, and deserializing columns
                    that will not be required further down the compute chain.
                    By default all of the available columns are projected. Raises
                    an exception if any of the referenced column names does not exist
                    in the dataset's Schema.
                filter : Expression, default None
                    Scan will return only the rows matching the filter.
                    If possible the predicate will be pushed down to exploit the
                    partition information or internal metadata found in the data
                    source, e.g. Parquet statistics. Otherwise filters the loaded
                    RecordBatches before yielding them.
                batch_size : int, default 131_072
                    The maximum row count for scanned record batches. If scanned
                    record batches are overflowing memory then this method can be
                    called to reduce their size.
                batch_readahead : int, default 16
                    The number of batches to read ahead in a file. This might not work
                    for all file formats. Increasing this number will increase
                    RAM usage but could also improve IO utilization.
                fragment_readahead : int, default 4
                    The number of files to read ahead. Increasing this number will increase
                    RAM usage but could also improve IO utilization.
                fragment_scan_options : FragmentScanOptions, default None
                    Options specific to a particular scan and fragment type, which
                    can change between different scans of the same dataset.
                use_threads : bool, default True
                    If enabled, then maximum parallelism will be used determined by
                    the number of available CPU cores.
                memory_pool : MemoryPool, default None
                    For memory allocations, if required. If not specified, uses the
                    default pool.
        
                Returns
                -------
                Table
        """
        pass

    def to_batches(self, Schema_schema=None, columns=None, Expression_filter=None, int_batch_size=None, int_batch_readahead=None, int_fragment_readahead=None, FragmentScanOptions_fragment_scan_options=None, bool_use_threads=True, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
        """
        Fragment.to_batches(self, Schema schema=None, columns=None, Expression filter=None, int batch_size=_DEFAULT_BATCH_SIZE, int batch_readahead=_DEFAULT_BATCH_READAHEAD, int fragment_readahead=_DEFAULT_FRAGMENT_READAHEAD, FragmentScanOptions fragment_scan_options=None, bool use_threads=True, MemoryPool memory_pool=None)
        
                Read the fragment as materialized record batches.
        
                Parameters
                ----------
                schema : Schema, optional
                    Concrete schema to use for scanning.
                columns : list of str, default None
                    The columns to project. This can be a list of column names to
                    include (order and duplicates will be preserved), or a dictionary
                    with {new_column_name: expression} values for more advanced
                    projections.
        
                    The list of columns or expressions may use the special fields
                    `__batch_index` (the index of the batch within the fragment),
                    `__fragment_index` (the index of the fragment within the dataset),
                    `__last_in_fragment` (whether the batch is last in fragment), and
                    `__filename` (the name of the source file or a description of the
                    source fragment).
        
                    The columns will be passed down to Datasets and corresponding data
                    fragments to avoid loading, copying, and deserializing columns
                    that will not be required further down the compute chain.
                    By default all of the available columns are projected. Raises
                    an exception if any of the referenced column names does not exist
                    in the dataset's Schema.
                filter : Expression, default None
                    Scan will return only the rows matching the filter.
                    If possible the predicate will be pushed down to exploit the
                    partition information or internal metadata found in the data
                    source, e.g. Parquet statistics. Otherwise filters the loaded
                    RecordBatches before yielding them.
                batch_size : int, default 131_072
                    The maximum row count for scanned record batches. If scanned
                    record batches are overflowing memory then this method can be
                    called to reduce their size.
                batch_readahead : int, default 16
                    The number of batches to read ahead in a file. This might not work
                    for all file formats. Increasing this number will increase
                    RAM usage but could also improve IO utilization.
                fragment_readahead : int, default 4
                    The number of files to read ahead. Increasing this number will increase
                    RAM usage but could also improve IO utilization.
                fragment_scan_options : FragmentScanOptions, default None
                    Options specific to a particular scan and fragment type, which
                    can change between different scans of the same dataset.
                use_threads : bool, default True
                    If enabled, then maximum parallelism will be used determined by
                    the number of available CPU cores.
                memory_pool : MemoryPool, default None
                    For memory allocations, if required. If not specified, uses the
                    default pool.
        
                Returns
                -------
                record_batches : iterator of RecordBatch
        """
        pass

    def to_table(self, Schema_schema=None, columns=None, Expression_filter=None, int_batch_size=None, int_batch_readahead=None, int_fragment_readahead=None, FragmentScanOptions_fragment_scan_options=None, bool_use_threads=True, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
        """
        Fragment.to_table(self, Schema schema=None, columns=None, Expression filter=None, int batch_size=_DEFAULT_BATCH_SIZE, int batch_readahead=_DEFAULT_BATCH_READAHEAD, int fragment_readahead=_DEFAULT_FRAGMENT_READAHEAD, FragmentScanOptions fragment_scan_options=None, bool use_threads=True, MemoryPool memory_pool=None)
        
                Convert this Fragment into a Table.
        
                Use this convenience utility with care. This will serially materialize
                the Scan result in memory before creating the Table.
        
                Parameters
                ----------
                schema : Schema, optional
                    Concrete schema to use for scanning.
                columns : list of str, default None
                    The columns to project. This can be a list of column names to
                    include (order and duplicates will be preserved), or a dictionary
                    with {new_column_name: expression} values for more advanced
                    projections.
        
                    The list of columns or expressions may use the special fields
                    `__batch_index` (the index of the batch within the fragment),
                    `__fragment_index` (the index of the fragment within the dataset),
                    `__last_in_fragment` (whether the batch is last in fragment), and
                    `__filename` (the name of the source file or a description of the
                    source fragment).
        
                    The columns will be passed down to Datasets and corresponding data
                    fragments to avoid loading, copying, and deserializing columns
                    that will not be required further down the compute chain.
                    By default all of the available columns are projected. Raises
                    an exception if any of the referenced column names does not exist
                    in the dataset's Schema.
                filter : Expression, default None
                    Scan will return only the rows matching the filter.
                    If possible the predicate will be pushed down to exploit the
                    partition information or internal metadata found in the data
                    source, e.g. Parquet statistics. Otherwise filters the loaded
                    RecordBatches before yielding them.
                batch_size : int, default 131_072
                    The maximum row count for scanned record batches. If scanned
                    record batches are overflowing memory then this method can be
                    called to reduce their size.
                batch_readahead : int, default 16
                    The number of batches to read ahead in a file. This might not work
                    for all file formats. Increasing this number will increase
                    RAM usage but could also improve IO utilization.
                fragment_readahead : int, default 4
                    The number of files to read ahead. Increasing this number will increase
                    RAM usage but could also improve IO utilization.
                fragment_scan_options : FragmentScanOptions, default None
                    Options specific to a particular scan and fragment type, which
                    can change between different scans of the same dataset.
                use_threads : bool, default True
                    If enabled, then maximum parallelism will be used determined by
                    the number of available CPU cores.
                memory_pool : MemoryPool, default None
                    For memory allocations, if required. If not specified, uses the
                    default pool.
        
                Returns
                -------
                table : Table
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Fragment.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Fragment.__setstate_cython__(self, __pyx_state) """
        pass

    partition_expression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An Expression which evaluates to true for all data viewed by this
        Fragment.
        """

    physical_schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the physical schema of this Fragment. This schema can be
        different from the dataset read schema."""


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001D1A898DBA0>'


