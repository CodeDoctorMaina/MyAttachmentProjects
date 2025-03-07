# encoding: utf-8
# module pyarrow._dataset_parquet
# from C:\Users\hp\PycharmProjects\Text_Summarizer\venv\lib\site-packages\pyarrow\_dataset_parquet.cp38-win_amd64.pyd
# by generator 1.147
""" Dataset support for Parquet file format. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import os as os # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\os.py
import warnings as warnings # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\warnings.py
import pyarrow as pa # C:\Users\hp\PycharmProjects\Text_Summarizer\venv\lib\site-packages\pyarrow\__init__.py
from pyarrow.lib import frombytes, tobytes

from pyarrow._dataset_parquet_encryption import (set_decryption_config, 
    set_encryption_config)

import pyarrow.lib as __pyarrow_lib
import pyarrow._dataset as __pyarrow__dataset


# Variables with simple values

parquet_encryption_enabled = True

# functions

def __pyx_unpickle_ParquetReadOptions(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_ParquetReadOptions(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

# classes

class ParquetDatasetFactory(__pyarrow__dataset.DatasetFactory):
    """
    ParquetDatasetFactory(metadata_path, FileSystem filesystem, FileFormat format, ParquetFactoryOptions options=None)
    
        Create a ParquetDatasetFactory from a Parquet `_metadata` file.
    
        Parameters
        ----------
        metadata_path : str
            Path to the `_metadata` parquet metadata-only file generated with
            `pyarrow.parquet.write_metadata`.
        filesystem : pyarrow.fs.FileSystem
            Filesystem to read the metadata_path from, and subsequent parquet
            files.
        format : ParquetFileFormat
            Parquet format options.
        options : ParquetFactoryOptions, optional
            Various flags influencing the discovery of filesystem paths.
    """
    def __init__(self, metadata_path, FileSystem_filesystem, FileFormat_format, ParquetFactoryOptions_options=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ParquetDatasetFactory.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ParquetDatasetFactory.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000026D0DE399F0>'


class ParquetFactoryOptions(__pyarrow_lib._Weakrefable):
    """
    ParquetFactoryOptions(partition_base_dir=None, partitioning=None, validate_column_chunk_paths=False)
    
        Influences the discovery of parquet dataset.
    
        Parameters
        ----------
        partition_base_dir : str, optional
            For the purposes of applying the partitioning, paths will be
            stripped of the partition_base_dir. Files not matching the
            partition_base_dir prefix will be skipped for partitioning discovery.
            The ignored files will still be part of the Dataset, but will not
            have partition information.
        partitioning : Partitioning, PartitioningFactory, optional
            The partitioning scheme applied to fragments, see ``Partitioning``.
        validate_column_chunk_paths : bool, default False
            Assert that all ColumnChunk paths are consistent. The parquet spec
            allows for ColumnChunk data to be stored in multiple files, but
            ParquetDatasetFactory supports only a single file with all ColumnChunk
            data. If this flag is set construction of a ParquetDatasetFactory will
            raise an error if ColumnChunk data is not resident in a single file.
    """
    def __init__(self, partition_base_dir=None, partitioning=None, validate_column_chunk_paths=False): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ParquetFactoryOptions.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ParquetFactoryOptions.__setstate_cython__(self, __pyx_state) """
        pass

    partitioning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Partitioning to apply to discovered files.

        NOTE: setting this property will overwrite partitioning_factory.
        """

    partitioning_factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PartitioningFactory to apply to discovered files and
        discover a Partitioning.

        NOTE: setting this property will overwrite partitioning.
        """

    partition_base_dir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Base directory to strip paths before applying the partitioning.
        """

    validate_column_chunk_paths = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Base directory to strip paths before applying the partitioning.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000026D0DE39990>'
    __slots__ = ()


class ParquetFileFormat(__pyarrow__dataset.FileFormat):
    """
    ParquetFileFormat(read_options=None, default_fragment_scan_options=None, **kwargs)
    
        FileFormat for Parquet
    
        Parameters
        ----------
        read_options : ParquetReadOptions
            Read options for the file.
        default_fragment_scan_options : ParquetFragmentScanOptions
            Scan Options for the file.
        **kwargs : dict
            Additional options for read option or scan option
    """
    def equals(self, ParquetFileFormat_other): # real signature unknown; restored from __doc__
        """
        ParquetFileFormat.equals(self, ParquetFileFormat other)
        
                Parameters
                ----------
                other : pyarrow.dataset.ParquetFileFormat
        
                Returns
                -------
                bool
        """
        pass

    def make_fragment(self, file, filesystem=None, Expression_partition_expression=None, row_groups=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        ParquetFileFormat.make_fragment(self, file, filesystem=None, Expression partition_expression=None, row_groups=None, *, file_size=None)
        
                Make a FileFragment from a given file.
        
                Parameters
                ----------
                file : file-like object, path-like or str
                    The file or file path to make a fragment from.
                filesystem : Filesystem, optional
                    If `filesystem` is given, `file` must be a string and specifies
                    the path of the file to read from the filesystem.
                partition_expression : Expression, optional
                    An expression that is guaranteed true for all rows in the fragment.  Allows
                    fragment to be potentially skipped while scanning with a filter.
                row_groups : Iterable, optional
                    The indices of the row groups to include
                file_size : int, optional
                    The size of the file in bytes. Can improve performance with high-latency filesystems
                    when file size needs to be known before reading.
        
                Returns
                -------
                fragment : Fragment
                    The file fragment
        """
        pass

    def make_write_options(self, **kwargs): # real signature unknown; restored from __doc__
        """
        ParquetFileFormat.make_write_options(self, **kwargs)
        
                Parameters
                ----------
                **kwargs : dict
        
                Returns
                -------
                pyarrow.dataset.FileWriteOptions
        """
        pass

    def __init__(self, read_options=None, default_fragment_scan_options=None, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ ParquetFileFormat.__reduce__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    default_extname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    read_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000026D0C31E2D0>'


class ParquetFileFragment(__pyarrow__dataset.FileFragment):
    """ A Fragment representing a parquet file. """
    def ensure_complete_metadata(self): # real signature unknown; restored from __doc__
        """
        ParquetFileFragment.ensure_complete_metadata(self)
        
                Ensure that all metadata (statistics, physical schema, ...) have
                been read and cached in this fragment.
        """
        pass

    def split_by_row_group(self, Expression_filter=None, Schema_schema=None): # real signature unknown; restored from __doc__
        """
        ParquetFileFragment.split_by_row_group(self, Expression filter=None, Schema schema=None)
        
                Split the fragment into multiple fragments.
        
                Yield a Fragment wrapping each row group in this ParquetFileFragment.
                Row groups will be excluded whose metadata contradicts the optional
                filter.
        
                Parameters
                ----------
                filter : Expression, default None
                    Only include the row groups which satisfy this predicate (using
                    the Parquet RowGroup statistics).
                schema : Schema, default None
                    Schema to use when filtering row groups. Defaults to the
                    Fragment's physical schema
        
                Returns
                -------
                A list of Fragments
        """
        pass

    def subset(self, Expression_filter=None, Schema_schema=None, row_group_ids=None): # real signature unknown; restored from __doc__
        """
        ParquetFileFragment.subset(self, Expression filter=None, Schema schema=None, row_group_ids=None)
        
                Create a subset of the fragment (viewing a subset of the row groups).
        
                Subset can be specified by either a filter predicate (with optional
                schema) or by a list of row group IDs. Note that when using a filter,
                the resulting fragment can be empty (viewing no row groups).
        
                Parameters
                ----------
                filter : Expression, default None
                    Only include the row groups which satisfy this predicate (using
                    the Parquet RowGroup statistics).
                schema : Schema, default None
                    Schema to use when filtering row groups. Defaults to the
                    Fragment's physical schema
                row_group_ids : list of ints
                    The row group IDs to include in the subset. Can only be specified
                    if `filter` is None.
        
                Returns
                -------
                ParquetFileFragment
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ ParquetFileFragment.__reduce__(self) """
        pass

    metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_row_groups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the number of row groups viewed by this fragment (not the
        number of row groups in the origin file).
        """

    row_groups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000026D0DE39900>'


class ParquetFileWriteOptions(__pyarrow__dataset.FileWriteOptions):
    # no doc
    def update(self, **kwargs): # real signature unknown; restored from __doc__
        """
        ParquetFileWriteOptions.update(self, **kwargs)
        
                Parameters
                ----------
                **kwargs : dict
        """
        pass

    def _set_arrow_properties(self): # real signature unknown; restored from __doc__
        """ ParquetFileWriteOptions._set_arrow_properties(self) """
        pass

    def _set_encryption_config(self): # real signature unknown; restored from __doc__
        """ ParquetFileWriteOptions._set_encryption_config(self) """
        pass

    def _set_properties(self): # real signature unknown; restored from __doc__
        """ ParquetFileWriteOptions._set_properties(self) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ParquetFileWriteOptions.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ParquetFileWriteOptions.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000026D0C31E390>'


class ParquetFragmentScanOptions(__pyarrow__dataset.FragmentScanOptions):
    """
    ParquetFragmentScanOptions(bool use_buffered_stream=False, *, buffer_size=8192, bool pre_buffer=True, cache_options=None, thrift_string_size_limit=None, thrift_container_size_limit=None, decryption_config=None, bool page_checksum_verification=False)
    
        Scan-specific options for Parquet fragments.
    
        Parameters
        ----------
        use_buffered_stream : bool, default False
            Read files through buffered input streams rather than loading entire
            row groups at once. This may be enabled to reduce memory overhead.
            Disabled by default.
        buffer_size : int, default 8192
            Size of buffered stream, if enabled. Default is 8KB.
        pre_buffer : bool, default True
            If enabled, pre-buffer the raw Parquet data instead of issuing one
            read per column chunk. This can improve performance on high-latency
            filesystems (e.g. S3, GCS) by coalescing and issuing file reads in
            parallel using a background I/O thread pool.
            Set to False if you want to prioritize minimal memory usage
            over maximum speed.
        cache_options : pyarrow.CacheOptions, default None
            Cache options used when pre_buffer is enabled. The default values should
            be good for most use cases. You may want to adjust these for example if
            you have exceptionally high latency to the file system. 
        thrift_string_size_limit : int, default None
            If not None, override the maximum total string size allocated
            when decoding Thrift structures. The default limit should be
            sufficient for most Parquet files.
        thrift_container_size_limit : int, default None
            If not None, override the maximum total size of containers allocated
            when decoding Thrift structures. The default limit should be
            sufficient for most Parquet files.
        decryption_config : pyarrow.dataset.ParquetDecryptionConfig, default None
            If not None, use the provided ParquetDecryptionConfig to decrypt the
            Parquet file.
        page_checksum_verification : bool, default False
            If True, verify the page checksum for each page read from the file.
    """
    def equals(self, ParquetFragmentScanOptions_other): # real signature unknown; restored from __doc__
        """
        ParquetFragmentScanOptions.equals(self, ParquetFragmentScanOptions other)
        
                Parameters
                ----------
                other : pyarrow.dataset.ParquetFragmentScanOptions
        
                Returns
                -------
                bool
        """
        pass

    def _reconstruct(self, kwargs): # real signature unknown; restored from __doc__
        """ ParquetFragmentScanOptions._reconstruct(kwargs) """
        pass

    def __init__(self, bool_use_buffered_stream=False, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ ParquetFragmentScanOptions.__reduce__(self) """
        pass

    buffer_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cache_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    page_checksum_verification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parquet_decryption_config = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pre_buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thrift_container_size_limit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thrift_string_size_limit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    use_buffered_stream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000026D0C31E360>'
    __slots__ = ()


class ParquetReadOptions(__pyarrow_lib._Weakrefable):
    """
    ParquetReadOptions(dictionary_columns=None, coerce_int96_timestamp_unit=None)
    
        Parquet format specific options for reading.
    
        Parameters
        ----------
        dictionary_columns : list of string, default None
            Names of columns which should be dictionary encoded as
            they are read
        coerce_int96_timestamp_unit : str, default None
            Cast timestamps that are stored in INT96 format to a particular
            resolution (e.g. 'ms'). Setting to None is equivalent to 'ns'
            and therefore INT96 timestamps will be inferred as timestamps
            in nanoseconds
    """
    def equals(self, ParquetReadOptions_other): # real signature unknown; restored from __doc__
        """
        ParquetReadOptions.equals(self, ParquetReadOptions other)
        
                Parameters
                ----------
                other : pyarrow.dataset.ParquetReadOptions
        
                Returns
                -------
                bool
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, dictionary_columns=None, coerce_int96_timestamp_unit=None): # real signature unknown; restored from __doc__
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
        """ ParquetReadOptions.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ParquetReadOptions.__setstate_cython__(self, __pyx_state) """
        pass

    coerce_int96_timestamp_unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dictionary_columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """dictionary_columns: set"""

    _coerce_int96_timestamp_unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """_coerce_int96_timestamp_unit: 'TimeUnit'"""


    __hash__ = None


class RowGroupInfo(object):
    """
    A wrapper class for RowGroup information
    
        Parameters
        ----------
        id : integer
            The group ID.
        metadata : FileMetaData
            The rowgroup metadata.
        schema : Schema
            Schema of the rows.
    """
    def __eq__(self, other): # real signature unknown; restored from __doc__
        """ RowGroupInfo.__eq__(self, other) """
        pass

    def __init__(self, id, metadata, schema): # real signature unknown; restored from __doc__
        """ RowGroupInfo.__init__(self, id, metadata, schema) """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ RowGroupInfo.__repr__(self) """
        pass

    num_rows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """RowGroupInfo.num_rows(self)"""

    statistics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """RowGroupInfo.statistics(self)"""

    total_byte_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """RowGroupInfo.total_byte_size(self)"""

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow._dataset_parquet', '__doc__': '\\n    A wrapper class for RowGroup information\\n\\n    Parameters\\n    ----------\\n    id : integer\\n        The group ID.\\n    metadata : FileMetaData\\n        The rowgroup metadata.\\n    schema : Schema\\n        Schema of the rows.\\n    ', '__init__': <cyfunction RowGroupInfo.__init__ at 0x0000026D0DE32040>, 'num_rows': <property object at 0x0000026D0DE4B630>, 'total_byte_size': <property object at 0x0000026D0DE92220>, 'statistics': <property object at 0x0000026D0DE92270>, '__repr__': <cyfunction RowGroupInfo.__repr__ at 0x0000026D0DE32450>, '__eq__': <cyfunction RowGroupInfo.__eq__ at 0x0000026D0DE32520>, '__dict__': <attribute '__dict__' of 'RowGroupInfo' objects>, '__weakref__': <attribute '__weakref__' of 'RowGroupInfo' objects>, '__hash__': None})"
    __hash__ = None


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000026D058C9100>'

__spec__ = None # (!) real value is "ModuleSpec(name='pyarrow._dataset_parquet', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000026D058C9100>, origin='C:\\\\Users\\\\hp\\\\PycharmProjects\\\\Text_Summarizer\\\\venv\\\\lib\\\\site-packages\\\\pyarrow\\\\_dataset_parquet.cp38-win_amd64.pyd')"

__test__ = {}

