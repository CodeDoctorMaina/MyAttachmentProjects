# encoding: utf-8
# module pyarrow._dataset_parquet_encryption
# from C:\Users\hp\PycharmProjects\Text_Summarizer\venv\lib\site-packages\pyarrow\_dataset_parquet_encryption.cp38-win_amd64.pyd
# by generator 1.147
""" Dataset support for Parquet encryption. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import pyarrow.lib as __pyarrow_lib


# functions

def set_decryption_config(ParquetFragmentScanOptions_opts, ParquetDecryptionConfig_config): # real signature unknown; restored from __doc__
    """ set_decryption_config(ParquetFragmentScanOptions opts, ParquetDecryptionConfig config) """
    pass

def set_encryption_config(ParquetFileWriteOptions_opts, ParquetEncryptionConfig_config): # real signature unknown; restored from __doc__
    """ set_encryption_config(ParquetFileWriteOptions opts, ParquetEncryptionConfig config) """
    pass

# classes

class ParquetDecryptionConfig(__pyarrow_lib._Weakrefable):
    """
    Core configuration class encapsulating parameters for high-level decryption
        within the Parquet framework.
    
        ParquetDecryptionConfig is designed to pass decryption-related parameters to
        the appropriate decryption components within the Parquet library. It holds references to
        objects that define the decryption strategy, Key Management Service (KMS) configuration,
        and specific decryption configurations for reading encrypted Parquet data.
    
        Parameters
        ----------
        crypto_factory : pyarrow.parquet.encryption.CryptoFactory
            Shared pointer to a `CryptoFactory` object, pivotal in creating cryptographic
            components for the decryption process.
        kms_connection_config : pyarrow.parquet.encryption.KmsConnectionConfig
            Shared pointer to a `KmsConnectionConfig` object, containing parameters necessary
            for connecting to a Key Management Service (KMS) during decryption.
        decryption_config : pyarrow.parquet.encryption.DecryptionConfiguration
            Shared pointer to a `DecryptionConfiguration` object, specifying decryption settings
            for reading encrypted Parquet data.
    
        Raises
        ------
        ValueError
            Raised if `decryption_config` is None.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ParquetDecryptionConfig.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ParquetDecryptionConfig.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000244BDC89060>'
    __slots__ = ()


class ParquetEncryptionConfig(__pyarrow_lib._Weakrefable):
    """
    Core configuration class encapsulating parameters for high-level encryption
        within the Parquet framework.
    
        The ParquetEncryptionConfig class serves as a bridge for passing encryption-related
        parameters to the appropriate components within the Parquet library. It maintains references
        to objects that define the encryption strategy, Key Management Service (KMS) configuration,
        and specific encryption configurations for Parquet data.
    
        Parameters
        ----------
        crypto_factory : pyarrow.parquet.encryption.CryptoFactory
            Shared pointer to a `CryptoFactory` object. The `CryptoFactory` is responsible for
            creating cryptographic components, such as encryptors and decryptors.
        kms_connection_config : pyarrow.parquet.encryption.KmsConnectionConfig
            Shared pointer to a `KmsConnectionConfig` object. This object holds the configuration
            parameters necessary for connecting to a Key Management Service (KMS).
        encryption_config : pyarrow.parquet.encryption.EncryptionConfiguration
            Shared pointer to an `EncryptionConfiguration` object. This object defines specific
            encryption settings for Parquet data, including the keys assigned to different columns.
    
        Raises
        ------
        ValueError
            Raised if `encryption_config` is None.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ParquetEncryptionConfig.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ParquetEncryptionConfig.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000244BDC89030>'
    __slots__ = ()


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000244BDC89100>'

__spec__ = None # (!) real value is "ModuleSpec(name='pyarrow._dataset_parquet_encryption', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000244BDC89100>, origin='C:\\\\Users\\\\hp\\\\PycharmProjects\\\\Text_Summarizer\\\\venv\\\\lib\\\\site-packages\\\\pyarrow\\\\_dataset_parquet_encryption.cp38-win_amd64.pyd')"

__test__ = {}

