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


class FileFormat(__pyarrow_lib._Weakrefable):
    """ FileFormat() """
    def inspect(self, file, filesystem=None): # real signature unknown; restored from __doc__
        """
        FileFormat.inspect(self, file, filesystem=None)
        
                Infer the schema of a file.
        
                Parameters
                ----------
                file : file-like object, path-like or str
                    The file or file path to infer a schema from.
                filesystem : Filesystem, optional
                    If `filesystem` is given, `file` must be a string and specifies
                    the path of the file to read from the filesystem.
        
                Returns
                -------
                schema : Schema
                    The schema inferred from the file
        """
        pass

    def make_fragment(self, file, filesystem=None, Expression_partition_expression=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        FileFormat.make_fragment(self, file, filesystem=None, Expression partition_expression=None, *, file_size=None)
        
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
                file_size : int, optional
                    The size of the file in bytes. Can improve performance with high-latency filesystems
                    when file size needs to be known before reading.
        
                Returns
                -------
                fragment : Fragment
                    The file fragment
        """
        pass

    def make_write_options(self): # real signature unknown; restored from __doc__
        """ FileFormat.make_write_options(self) """
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ FileFormat.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ FileFormat.__setstate_cython__(self, __pyx_state) """
        pass

    default_extname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    default_fragment_scan_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001D1A898DAE0>'


