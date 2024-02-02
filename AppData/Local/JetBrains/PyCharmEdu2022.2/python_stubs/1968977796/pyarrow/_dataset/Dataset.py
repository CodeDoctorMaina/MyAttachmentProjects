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


class Dataset(__pyarrow_lib._Weakrefable):
    """
    Dataset()
    
        Collection of data fragments and potentially child datasets.
    
        Arrow Datasets allow you to query against data that has been split across
        multiple files. This sharding of data may indicate partitioning, which
        can accelerate queries that only touch some partitions (files).
    """
    def count_rows(self, Expression_filter=None, int_batch_size=None, int_batch_readahead=None, int_fragment_readahead=None, FragmentScanOptions_fragment_scan_options=None, bool_use_threads=True, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
        """
        Dataset.count_rows(self, Expression filter=None, int batch_size=_DEFAULT_BATCH_SIZE, int batch_readahead=_DEFAULT_BATCH_READAHEAD, int fragment_readahead=_DEFAULT_FRAGMENT_READAHEAD, FragmentScanOptions fragment_scan_options=None, bool use_threads=True, MemoryPool memory_pool=None)
        
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

    def filter(self, expression): # real signature unknown; restored from __doc__
        """
        Dataset.filter(self, expression)
        
                Apply a row filter to the dataset.
        
                Parameters
                ----------
                expression : Expression
                    The filter that should be applied to the dataset.
        
                Returns
                -------
                Dataset
        """
        pass

    def get_fragments(self, Expression_filter=None): # real signature unknown; restored from __doc__
        """
        Dataset.get_fragments(self, Expression filter=None)
        Returns an iterator over the fragments in this dataset.
        
                Parameters
                ----------
                filter : Expression, default None
                    Return fragments matching the optional filter, either using the
                    partition_expression or internal information like Parquet's
                    statistics.
        
                Returns
                -------
                fragments : iterator of Fragment
        """
        pass

    def head(self, int_num_rows, columns=None, Expression_filter=None, int_batch_size=None, int_batch_readahead=None, int_fragment_readahead=None, FragmentScanOptions_fragment_scan_options=None, bool_use_threads=True, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
        """
        Dataset.head(self, int num_rows, columns=None, Expression filter=None, int batch_size=_DEFAULT_BATCH_SIZE, int batch_readahead=_DEFAULT_BATCH_READAHEAD, int fragment_readahead=_DEFAULT_FRAGMENT_READAHEAD, FragmentScanOptions fragment_scan_options=None, bool use_threads=True, MemoryPool memory_pool=None)
        
                Load the first N rows of the dataset.
        
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
                table : Table
        """
        pass

    def join(self, right_dataset, keys, right_keys=None, join_type=None, left_suffix=None, right_suffix=None, coalesce_keys=True, use_threads=True): # real signature unknown; restored from __doc__
        """
        Dataset.join(self, right_dataset, keys, right_keys=None, join_type=u'left outer', left_suffix=None, right_suffix=None, coalesce_keys=True, use_threads=True)
        
                Perform a join between this dataset and another one.
        
                Result of the join will be a new dataset, where further
                operations can be applied.
        
                Parameters
                ----------
                right_dataset : dataset
                    The dataset to join to the current one, acting as the right dataset
                    in the join operation.
                keys : str or list[str]
                    The columns from current dataset that should be used as keys
                    of the join operation left side.
                right_keys : str or list[str], default None
                    The columns from the right_dataset that should be used as keys
                    on the join operation right side.
                    When ``None`` use the same key names as the left dataset.
                join_type : str, default "left outer"
                    The kind of join that should be performed, one of
                    ("left semi", "right semi", "left anti", "right anti",
                    "inner", "left outer", "right outer", "full outer")
                left_suffix : str, default None
                    Which suffix to add to right column names. This prevents confusion
                    when the columns in left and right datasets have colliding names.
                right_suffix : str, default None
                    Which suffix to add to the left column names. This prevents confusion
                    when the columns in left and right datasets have colliding names.
                coalesce_keys : bool, default True
                    If the duplicated keys should be omitted from one of the sides
                    in the join result.
                use_threads : bool, default True
                    Whenever to use multithreading or not.
        
                Returns
                -------
                InMemoryDataset
        """
        pass

    def replace_schema(self, Schema_schema): # real signature unknown; restored from __doc__
        """
        Dataset.replace_schema(self, Schema schema)
        
                Return a copy of this Dataset with a different schema.
        
                The copy will view the same Fragments. If the new schema is not
                compatible with the original dataset's schema then an error will
                be raised.
        
                Parameters
                ----------
                schema : Schema
                    The new dataset schema.
        """
        pass

    def scanner(self, columns=None, Expression_filter=None, int_batch_size=None, int_batch_readahead=None, int_fragment_readahead=None, FragmentScanOptions_fragment_scan_options=None, bool_use_threads=True, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
        """
        Dataset.scanner(self, columns=None, Expression filter=None, int batch_size=_DEFAULT_BATCH_SIZE, int batch_readahead=_DEFAULT_BATCH_READAHEAD, int fragment_readahead=_DEFAULT_FRAGMENT_READAHEAD, FragmentScanOptions fragment_scan_options=None, bool use_threads=True, MemoryPool memory_pool=None)
        
                Build a scan operation against the dataset.
        
                Data is not loaded immediately. Instead, this produces a Scanner,
                which exposes further operations (e.g. loading all data as a
                table, counting rows).
        
                See the :meth:`Scanner.from_dataset` method for further information.
        
                Parameters
                ----------
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
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> table = pa.table({'year': [2020, 2022, 2021, 2022, 2019, 2021],
                ...                   'n_legs': [2, 2, 4, 4, 5, 100],
                ...                   'animal': ["Flamingo", "Parrot", "Dog", "Horse",
                ...                              "Brittle stars", "Centipede"]})
                >>>
                >>> import pyarrow.parquet as pq
                >>> pq.write_table(table, "dataset_scanner.parquet")
        
                >>> import pyarrow.dataset as ds
                >>> dataset = ds.dataset("dataset_scanner.parquet")
        
                Selecting a subset of the columns:
        
                >>> dataset.scanner(columns=["year", "n_legs"]).to_table()
                pyarrow.Table
                year: int64
                n_legs: int64
                ----
                year: [[2020,2022,2021,2022,2019,2021]]
                n_legs: [[2,2,4,4,5,100]]
        
                Projecting selected columns using an expression:
        
                >>> dataset.scanner(columns={
                ...     "n_legs_uint": ds.field("n_legs").cast("uint8"),
                ... }).to_table()
                pyarrow.Table
                n_legs_uint: uint8
                ----
                n_legs_uint: [[2,2,4,4,5,100]]
        
                Filtering rows while scanning:
        
                >>> dataset.scanner(filter=ds.field("year") > 2020).to_table()
                pyarrow.Table
                year: int64
                n_legs: int64
                animal: string
                ----
                year: [[2022,2021,2022,2021]]
                n_legs: [[2,4,4,100]]
                animal: [["Parrot","Dog","Horse","Centipede"]]
        """
        pass

    def sort_by(self, sorting, **kwargs): # real signature unknown; restored from __doc__
        """
        Dataset.sort_by(self, sorting, **kwargs)
        
                Sort the Dataset by one or multiple columns.
        
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
                InMemoryDataset
                    A new dataset sorted according to the sort keys.
        """
        pass

    def take(self, indices, columns=None, Expression_filter=None, int_batch_size=None, int_batch_readahead=None, int_fragment_readahead=None, FragmentScanOptions_fragment_scan_options=None, bool_use_threads=True, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
        """
        Dataset.take(self, indices, columns=None, Expression filter=None, int batch_size=_DEFAULT_BATCH_SIZE, int batch_readahead=_DEFAULT_BATCH_READAHEAD, int fragment_readahead=_DEFAULT_FRAGMENT_READAHEAD, FragmentScanOptions fragment_scan_options=None, bool use_threads=True, MemoryPool memory_pool=None)
        
                Select rows of data by index.
        
                Parameters
                ----------
                indices : Array or array-like
                    indices of rows to select in the dataset.
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

    def to_batches(self, columns=None, Expression_filter=None, int_batch_size=None, int_batch_readahead=None, int_fragment_readahead=None, FragmentScanOptions_fragment_scan_options=None, bool_use_threads=True, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
        """
        Dataset.to_batches(self, columns=None, Expression filter=None, int batch_size=_DEFAULT_BATCH_SIZE, int batch_readahead=_DEFAULT_BATCH_READAHEAD, int fragment_readahead=_DEFAULT_FRAGMENT_READAHEAD, FragmentScanOptions fragment_scan_options=None, bool use_threads=True, MemoryPool memory_pool=None)
        
                Read the dataset as materialized record batches.
        
                Parameters
                ----------
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

    def to_table(self, columns=None, Expression_filter=None, int_batch_size=None, int_batch_readahead=None, int_fragment_readahead=None, FragmentScanOptions_fragment_scan_options=None, bool_use_threads=True, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
        """
        Dataset.to_table(self, columns=None, Expression filter=None, int batch_size=_DEFAULT_BATCH_SIZE, int batch_readahead=_DEFAULT_BATCH_READAHEAD, int fragment_readahead=_DEFAULT_FRAGMENT_READAHEAD, FragmentScanOptions fragment_scan_options=None, bool use_threads=True, MemoryPool memory_pool=None)
        
                Read the dataset to an Arrow table.
        
                Note that this method reads all the selected data from the dataset
                into memory.
        
                Parameters
                ----------
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

    def _get_fragments(self, Expression_filter): # real signature unknown; restored from __doc__
        """ Dataset._get_fragments(self, Expression filter) """
        pass

    def _scanner_options(self, options): # real signature unknown; restored from __doc__
        """
        Dataset._scanner_options(self, options)
        Returns the default options to create a new Scanner.
        
                This is automatically invoked by :meth:`Dataset.scanner`
                and there is no need to use it.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Dataset.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Dataset.__setstate_cython__(self, __pyx_state) """
        pass

    partition_expression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        An Expression which evaluates to true for all data viewed by this
        Dataset.
        """

    schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The common schema of the full Dataset"""

    _scan_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """_scan_options: dict"""


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001D1A898D9C0>'


