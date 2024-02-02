# encoding: utf-8
# module pyarrow._substrait
# from C:\Users\hp\PycharmProjects\Text_Summarizer\venv\lib\site-packages\pyarrow\_substrait.cp38-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from pyarrow.lib import Buffer, frombytes, py_buffer, tobytes

import pyarrow.lib as __pyarrow_lib


# functions

def deserialize_expressions(buf): # real signature unknown; restored from __doc__
    """
    deserialize_expressions(buf)
    
        Deserialize an ExtendedExpression Substrait message into a BoundExpressions object
    
        Parameters
        ----------
        buf : Buffer or bytes
            The message to deserialize
    
        Returns
        -------
        BoundExpressions
            The deserialized expressions, their names, and the bound schema
    """
    pass

def get_supported_functions(): # real signature unknown; restored from __doc__
    """
    get_supported_functions()
    
        Get a list of Substrait functions that the underlying
        engine currently supports.
    
        Returns
        -------
        list[str]
            A list of function ids encoded as '{uri}#{name}'
    """
    pass

def run_query(plan, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    run_query(plan, *, table_provider=None, use_threads=True)
    
        Execute a Substrait plan and read the results as a RecordBatchReader.
    
        Parameters
        ----------
        plan : Union[Buffer, bytes]
            The serialized Substrait plan to execute.
        table_provider : object (optional)
            A function to resolve any NamedTable relation to a table.
            The function will receive two arguments which will be a list
            of strings representing the table name and a pyarrow.Schema representing
            the expected schema and should return a pyarrow.Table.
        use_threads : bool, default True
            If True then multiple threads will be used to run the query.  If False then
            all CPU intensive work will be done on the calling thread.
    
        Returns
        -------
        RecordBatchReader
            A reader containing the result of the executed query
    
        Examples
        --------
        >>> import pyarrow as pa
        >>> from pyarrow.lib import tobytes
        >>> import pyarrow.substrait as substrait
        >>> test_table_1 = pa.Table.from_pydict({"x": [1, 2, 3]})
        >>> test_table_2 = pa.Table.from_pydict({"x": [4, 5, 6]})
        >>> def table_provider(names, schema):
        ...     if not names:
        ...        raise Exception("No names provided")
        ...     elif names[0] == "t1":
        ...        return test_table_1
        ...     elif names[1] == "t2":
        ...        return test_table_2
        ...     else:
        ...        raise Exception("Unrecognized table name")
        ...
        >>> substrait_query = '''
        ...         {
        ...             "relations": [
        ...             {"rel": {
        ...                 "read": {
        ...                 "base_schema": {
        ...                     "struct": {
        ...                     "types": [
        ...                                 {"i64": {}}
        ...                             ]
        ...                     },
        ...                     "names": [
        ...                             "x"
        ...                             ]
        ...                 },
        ...                 "namedTable": {
        ...                         "names": ["t1"]
        ...                 }
        ...                 }
        ...             }}
        ...             ]
        ...         }
        ... '''
        >>> buf = pa._substrait._parse_json_plan(tobytes(substrait_query))
        >>> reader = pa.substrait.run_query(buf, table_provider=table_provider)
        >>> reader.read_all()
        pyarrow.Table
        x: int64
        ----
        x: [[1,2,3]]
    """
    pass

def serialize_expressions(exprs, names, schema, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    serialize_expressions(exprs, names, schema, *, allow_arrow_extensions=False)
    
        Serialize a collection of expressions into Substrait
    
        Substrait expressions must be bound to a schema.  For example,
        the Substrait expression ``a:i32 + b:i32`` is different from the
        Substrait expression ``a:i64 + b:i64``.  Pyarrow expressions are
        typically unbound.  For example, both of the above expressions
        would be represented as ``a + b`` in pyarrow.
    
        This means a schema must be provided when serializing an expression.
        It also means that the serialization may fail if a matching function
        call cannot be found for the expression.
    
        Parameters
        ----------
        exprs : list of Expression
            The expressions to serialize
        names : list of str
            Names for the expressions
        schema : Schema
            The schema the expressions will be bound to
        allow_arrow_extensions : bool, default False
            If False then only functions that are part of the core Substrait function
            definitions will be allowed.  Set this to True to allow pyarrow-specific functions
            and user defined functions but the result may not be accepted by other
            compute libraries.
    
        Returns
        -------
        Buffer
            An ExtendedExpression message containing the serialized expressions
    """
    pass

def _parse_json_plan(plan): # real signature unknown; restored from __doc__
    """
    _parse_json_plan(plan)
    
        Parse a JSON plan into equivalent serialized Protobuf.
    
        Parameters
        ----------
        plan : bytes
            Substrait plan in JSON.
    
        Returns
        -------
        Buffer
            A buffer containing the serialized Protobuf plan.
    """
    pass

# classes

class BoundExpressions(__pyarrow_lib._Weakrefable):
    """
    BoundExpressions()
    
        A collection of named expressions and the schema they are bound to
    
        This is equivalent to the Substrait ExtendedExpression message
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ BoundExpressions.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ BoundExpressions.__setstate_cython__(self, __pyx_state) """
        pass

    expressions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        A dict from expression name to expression
        """

    schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The common schema that all expressions are bound to
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001CCF17C9030>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001CCF17C9100>'

__spec__ = None # (!) real value is "ModuleSpec(name='pyarrow._substrait', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001CCF17C9100>, origin='C:\\\\Users\\\\hp\\\\PycharmProjects\\\\Text_Summarizer\\\\venv\\\\lib\\\\site-packages\\\\pyarrow\\\\_substrait.cp38-win_amd64.pyd')"

__test__ = {
    'run_query (line 56)': '\n    Execute a Substrait plan and read the results as a RecordBatchReader.\n\n    Parameters\n    ----------\n    plan : Union[Buffer, bytes]\n        The serialized Substrait plan to execute.\n    table_provider : object (optional)\n        A function to resolve any NamedTable relation to a table.\n        The function will receive two arguments which will be a list\n        of strings representing the table name and a pyarrow.Schema representing\n        the expected schema and should return a pyarrow.Table.\n    use_threads : bool, default True\n        If True then multiple threads will be used to run the query.  If False then\n        all CPU intensive work will be done on the calling thread.\n\n    Returns\n    -------\n    RecordBatchReader\n        A reader containing the result of the executed query\n\n    Examples\n    --------\n    >>> import pyarrow as pa\n    >>> from pyarrow.lib import tobytes\n    >>> import pyarrow.substrait as substrait\n    >>> test_table_1 = pa.Table.from_pydict({"x": [1, 2, 3]})\n    >>> test_table_2 = pa.Table.from_pydict({"x": [4, 5, 6]})\n    >>> def table_provider(names, schema):\n    ...     if not names:\n    ...        raise Exception("No names provided")\n    ...     elif names[0] == "t1":\n    ...        return test_table_1\n    ...     elif names[1] == "t2":\n    ...        return test_table_2\n    ...     else:\n    ...        raise Exception("Unrecognized table name")\n    ...\n    >>> substrait_query = \'\'\'\n    ...         {\n    ...             "relations": [\n    ...             {"rel": {\n    ...                 "read": {\n    ...                 "base_schema": {\n    ...                     "struct": {\n    ...                     "types": [\n    ...                                 {"i64": {}}\n    ...                             ]\n    ...                     },\n    ...                     "names": [\n    ...                             "x"\n    ...                             ]\n    ...                 },\n    ...                 "namedTable": {\n    ...                         "names": ["t1"]\n    ...                 }\n    ...                 }\n    ...             }}\n    ...             ]\n    ...         }\n    ... \'\'\'\n    >>> buf = pa._substrait._parse_json_plan(tobytes(substrait_query))\n    >>> reader = pa.substrait.run_query(buf, table_provider=table_provider)\n    >>> reader.read_all()\n    pyarrow.Table\n    x: int64\n    ----\n    x: [[1,2,3]]\n    ',
}

