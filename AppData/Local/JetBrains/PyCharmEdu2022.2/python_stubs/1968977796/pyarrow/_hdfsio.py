# encoding: utf-8
# module pyarrow._hdfsio
# from C:\Users\hp\PycharmProjects\Text_Summarizer\venv\lib\site-packages\pyarrow\_hdfsio.cp38-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import re as re # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\re.py
from pyarrow.lib import frombytes, tobytes

import pyarrow.lib as __pyarrow_lib


# functions

def have_libhdfs(): # real signature unknown; restored from __doc__
    """ have_libhdfs() """
    pass

def strip_hdfs_abspath(path): # real signature unknown; restored from __doc__
    """ strip_hdfs_abspath(path) """
    pass

# classes

class ArrowIOError(Exception):
    """ Base class for I/O related errors. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    characters_written = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    errno = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """POSIX exception code"""

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exception filename"""

    filename2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """second exception filename"""

    strerror = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exception strerror"""

    winerror = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Win32 exception code"""



class HadoopFileSystem(__pyarrow_lib._Weakrefable):
    # no doc
    def chmod(self, path, mode): # real signature unknown; restored from __doc__
        """
        HadoopFileSystem.chmod(self, path, mode)
        
                Change file permissions
        
                Parameters
                ----------
                path : string
                    absolute path to file or directory
                mode : int
                    POSIX-like bitmask
        """
        pass

    def chown(self, path, owner=None, group=None): # real signature unknown; restored from __doc__
        """
        HadoopFileSystem.chown(self, path, owner=None, group=None)
        
                Change file permissions
        
                Parameters
                ----------
                path : string
                    absolute path to file or directory
                owner : string, default None
                    New owner, None for no change
                group : string, default None
                    New group, None for no change
        """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """
        HadoopFileSystem.close(self)
        
                Disconnect from the HDFS cluster
        """
        pass

    @classmethod
    def connect(cls, type_cls, *args, **kwargs): # real signature unknown; restored from __doc__
        """ HadoopFileSystem.connect(type cls, *args, **kwargs) """
        pass

    def delete(self, path, bool_recursive=False): # real signature unknown; restored from __doc__
        """
        HadoopFileSystem.delete(self, path, bool recursive=False)
        
                Delete the indicated file or directory
        
                Parameters
                ----------
                path : string
                recursive : boolean, default False
                    If True, also delete child paths for directories
        """
        pass

    def df(self): # real signature unknown; restored from __doc__
        """
        HadoopFileSystem.df(self)
        
                Return free space on disk, like the UNIX df command
        
                Returns
                -------
                space : int
        """
        pass

    def download(self, path, stream, buffer_size=None): # real signature unknown; restored from __doc__
        """ HadoopFileSystem.download(self, path, stream, buffer_size=None) """
        pass

    def exists(self, path): # real signature unknown; restored from __doc__
        """
        HadoopFileSystem.exists(self, path)
        
                Returns True if the path is known to the cluster, False if it does not
                (or there is an RPC error)
        """
        pass

    def get_capacity(self): # real signature unknown; restored from __doc__
        """
        HadoopFileSystem.get_capacity(self)
        
                Get reported total capacity of file system
        
                Returns
                -------
                capacity : int
        """
        pass

    def get_space_used(self): # real signature unknown; restored from __doc__
        """
        HadoopFileSystem.get_space_used(self)
        
                Get space used on file system
        
                Returns
                -------
                space_used : int
        """
        pass

    def info(self, path): # real signature unknown; restored from __doc__
        """
        HadoopFileSystem.info(self, path)
        
                Return detailed HDFS information for path
        
                Parameters
                ----------
                path : string
                    Path to file or directory
        
                Returns
                -------
                path_info : dict
        """
        pass

    def isdir(self, path): # real signature unknown; restored from __doc__
        """ HadoopFileSystem.isdir(self, path) """
        pass

    def isfile(self, path): # real signature unknown; restored from __doc__
        """ HadoopFileSystem.isfile(self, path) """
        pass

    def ls(self, path, bool_full_info): # real signature unknown; restored from __doc__
        """ HadoopFileSystem.ls(self, path, bool full_info) """
        pass

    def mkdir(self, path): # real signature unknown; restored from __doc__
        """
        HadoopFileSystem.mkdir(self, path)
        
                Create indicated directory and any necessary parent directories
        """
        pass

    def open(self, path, mode=None, buffer_size=None, replication=None, default_block_size=None): # real signature unknown; restored from __doc__
        """
        HadoopFileSystem.open(self, path, mode=u'rb', buffer_size=None, replication=None, default_block_size=None)
        
                Open HDFS file for reading or writing
        
                Parameters
                ----------
                mode : string
                    Must be one of 'rb', 'wb', 'ab'
        
                Returns
                -------
                handle : HdfsFile
        """
        pass

    def rename(self, path, new_path): # real signature unknown; restored from __doc__
        """ HadoopFileSystem.rename(self, path, new_path) """
        pass

    def stat(self, path): # real signature unknown; restored from __doc__
        """
        HadoopFileSystem.stat(self, path)
        
                Return basic file system statistics about path
        
                Parameters
                ----------
                path : string
                    Path to file or directory
        
                Returns
                -------
                stat : dict
        """
        pass

    def upload(self, path, stream, buffer_size=None): # real signature unknown; restored from __doc__
        """
        HadoopFileSystem.upload(self, path, stream, buffer_size=None)
        
                Upload file-like object to HDFS path
        """
        pass

    def _connect(self, host, port, user, kerb_ticket, extra_conf): # real signature unknown; restored from __doc__
        """ HadoopFileSystem._connect(self, host, port, user, kerb_ticket, extra_conf) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ HadoopFileSystem.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ HadoopFileSystem.__setstate_cython__(self, __pyx_state) """
        pass

    extra_conf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    host = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_open = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    kerb_ticket = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000023372F3C210>'


class HdfsFile(__pyarrow_lib.NativeFile):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ HdfsFile.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ HdfsFile.__setstate_cython__(self, __pyx_state) """
        pass

    buffer_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000023372F3C1E0>'


class _HdfsFileNanny(__pyarrow_lib._Weakrefable):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _HdfsFileNanny.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _HdfsFileNanny.__setstate_cython__(self, __pyx_state) """
        pass


# variables with complex values

_HDFS_PATH_RE = None # (!) real value is "re.compile('hdfs://(.*):(\\\\d+)(.*)')"

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000023372F3C070>'

__spec__ = None # (!) real value is "ModuleSpec(name='pyarrow._hdfsio', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000023372F3C070>, origin='C:\\\\Users\\\\hp\\\\PycharmProjects\\\\Text_Summarizer\\\\venv\\\\lib\\\\site-packages\\\\pyarrow\\\\_hdfsio.cp38-win_amd64.pyd')"

__test__ = {}

