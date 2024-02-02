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


from ._Weakrefable import _Weakrefable

class RecordBatchReader(_Weakrefable):
    """
    Base class for reading stream of record batches.
    
        Record batch readers function as iterators of record batches that also
        provide the schema (without the need to get any batches).
    
        Warnings
        --------
        Do not call this class's constructor directly, use one of the
        ``RecordBatchReader.from_*`` functions instead.
    
        Notes
        -----
        To import and export using the Arrow C stream interface, use the
        ``_import_from_c`` and ``_export_to_c`` methods. However, keep in mind this
        interface is intended for expert users.
    
        Examples
        --------
        >>> import pyarrow as pa
        >>> schema = pa.schema([('x', pa.int64())])
        >>> def iter_record_batches():
        ...     for i in range(2):
        ...         yield pa.RecordBatch.from_arrays([pa.array([1, 2, 3])], schema=schema)
        >>> reader = pa.RecordBatchReader.from_batches(schema, iter_record_batches())
        >>> print(reader.schema)
        x: int64
        >>> for batch in reader:
        ...     print(batch)
        pyarrow.RecordBatch
        x: int64
        ----
        x: [1,2,3]
        pyarrow.RecordBatch
        x: int64
        ----
        x: [1,2,3]
    """
    def close(self): # real signature unknown; restored from __doc__
        """
        RecordBatchReader.close(self)
        
                Release any resources associated with the reader.
        """
        pass

    def from_batches(self, Schema_schema, batches): # real signature unknown; restored from __doc__
        """
        RecordBatchReader.from_batches(Schema schema, batches)
        
                Create RecordBatchReader from an iterable of batches.
        
                Parameters
                ----------
                schema : Schema
                    The shared schema of the record batches
                batches : Iterable[RecordBatch]
                    The batches that this reader will return.
        
                Returns
                -------
                reader : RecordBatchReader
        """
        pass

    def from_stream(self, data, schema=None): # real signature unknown; restored from __doc__
        """
        RecordBatchReader.from_stream(data, schema=None)
        
                Create RecordBatchReader from a Arrow-compatible stream object.
        
                This accepts objects implementing the Arrow PyCapsule Protocol for
                streams, i.e. objects that have a ``__arrow_c_stream__`` method.
        
                Parameters
                ----------
                data : Arrow-compatible stream object
                    Any object that implements the Arrow PyCapsule Protocol for
                    streams.
                schema : Schema, default None
                    The schema to which the stream should be casted, if supported
                    by the stream object.
        
                Returns
                -------
                RecordBatchReader
        """
        pass

    def iter_batches_with_custom_metadata(self): # real signature unknown; restored from __doc__
        """
        RecordBatchReader.iter_batches_with_custom_metadata(self)
        
                Iterate over record batches from the stream along with their custom
                metadata.
        
                Yields
                ------
                RecordBatchWithMetadata
        """
        pass

    def read_all(self): # real signature unknown; restored from __doc__
        """
        RecordBatchReader.read_all(self)
        
                Read all record batches as a pyarrow.Table.
        
                Returns
                -------
                Table
        """
        pass

    def read_next_batch(self): # real signature unknown; restored from __doc__
        """
        RecordBatchReader.read_next_batch(self)
        
                Read next RecordBatch from the stream.
        
                Raises
                ------
                StopIteration:
                    At end of stream.
        
                Returns
                -------
                RecordBatch
        """
        pass

    def read_next_batch_with_custom_metadata(self): # real signature unknown; restored from __doc__
        """
        RecordBatchReader.read_next_batch_with_custom_metadata(self)
        
                Read next RecordBatch from the stream along with its custom metadata.
        
                Raises
                ------
                StopIteration:
                    At end of stream.
        
                Returns
                -------
                batch : RecordBatch
                custom_metadata : KeyValueMetadata
        """
        pass

    def read_pandas(self, **options): # real signature unknown; restored from __doc__
        """
        _ReadPandasMixin.read_pandas(self, **options)
        
                Read contents of stream to a pandas.DataFrame.
        
                Read all record batches as a pyarrow.Table then convert it to a
                pandas.DataFrame using Table.to_pandas.
        
                Parameters
                ----------
                **options
                    Arguments to forward to :meth:`Table.to_pandas`.
        
                Returns
                -------
                df : pandas.DataFrame
        """
        pass

    def _export_to_c(self, out_ptr): # real signature unknown; restored from __doc__
        """
        RecordBatchReader._export_to_c(self, out_ptr)
        
                Export to a C ArrowArrayStream struct, given its pointer.
        
                Parameters
                ----------
                out_ptr: int
                    The raw pointer to a C ArrowArrayStream struct.
        
                Be careful: if you don't pass the ArrowArrayStream struct to a
                consumer, array memory will leak.  This is a low-level function
                intended for expert users.
        """
        pass

    def _import_from_c(self, in_ptr): # real signature unknown; restored from __doc__
        """
        RecordBatchReader._import_from_c(in_ptr)
        
                Import RecordBatchReader from a C ArrowArrayStream struct,
                given its pointer.
        
                Parameters
                ----------
                in_ptr: int
                    The raw pointer to a C ArrowArrayStream struct.
        
                This is a low-level function intended for expert users.
        """
        pass

    def _import_from_c_capsule(self, stream): # real signature unknown; restored from __doc__
        """
        RecordBatchReader._import_from_c_capsule(stream)
        
                Import RecordBatchReader from a C ArrowArrayStream PyCapsule.
        
                Parameters
                ----------
                stream: PyCapsule
                    A capsule containing a C ArrowArrayStream PyCapsule.
        
                Returns
                -------
                RecordBatchReader
        """
        pass

    def __arrow_c_stream__(self, requested_schema=None): # real signature unknown; restored from __doc__
        """
        RecordBatchReader.__arrow_c_stream__(self, requested_schema=None)
        
                Export to a C ArrowArrayStream PyCapsule.
        
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
                    A capsule containing a C ArrowArrayStream struct.
        """
        pass

    def __enter__(self): # real signature unknown; restored from __doc__
        """ RecordBatchReader.__enter__(self) """
        pass

    def __exit__(self, exc_type, exc_val, exc_tb): # real signature unknown; restored from __doc__
        """ RecordBatchReader.__exit__(self, exc_type, exc_val, exc_tb) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ RecordBatchReader.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ RecordBatchReader.__setstate_cython__(self, __pyx_state) """
        pass

    schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Shared schema of the record batches in the stream.

        Returns
        -------
        Schema
        """



