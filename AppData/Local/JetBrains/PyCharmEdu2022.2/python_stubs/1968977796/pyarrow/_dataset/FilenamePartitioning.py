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


from .KeyValuePartitioning import KeyValuePartitioning

class FilenamePartitioning(KeyValuePartitioning):
    """
    FilenamePartitioning(Schema schema, dictionaries=None, segment_encoding=u'uri')
    
        A Partitioning based on a specified Schema.
    
        The FilenamePartitioning expects one segment in the file name for each
        field in the schema (all fields are required to be present) separated
        by '_'. For example given schema<year:int16, month:int8> the name
        ``"2009_11_"`` would be parsed to ("year" == 2009 and "month" == 11).
    
        Parameters
        ----------
        schema : Schema
            The schema that describes the partitions present in the file path.
        dictionaries : dict[str, Array]
            If the type of any field of `schema` is a dictionary type, the
            corresponding entry of `dictionaries` must be an array containing
            every value which may be taken by the corresponding column or an
            error will be raised in parsing.
        segment_encoding : str, default "uri"
            After splitting paths into segments, decode the segments. Valid
            values are "uri" (URI-decode segments) and "none" (leave as-is).
    
        Returns
        -------
        FilenamePartitioning
    
        Examples
        --------
        >>> from pyarrow.dataset import FilenamePartitioning
        >>> partitioning = FilenamePartitioning(
        ...     pa.schema([("year", pa.int16()), ("month", pa.int8())]))
        >>> print(partitioning.parse("2009_11_data.parquet"))
        ((year == 2009) and (month == 11))
    """
    def discover(self, field_names=None, infer_dictionary=False, schema=None, segment_encoding=None): # real signature unknown; restored from __doc__
        """
        FilenamePartitioning.discover(field_names=None, infer_dictionary=False, schema=None, segment_encoding=u'uri')
        
                Discover a FilenamePartitioning.
        
                Parameters
                ----------
                field_names : list of str
                    The names to associate with the values from the subdirectory names.
                    If schema is given, will be populated from the schema.
                infer_dictionary : bool, default False
                    When inferring a schema for partition fields, yield dictionary
                    encoded types instead of plain types. This can be more efficient
                    when materializing virtual columns, and Expressions parsed by the
                    finished Partitioning will include dictionaries of all unique
                    inspected values for each field.
                schema : Schema, default None
                    Use this schema instead of inferring a schema from partition
                    values. Partition values will be validated against this schema
                    before accumulation into the Partitioning's dictionary.
                segment_encoding : str, default "uri"
                    After splitting paths into segments, decode the segments. Valid
                    values are "uri" (URI-decode segments) and "none" (leave as-is).
        
                Returns
                -------
                PartitioningFactory
                    To be used in the FileSystemFactoryOptions.
        """
        pass

    def __init__(self, Schema_schema, dictionaries=None, segment_encoding=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001D1A899D2D0>'


