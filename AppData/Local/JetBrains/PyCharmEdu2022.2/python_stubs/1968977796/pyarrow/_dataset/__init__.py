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


# Variables with simple values

_dataset_pq = False

_DEFAULT_BATCH_READAHEAD = 16
_DEFAULT_BATCH_SIZE = 131072

_DEFAULT_FRAGMENT_READAHEAD = 4

_orc_fileformat = None
_orc_imported = False

# functions

def get_partition_keys(Expression_partition_expression): # real signature unknown; restored from __doc__
    """
    get_partition_keys(Expression partition_expression)
    
        Extract partition keys (equality constraints between a field and a scalar)
        from an expression as a dict mapping the field's name to its value.
    
        NB: All expressions yielded by a HivePartitioning or DirectoryPartitioning
        will be conjunctions of equality conditions and are accessible through this
        function. Other subexpressions will be ignored.
    
        Parameters
        ----------
        partition_expression : pyarrow.dataset.Expression
    
        Returns
        -------
        dict
    
        Examples
        --------
    
        For example, an expression of
        <pyarrow.dataset.Expression ((part == A:string) and (year == 2016:int32))>
        is converted to {'part': 'A', 'year': 2016}
    """
    pass

def _constructor_directory_partitioning_factory(*args): # real signature unknown; restored from __doc__
    """ _constructor_directory_partitioning_factory(*args) """
    pass

def _constructor_filename_partitioning_factory(*args): # real signature unknown; restored from __doc__
    """ _constructor_filename_partitioning_factory(*args) """
    pass

def _constructor_hive_partitioning_factory(*args): # real signature unknown; restored from __doc__
    """ _constructor_hive_partitioning_factory(*args) """
    pass

def _filesystemdataset_write(Scanner_data, base_dir, unicode_basename_template, FileSystem_filesystem, Partitioning_partitioning, FileWriteOptions_file_options, int_max_partitions, file_visitor, unicode_existing_data_behavior, int_max_open_files, int_max_rows_per_file, int_min_rows_per_group, int_max_rows_per_group, bool_create_dir): # real signature unknown; restored from __doc__
    """
    _filesystemdataset_write(Scanner data, base_dir, unicode basename_template, FileSystem filesystem, Partitioning partitioning, FileWriteOptions file_options, int max_partitions, file_visitor, unicode existing_data_behavior, int max_open_files, int max_rows_per_file, int min_rows_per_group, int max_rows_per_group, bool create_dir)
    
        CFileSystemDataset.Write wrapper
    """
    pass

def _get_orc_fileformat(): # real signature unknown; restored from __doc__
    """
    _get_orc_fileformat()
    
        Import OrcFileFormat on first usage (to avoid circular import issue
        when `pyarrow._dataset_orc` would be imported first)
    """
    pass

def _get_parquet_classes(): # real signature unknown; restored from __doc__
    """
    _get_parquet_classes()
    
        Import Parquet class files on first usage (to avoid circular import issue
        when `pyarrow._dataset_parquet` would be imported first)
    """
    pass

def _get_parquet_symbol(name): # real signature unknown; restored from __doc__
    """
    _get_parquet_symbol(name)
    
        Get a symbol from pyarrow.parquet if the latter is importable, otherwise
        return None.
    """
    pass

def _is_iterable(obj): # reliably restored by inspect
    # no doc
    pass

def _is_path_like(path): # reliably restored by inspect
    # no doc
    pass

def _stringify_path(path): # reliably restored by inspect
    """ Convert *path* to a string or unicode path if possible. """
    pass

def __pyx_unpickle_WrittenFile(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_WrittenFile(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

# classes

from .FileFormat import FileFormat
from .CsvFileFormat import CsvFileFormat
from .FileWriteOptions import FileWriteOptions
from .CsvFileWriteOptions import CsvFileWriteOptions
from .FragmentScanOptions import FragmentScanOptions
from .CsvFragmentScanOptions import CsvFragmentScanOptions
from .Dataset import Dataset
from .DatasetFactory import DatasetFactory
from .Partitioning import Partitioning
from .KeyValuePartitioning import KeyValuePartitioning
from .DirectoryPartitioning import DirectoryPartitioning
from .IpcFileFormat import IpcFileFormat
from .FeatherFileFormat import FeatherFileFormat
from .Fragment import Fragment
from .FileFragment import FileFragment
from .FilenamePartitioning import FilenamePartitioning
from .FileSystemDataset import FileSystemDataset
from .FileSystemDatasetFactory import FileSystemDatasetFactory
from .FileSystemFactoryOptions import FileSystemFactoryOptions
from .HivePartitioning import HivePartitioning
from .InMemoryDataset import InMemoryDataset
from .IpcFileWriteOptions import IpcFileWriteOptions
from .JsonFileFormat import JsonFileFormat
from .JsonFragmentScanOptions import JsonFragmentScanOptions
from .PartitioningFactory import PartitioningFactory
from .RecordBatchIterator import RecordBatchIterator
from .Scanner import Scanner
from ._ScanNodeOptions import _ScanNodeOptions
from .ScanNodeOptions import ScanNodeOptions
from .TaggedRecordBatch import TaggedRecordBatch
from .TaggedRecordBatchIterator import TaggedRecordBatchIterator
from .UnionDataset import UnionDataset
from .UnionDatasetFactory import UnionDatasetFactory
from .WrittenFile import WrittenFile
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D1A1F39100>'

__pyx_capi__ = {
    '_make_file_source': None, # (!) real value is '<capsule object "arrow::dataset::FileSource (PyObject *, struct __pyx_opt_args_7pyarrow_8_dataset__make_file_source *__pyx_optional_args)" at 0x000001D1A898D900>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pyarrow._dataset', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D1A1F39100>, origin='C:\\\\Users\\\\hp\\\\PycharmProjects\\\\Text_Summarizer\\\\venv\\\\lib\\\\site-packages\\\\pyarrow\\\\_dataset.cp38-win_amd64.pyd')"

__test__ = {
    'Dataset.scanner (line 283)': '\n        Build a scan operation against the dataset.\n\n        Data is not loaded immediately. Instead, this produces a Scanner,\n        which exposes further operations (e.g. loading all data as a\n        table, counting rows).\n\n        See the :meth:`Scanner.from_dataset` method for further information.\n\n        Parameters\n        ----------\n        columns : list of str, default None\n            The columns to project. This can be a list of column names to\n            include (order and duplicates will be preserved), or a dictionary\n            with {new_column_name: expression} values for more advanced\n            projections.\n\n            The list of columns or expressions may use the special fields\n            `__batch_index` (the index of the batch within the fragment),\n            `__fragment_index` (the index of the fragment within the dataset),\n            `__last_in_fragment` (whether the batch is last in fragment), and\n            `__filename` (the name of the source file or a description of the\n            source fragment).\n\n            The columns will be passed down to Datasets and corresponding data\n            fragments to avoid loading, copying, and deserializing columns\n            that will not be required further down the compute chain.\n            By default all of the available columns are projected. Raises\n            an exception if any of the referenced column names does not exist\n            in the dataset\'s Schema.\n        filter : Expression, default None\n            Scan will return only the rows matching the filter.\n            If possible the predicate will be pushed down to exploit the\n            partition information or internal metadata found in the data\n            source, e.g. Parquet statistics. Otherwise filters the loaded\n            RecordBatches before yielding them.\n        batch_size : int, default 131_072\n            The maximum row count for scanned record batches. If scanned\n            record batches are overflowing memory then this method can be\n            called to reduce their size.\n        batch_readahead : int, default 16\n            The number of batches to read ahead in a file. This might not work\n            for all file formats. Increasing this number will increase\n            RAM usage but could also improve IO utilization.\n        fragment_readahead : int, default 4\n            The number of files to read ahead. Increasing this number will increase\n            RAM usage but could also improve IO utilization.\n        fragment_scan_options : FragmentScanOptions, default None\n            Options specific to a particular scan and fragment type, which\n            can change between different scans of the same dataset.\n        use_threads : bool, default True\n            If enabled, then maximum parallelism will be used determined by\n            the number of available CPU cores.\n        memory_pool : MemoryPool, default None\n            For memory allocations, if required. If not specified, uses the\n            default pool.\n\n        Returns\n        -------\n        scanner : Scanner\n\n        Examples\n        --------\n        >>> import pyarrow as pa\n        >>> table = pa.table({\'year\': [2020, 2022, 2021, 2022, 2019, 2021],\n        ...                   \'n_legs\': [2, 2, 4, 4, 5, 100],\n        ...                   \'animal\': ["Flamingo", "Parrot", "Dog", "Horse",\n        ...                              "Brittle stars", "Centipede"]})\n        >>>\n        >>> import pyarrow.parquet as pq\n        >>> pq.write_table(table, "dataset_scanner.parquet")\n\n        >>> import pyarrow.dataset as ds\n        >>> dataset = ds.dataset("dataset_scanner.parquet")\n\n        Selecting a subset of the columns:\n\n        >>> dataset.scanner(columns=["year", "n_legs"]).to_table()\n        pyarrow.Table\n        year: int64\n        n_legs: int64\n        ----\n        year: [[2020,2022,2021,2022,2019,2021]]\n        n_legs: [[2,2,4,4,5,100]]\n\n        Projecting selected columns using an expression:\n\n        >>> dataset.scanner(columns={\n        ...     "n_legs_uint": ds.field("n_legs").cast("uint8"),\n        ... }).to_table()\n        pyarrow.Table\n        n_legs_uint: uint8\n        ----\n        n_legs_uint: [[2,2,4,4,5,100]]\n\n        Filtering rows while scanning:\n\n        >>> dataset.scanner(filter=ds.field("year") > 2020).to_table()\n        pyarrow.Table\n        year: int64\n        n_legs: int64\n        animal: string\n        ----\n        year: [[2022,2021,2022,2021]]\n        n_legs: [[2,4,4,100]]\n        animal: [["Parrot","Dog","Horse","Centipede"]]\n        ',
}

