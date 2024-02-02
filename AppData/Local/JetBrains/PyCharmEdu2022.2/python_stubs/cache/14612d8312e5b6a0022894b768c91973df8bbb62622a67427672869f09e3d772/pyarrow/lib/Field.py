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

class Field(_Weakrefable):
    """
    Field()
    
        A named field, with a data type, nullability, and optional metadata.
    
        Notes
        -----
        Do not use this class's constructor directly; use pyarrow.field
    
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
    def equals(self, Field_other, bool_check_metadata=False): # real signature unknown; restored from __doc__
        """
        Field.equals(self, Field other, bool check_metadata=False)
        
                Test if this field is equal to the other
        
                Parameters
                ----------
                other : pyarrow.Field
                check_metadata : bool, default False
                    Whether Field metadata equality should be checked as well.
        
                Returns
                -------
                is_equal : bool
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> f1 = pa.field('key', pa.int32())
                >>> f2 = pa.field('key', pa.int32(), nullable=False)
                >>> f1.equals(f2)
                False
                >>> f1.equals(f1)
                True
        """
        pass

    def flatten(self): # real signature unknown; restored from __doc__
        """
        Field.flatten(self)
        
                Flatten this field.  If a struct field, individual child fields
                will be returned with their names prefixed by the parent's name.
        
                Returns
                -------
                fields : List[pyarrow.Field]
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> f1 = pa.field('bar', pa.float64(), nullable=False)
                >>> f2 = pa.field('foo', pa.int32()).with_metadata({"key": "Something important"})
                >>> ff = pa.field('ff', pa.struct([f1, f2]), nullable=False)
        
                Flatten a struct field:
        
                >>> ff
                pyarrow.Field<ff: struct<bar: double not null, foo: int32> not null>
                >>> ff.flatten()
                [pyarrow.Field<ff.bar: double not null>, pyarrow.Field<ff.foo: int32>]
        """
        pass

    def remove_metadata(self): # real signature unknown; restored from __doc__
        """
        Field.remove_metadata(self)
        
                Create new field without metadata, if any
        
                Returns
                -------
                field : pyarrow.Field
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> field = pa.field('key', pa.int32(),
                ...                  metadata={"key": "Something important"})
                >>> field.metadata
                {b'key': b'Something important'}
        
                Create new field by removing the metadata from the existing one:
        
                >>> field_new = field.remove_metadata()
                >>> field_new.metadata
        """
        pass

    def with_metadata(self, metadata): # real signature unknown; restored from __doc__
        """
        Field.with_metadata(self, metadata)
        
                Add metadata as dict of string keys and values to Field
        
                Parameters
                ----------
                metadata : dict
                    Keys and values must be string-like / coercible to bytes
        
                Returns
                -------
                field : pyarrow.Field
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> field = pa.field('key', pa.int32())
        
                Create new field by adding metadata to existing one:
        
                >>> field_new = field.with_metadata({"key": "Something important"})
                >>> field_new
                pyarrow.Field<key: int32>
                >>> field_new.metadata
                {b'key': b'Something important'}
        """
        pass

    def with_name(self, name): # real signature unknown; restored from __doc__
        """
        Field.with_name(self, name)
        
                A copy of this field with the replaced name
        
                Parameters
                ----------
                name : str
        
                Returns
                -------
                field : pyarrow.Field
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> field = pa.field('key', pa.int32())
                >>> field
                pyarrow.Field<key: int32>
        
                Create new field by replacing the name of an existing one:
        
                >>> field_new = field.with_name('lock')
                >>> field_new
                pyarrow.Field<lock: int32>
        """
        pass

    def with_nullable(self, nullable): # real signature unknown; restored from __doc__
        """
        Field.with_nullable(self, nullable)
        
                A copy of this field with the replaced nullability
        
                Parameters
                ----------
                nullable : bool
        
                Returns
                -------
                field: pyarrow.Field
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> field = pa.field('key', pa.int32())
                >>> field
                pyarrow.Field<key: int32>
                >>> field.nullable
                True
        
                Create new field by replacing the nullability of an existing one:
        
                >>> field_new = field.with_nullable(False)
                >>> field_new
                pyarrow.Field<key: int32 not null>
                >>> field_new.nullable
                False
        """
        pass

    def with_type(self, DataType_new_type): # real signature unknown; restored from __doc__
        """
        Field.with_type(self, DataType new_type)
        
                A copy of this field with the replaced type
        
                Parameters
                ----------
                new_type : pyarrow.DataType
        
                Returns
                -------
                field : pyarrow.Field
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> field = pa.field('key', pa.int32())
                >>> field
                pyarrow.Field<key: int32>
        
                Create new field by replacing type of an existing one:
        
                >>> field_new = field.with_type(pa.int64())
                >>> field_new
                pyarrow.Field<key: int64>
        """
        pass

    def _export_to_c(self, out_ptr): # real signature unknown; restored from __doc__
        """
        Field._export_to_c(self, out_ptr)
        
                Export to a C ArrowSchema struct, given its pointer.
        
                Be careful: if you don't pass the ArrowSchema struct to a consumer,
                its memory will leak.  This is a low-level function intended for
                expert users.
        """
        pass

    def _import_from_c(self, in_ptr): # real signature unknown; restored from __doc__
        """
        Field._import_from_c(in_ptr)
        
                Import Field from a C ArrowSchema struct, given its pointer.
        
                This is a low-level function intended for expert users.
        """
        pass

    def _import_from_c_capsule(self, schema): # real signature unknown; restored from __doc__
        """
        Field._import_from_c_capsule(schema)
        
                Import a Field from a ArrowSchema PyCapsule
        
                Parameters
                ----------
                schema : PyCapsule
                    A valid PyCapsule with name 'arrow_schema' containing an
                    ArrowSchema pointer.
        """
        pass

    def __arrow_c_schema__(self): # real signature unknown; restored from __doc__
        """
        Field.__arrow_c_schema__(self)
        
                Export to a ArrowSchema PyCapsule
        
                Unlike _export_to_c, this will not leak memory if the capsule is not used.
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

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
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

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ Field.__reduce__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The field metadata.

        Examples
        --------
        >>> import pyarrow as pa
        >>> field = pa.field('key', pa.int32(),
        ...                  metadata={"key": "Something important"})
        >>> field.metadata
        {b'key': b'Something important'}
        """

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The field name.

        Examples
        --------
        >>> import pyarrow as pa
        >>> field = pa.field('key', pa.int32())
        >>> field.name
        'key'
        """

    nullable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The field nullability.

        Examples
        --------
        >>> import pyarrow as pa
        >>> f1 = pa.field('key', pa.int32())
        >>> f2 = pa.field('key', pa.int32(), nullable=False)
        >>> f1.nullable
        True
        >>> f2.nullable
        False
        """

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000029E0467ABD0>'


