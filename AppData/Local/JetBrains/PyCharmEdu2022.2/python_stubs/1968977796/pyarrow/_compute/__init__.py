# encoding: utf-8
# module pyarrow._compute
# from C:\Users\hp\PycharmProjects\Text_Summarizer\venv\lib\site-packages\pyarrow\_compute.cp38-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import pyarrow.lib as lib # C:\Users\hp\PycharmProjects\Text_Summarizer\venv\lib\site-packages\pyarrow\lib.cp38-win_amd64.pyd
import inspect as inspect # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\inspect.py
import numpy as np # C:\Users\hp\PycharmProjects\Text_Summarizer\venv\lib\site-packages\numpy\__init__.py
import warnings as warnings # C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\warnings.py
from pyarrow.lib import ArrowInvalid, frombytes, tobytes

import pyarrow.lib as __pyarrow_lib


# Variables with simple values

_DEPR_MSG = 'pyarrow.{} is deprecated as of {}, please use pyarrow.{} instead.'

_substrait_msg = 'The pyarrow installation is not built with support for Substrait.'

__pas = None

# functions

def call_function(name, args, options=None, memory_pool=None, length=None): # real signature unknown; restored from __doc__
    """
    call_function(name, args, options=None, memory_pool=None, length=None)
    
        Call a named function.
    
        The function is looked up in the global registry
        (as returned by `function_registry()`).
    
        Parameters
        ----------
        name : str
            The name of the function to call.
        args : list
            The arguments to the function.
        options : optional
            options provided to the function.
        memory_pool : MemoryPool, optional
            memory pool to use for allocations during function execution.
        length : int, optional
            Batch size for execution, for nullary (no argument) functions. If not
            passed, inferred from data.
    """
    pass

def call_tabular_function(function_name, args=None, func_registry=None): # real signature unknown; restored from __doc__
    """
    call_tabular_function(function_name, args=None, func_registry=None)
    
        Get a record batch iterator from a tabular function.
    
        Parameters
        ----------
        function_name : str
            Name of the function.
        args : iterable
            The arguments to pass to the function.  Accepted types depend
            on the specific function.  Currently, only an empty args is supported.
        func_registry : FunctionRegistry
            Optional function registry to use instead of the default global one.
    """
    pass

def function_registry(): # real signature unknown; restored from __doc__
    """ function_registry() """
    pass

def get_function(name): # real signature unknown; restored from __doc__
    """
    get_function(name)
    
        Get a function by name.
    
        The function is looked up in the global registry
        (as returned by `function_registry()`).
    
        Parameters
        ----------
        name : str
            The name of the function to lookup
    """
    pass

def list_functions(): # real signature unknown; restored from __doc__
    """
    list_functions()
    
        Return all function names in the global registry.
    """
    pass

def namedtuple(typename, field_names, *, rename=False, defaults=None, module=None): # reliably restored by inspect
    """
    Returns a new subclass of tuple with named fields.
    
        >>> Point = namedtuple('Point', ['x', 'y'])
        >>> Point.__doc__                   # docstring for the new class
        'Point(x, y)'
        >>> p = Point(11, y=22)             # instantiate with positional args or keywords
        >>> p[0] + p[1]                     # indexable like a plain tuple
        33
        >>> x, y = p                        # unpack like a regular tuple
        >>> x, y
        (11, 22)
        >>> p.x + p.y                       # fields also accessible by name
        33
        >>> d = p._asdict()                 # convert to a dictionary
        >>> d['x']
        11
        >>> Point(**d)                      # convert from a dictionary
        Point(x=11, y=22)
        >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
        Point(x=100, y=22)
    """
    pass

def register_aggregate_function(func, function_name, function_doc, in_types, out_type, func_registry=None): # real signature unknown; restored from __doc__
    """
    register_aggregate_function(func, function_name, function_doc, in_types, out_type, func_registry=None)
    
        Register a user-defined non-decomposable aggregate function.
    
        This API is EXPERIMENTAL.
    
        A non-decomposable aggregation function is a function that executes
        aggregate operations on the whole data that it is aggregating.
        In other words, non-decomposable aggregate function cannot be
        split into consume/merge/finalize steps.
    
        This is often used with ordered or segmented aggregation where groups
        can be emit before accumulating all of the input data.
    
        Note that currently the size of any input column cannot exceed 2 GB
        for a single segment (all groups combined).
    
        Parameters
        ----------
        func : callable
            A callable implementing the user-defined function.
            The first argument is the context argument of type
            UdfContext.
            Then, it must take arguments equal to the number of
            in_types defined. It must return a Scalar matching the
            out_type.
            To define a varargs function, pass a callable that takes
            *args. The in_type needs to match in type of inputs when
            the function gets called.
        function_name : str
            Name of the function. This name must be unique, i.e.,
            there should only be one function registered with
            this name in the function registry.
        function_doc : dict
            A dictionary object with keys "summary" (str),
            and "description" (str).
        in_types : Dict[str, DataType]
            A dictionary mapping function argument names to
            their respective DataType.
            The argument names will be used to generate
            documentation for the function. The number of
            arguments specified here determines the function
            arity.
        out_type : DataType
            Output type of the function.
        func_registry : FunctionRegistry
            Optional function registry to use instead of the default global one.
    
        Examples
        --------
        >>> import numpy as np
        >>> import pyarrow as pa
        >>> import pyarrow.compute as pc
        >>>
        >>> func_doc = {}
        >>> func_doc["summary"] = "simple median udf"
        >>> func_doc["description"] = "compute median"
        >>>
        >>> def compute_median(ctx, array):
        ...     return pa.scalar(np.median(array))
        >>>
        >>> func_name = "py_compute_median"
        >>> in_types = {"array": pa.int64()}
        >>> out_type = pa.float64()
        >>> pc.register_aggregate_function(compute_median, func_name, func_doc,
        ...                   in_types, out_type)
        >>>
        >>> func = pc.get_function(func_name)
        >>> func.name
        'py_compute_median'
        >>> answer = pc.call_function(func_name, [pa.array([20, 40])])
        >>> answer
        <pyarrow.DoubleScalar: 30.0>
        >>> table = pa.table([pa.array([1, 1, 2, 2]), pa.array([10, 20, 30, 40])], names=['k', 'v'])
        >>> result = table.group_by('k').aggregate([('v', 'py_compute_median')])
        >>> result
        pyarrow.Table
        k: int64
        v_py_compute_median: double
        ----
        k: [[1,2]]
        v_py_compute_median: [[15,35]]
    """
    pass

def register_scalar_function(func, function_name, function_doc, in_types, out_type, func_registry=None): # real signature unknown; restored from __doc__
    """
    register_scalar_function(func, function_name, function_doc, in_types, out_type, func_registry=None)
    
        Register a user-defined scalar function.
    
        This API is EXPERIMENTAL.
    
        A scalar function is a function that executes elementwise
        operations on arrays or scalars, i.e. a scalar function must
        be computed row-by-row with no state where each output row
        is computed only from its corresponding input row.
        In other words, all argument arrays have the same length,
        and the output array is of the same length as the arguments.
        Scalar functions are the only functions allowed in query engine
        expressions.
    
        Parameters
        ----------
        func : callable
            A callable implementing the user-defined function.
            The first argument is the context argument of type
            UdfContext.
            Then, it must take arguments equal to the number of
            in_types defined. It must return an Array or Scalar
            matching the out_type. It must return a Scalar if
            all arguments are scalar, else it must return an Array.
    
            To define a varargs function, pass a callable that takes
            *args. The last in_type will be the type of all varargs
            arguments.
        function_name : str
            Name of the function. There should only be one function
            registered with this name in the function registry.
        function_doc : dict
            A dictionary object with keys "summary" (str),
            and "description" (str).
        in_types : Dict[str, DataType]
            A dictionary mapping function argument names to
            their respective DataType.
            The argument names will be used to generate
            documentation for the function. The number of
            arguments specified here determines the function
            arity.
        out_type : DataType
            Output type of the function.
        func_registry : FunctionRegistry
            Optional function registry to use instead of the default global one.
    
        Examples
        --------
        >>> import pyarrow as pa
        >>> import pyarrow.compute as pc
        >>>
        >>> func_doc = {}
        >>> func_doc["summary"] = "simple udf"
        >>> func_doc["description"] = "add a constant to a scalar"
        >>>
        >>> def add_constant(ctx, array):
        ...     return pc.add(array, 1, memory_pool=ctx.memory_pool)
        >>>
        >>> func_name = "py_add_func"
        >>> in_types = {"array": pa.int64()}
        >>> out_type = pa.int64()
        >>> pc.register_scalar_function(add_constant, func_name, func_doc,
        ...                   in_types, out_type)
        >>>
        >>> func = pc.get_function(func_name)
        >>> func.name
        'py_add_func'
        >>> answer = pc.call_function(func_name, [pa.array([20])])
        >>> answer
        <pyarrow.lib.Int64Array object at ...>
        [
          21
        ]
    """
    pass

def register_tabular_function(func, function_name, function_doc, in_types, out_type, func_registry=None): # real signature unknown; restored from __doc__
    """
    register_tabular_function(func, function_name, function_doc, in_types, out_type, func_registry=None)
    
        Register a user-defined tabular function.
    
        This API is EXPERIMENTAL.
    
        A tabular function is one accepting a context argument of type
        UdfContext and returning a generator of struct arrays.
        The in_types argument must be empty and the out_type argument
        specifies a schema. Each struct array must have field types
        corresponding to the schema.
    
        Parameters
        ----------
        func : callable
            A callable implementing the user-defined function.
            The only argument is the context argument of type
            UdfContext. It must return a callable that
            returns on each invocation a StructArray matching
            the out_type, where an empty array indicates end.
        function_name : str
            Name of the function. There should only be one function
            registered with this name in the function registry.
        function_doc : dict
            A dictionary object with keys "summary" (str),
            and "description" (str).
        in_types : Dict[str, DataType]
            Must be an empty dictionary (reserved for future use).
        out_type : Union[Schema, DataType]
            Schema of the function's output, or a corresponding flat struct type.
        func_registry : FunctionRegistry
            Optional function registry to use instead of the default global one.
    """
    pass

def register_vector_function(func, function_name, function_doc, in_types, out_type, func_registry=None): # real signature unknown; restored from __doc__
    """
    register_vector_function(func, function_name, function_doc, in_types, out_type, func_registry=None)
    
        Register a user-defined vector function.
    
        This API is EXPERIMENTAL.
    
        A vector function is a function that executes vector
        operations on arrays. Vector function is often used
        when compute doesn't fit other more specific types of
        functions (e.g., scalar and aggregate).
    
        Parameters
        ----------
        func : callable
            A callable implementing the user-defined function.
            The first argument is the context argument of type
            UdfContext.
            Then, it must take arguments equal to the number of
            in_types defined. It must return an Array or Scalar
            matching the out_type. It must return a Scalar if
            all arguments are scalar, else it must return an Array.
    
            To define a varargs function, pass a callable that takes
            *args. The last in_type will be the type of all varargs
            arguments.
        function_name : str
            Name of the function. There should only be one function
            registered with this name in the function registry.
        function_doc : dict
            A dictionary object with keys "summary" (str),
            and "description" (str).
        in_types : Dict[str, DataType]
            A dictionary mapping function argument names to
            their respective DataType.
            The argument names will be used to generate
            documentation for the function. The number of
            arguments specified here determines the function
            arity.
        out_type : DataType
            Output type of the function.
        func_registry : FunctionRegistry
            Optional function registry to use instead of the default global one.
    
        Examples
        --------
        >>> import pyarrow as pa
        >>> import pyarrow.compute as pc
        >>>
        >>> func_doc = {}
        >>> func_doc["summary"] = "percent rank"
        >>> func_doc["description"] = "compute percent rank"
        >>>
        >>> def list_flatten_udf(ctx, x):
        ...     return pc.list_flatten(x)
        >>>
        >>> func_name = "list_flatten_udf"
        >>> in_types = {"array": pa.list_(pa.int64())}
        >>> out_type = pa.int64()
        >>> pc.register_vector_function(list_flatten_udf, func_name, func_doc,
        ...                   in_types, out_type)
        >>>
        >>> answer = pc.call_function(func_name, [pa.array([[1, 2], [3, 4]])])
        >>> answer
        <pyarrow.lib.Int64Array object at ...>
        [
          1,
          2,
          3,
          4
        ]
    """
    pass

def _deserialize(Buffer_buffer): # real signature unknown; restored from __doc__
    """ Expression._deserialize(Buffer buffer) """
    pass

def _forbid_instantiation(klass, subclasses_instead=True): # real signature unknown; restored from __doc__
    """ _forbid_instantiation(klass, subclasses_instead=True) """
    pass

def _get_udf_context(memory_pool, batch_length): # real signature unknown; restored from __doc__
    """ _get_udf_context(memory_pool, batch_length) """
    pass

def _min_count_doc(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _min_count_doc(*, default) """
    pass

def _pas(): # real signature unknown; restored from __doc__
    """ _pas() """
    pass

def _raise_invalid_function_option(value, description, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _raise_invalid_function_option(value, description, *, exception_class=ValueError) """
    pass

def _register_user_defined_function(register_func, func, function_name, function_doc, in_types, out_type, func_registry=None): # real signature unknown; restored from __doc__
    """
    _register_user_defined_function(register_func, func, function_name, function_doc, in_types, out_type, func_registry=None)
    
        Register a user-defined function.
    
        This method itself doesn't care about the type of the UDF
        (i.e., scalar vs tabular vs aggregate)
    
        Parameters
        ----------
        register_func: object
            An object holding a CRegisterUdf in a "register_func" attribute.
        func : callable
            A callable implementing the user-defined function.
        function_name : str
            Name of the function. There should only be one function
            registered with this name in the function registry.
        function_doc : dict
            A dictionary object with keys "summary" (str),
            and "description" (str).
        in_types : Dict[str, DataType]
            A dictionary mapping function argument names to
            their respective DataType.
        out_type : DataType
            Output type of the function.
        func_registry : FunctionRegistry
            Optional function registry to use instead of the default global one.
    """
    pass

def _skip_nulls_doc(): # real signature unknown; restored from __doc__
    """ _skip_nulls_doc() """
    pass

def __pyx_unpickle_Kernel(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_Kernel(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

# classes

from .FunctionOptions import FunctionOptions
from ._ArraySortOptions import _ArraySortOptions
from .ArraySortOptions import ArraySortOptions
from ._AssumeTimezoneOptions import _AssumeTimezoneOptions
from .AssumeTimezoneOptions import AssumeTimezoneOptions
from ._CastOptions import _CastOptions
from .CastOptions import CastOptions
from ._CountOptions import _CountOptions
from .CountOptions import CountOptions
from ._CumulativeOptions import _CumulativeOptions
from .CumulativeOptions import CumulativeOptions
from .CumulativeSumOptions import CumulativeSumOptions
from ._DayOfWeekOptions import _DayOfWeekOptions
from .DayOfWeekOptions import DayOfWeekOptions
from ._DictionaryEncodeOptions import _DictionaryEncodeOptions
from .DictionaryEncodeOptions import DictionaryEncodeOptions
from ._ElementWiseAggregateOptions import _ElementWiseAggregateOptions
from .ElementWiseAggregateOptions import ElementWiseAggregateOptions
from .Expression import Expression
from ._ExtractRegexOptions import _ExtractRegexOptions
from .ExtractRegexOptions import ExtractRegexOptions
from ._FilterOptions import _FilterOptions
from .FilterOptions import FilterOptions
from .Function import Function
from .FunctionDoc import FunctionDoc
from .FunctionRegistry import FunctionRegistry
from .HashAggregateFunction import HashAggregateFunction
from .Kernel import Kernel
from .HashAggregateKernel import HashAggregateKernel
from ._IndexOptions import _IndexOptions
from .IndexOptions import IndexOptions
from ._JoinOptions import _JoinOptions
from .JoinOptions import JoinOptions
from ._ListSliceOptions import _ListSliceOptions
from .ListSliceOptions import ListSliceOptions
from ._MakeStructOptions import _MakeStructOptions
from .MakeStructOptions import MakeStructOptions
from ._MapLookupOptions import _MapLookupOptions
from .MapLookupOptions import MapLookupOptions
from ._MatchSubstringOptions import _MatchSubstringOptions
from .MatchSubstringOptions import MatchSubstringOptions
from .MetaFunction import MetaFunction
from ._ModeOptions import _ModeOptions
from .ModeOptions import ModeOptions
from ._NullOptions import _NullOptions
from .NullOptions import NullOptions
from ._PadOptions import _PadOptions
from .PadOptions import PadOptions
from ._PairwiseOptions import _PairwiseOptions
from .PairwiseOptions import PairwiseOptions
from ._PartitionNthOptions import _PartitionNthOptions
from .PartitionNthOptions import PartitionNthOptions
from ._QuantileOptions import _QuantileOptions
from .QuantileOptions import QuantileOptions
from ._RandomOptions import _RandomOptions
from .RandomOptions import RandomOptions
from ._RankOptions import _RankOptions
from .RankOptions import RankOptions
from .RegisterUdf import RegisterUdf
from ._ReplaceSliceOptions import _ReplaceSliceOptions
from .ReplaceSliceOptions import ReplaceSliceOptions
from ._ReplaceSubstringOptions import _ReplaceSubstringOptions
from .ReplaceSubstringOptions import ReplaceSubstringOptions
from ._RoundBinaryOptions import _RoundBinaryOptions
from .RoundBinaryOptions import RoundBinaryOptions
from ._RoundOptions import _RoundOptions
from .RoundOptions import RoundOptions
from ._RoundTemporalOptions import _RoundTemporalOptions
from .RoundTemporalOptions import RoundTemporalOptions
from ._RoundToMultipleOptions import _RoundToMultipleOptions
from .RoundToMultipleOptions import RoundToMultipleOptions
from ._RunEndEncodeOptions import _RunEndEncodeOptions
from .RunEndEncodeOptions import RunEndEncodeOptions
from .ScalarAggregateFunction import ScalarAggregateFunction
from .ScalarAggregateKernel import ScalarAggregateKernel
from ._ScalarAggregateOptions import _ScalarAggregateOptions
from .ScalarAggregateOptions import ScalarAggregateOptions
from .ScalarFunction import ScalarFunction
from .ScalarKernel import ScalarKernel
from ._SelectKOptions import _SelectKOptions
from .SelectKOptions import SelectKOptions
from ._SetLookupOptions import _SetLookupOptions
from .SetLookupOptions import SetLookupOptions
from ._SliceOptions import _SliceOptions
from .SliceOptions import SliceOptions
from ._SortOptions import _SortOptions
from .SortOptions import SortOptions
from ._SplitOptions import _SplitOptions
from .SplitOptions import SplitOptions
from ._SplitPatternOptions import _SplitPatternOptions
from .SplitPatternOptions import SplitPatternOptions
from ._StrftimeOptions import _StrftimeOptions
from .StrftimeOptions import StrftimeOptions
from ._StrptimeOptions import _StrptimeOptions
from .StrptimeOptions import StrptimeOptions
from ._StructFieldOptions import _StructFieldOptions
from .StructFieldOptions import StructFieldOptions
from ._TakeOptions import _TakeOptions
from .TakeOptions import TakeOptions
from ._TDigestOptions import _TDigestOptions
from .TDigestOptions import TDigestOptions
from ._TrimOptions import _TrimOptions
from .TrimOptions import TrimOptions
from .UdfContext import UdfContext
from ._Utf8NormalizeOptions import _Utf8NormalizeOptions
from .Utf8NormalizeOptions import Utf8NormalizeOptions
from ._VarianceOptions import _VarianceOptions
from .VarianceOptions import VarianceOptions
from .VectorFunction import VectorFunction
from .VectorKernel import VectorKernel
from ._WeekOptions import _WeekOptions
from .WeekOptions import WeekOptions
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001FEDD6B9100>'

__pyx_capi__ = {
    '_bind': None, # (!) real value is '<capsule object "arrow::compute::Expression (struct __pyx_obj_7pyarrow_8_compute_Expression *, struct __pyx_obj_7pyarrow_3lib_Schema *)" at 0x000001FEE411BB70>'
    '_ensure_field_ref': None, # (!) real value is '<capsule object " arrow::FieldRef (PyObject *)" at 0x000001FEE411BBA0>'
    '_true': None, # (!) real value is '<capsule object "arrow::compute::Expression" at 0x000001FEE411BB40>'
    'unwrap_null_placement': None, # (!) real value is '<capsule object " arrow::compute::NullPlacement (PyObject *)" at 0x000001FEE411BC00>'
    'unwrap_sort_order': None, # (!) real value is '<capsule object " arrow::compute::SortOrder (PyObject *)" at 0x000001FEE411BBD0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pyarrow._compute', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001FEDD6B9100>, origin='C:\\\\Users\\\\hp\\\\PycharmProjects\\\\Text_Summarizer\\\\venv\\\\lib\\\\site-packages\\\\pyarrow\\\\_compute.cp38-win_amd64.pyd')"

__test__ = {
    'register_aggregate_function (line 2979)': '\n    Register a user-defined non-decomposable aggregate function.\n\n    This API is EXPERIMENTAL.\n\n    A non-decomposable aggregation function is a function that executes\n    aggregate operations on the whole data that it is aggregating.\n    In other words, non-decomposable aggregate function cannot be\n    split into consume/merge/finalize steps.\n\n    This is often used with ordered or segmented aggregation where groups\n    can be emit before accumulating all of the input data.\n\n    Note that currently the size of any input column cannot exceed 2 GB\n    for a single segment (all groups combined).\n\n    Parameters\n    ----------\n    func : callable\n        A callable implementing the user-defined function.\n        The first argument is the context argument of type\n        UdfContext.\n        Then, it must take arguments equal to the number of\n        in_types defined. It must return a Scalar matching the\n        out_type.\n        To define a varargs function, pass a callable that takes\n        *args. The in_type needs to match in type of inputs when\n        the function gets called.\n    function_name : str\n        Name of the function. This name must be unique, i.e.,\n        there should only be one function registered with\n        this name in the function registry.\n    function_doc : dict\n        A dictionary object with keys "summary" (str),\n        and "description" (str).\n    in_types : Dict[str, DataType]\n        A dictionary mapping function argument names to\n        their respective DataType.\n        The argument names will be used to generate\n        documentation for the function. The number of\n        arguments specified here determines the function\n        arity.\n    out_type : DataType\n        Output type of the function.\n    func_registry : FunctionRegistry\n        Optional function registry to use instead of the default global one.\n\n    Examples\n    --------\n    >>> import numpy as np\n    >>> import pyarrow as pa\n    >>> import pyarrow.compute as pc\n    >>>\n    >>> func_doc = {}\n    >>> func_doc["summary"] = "simple median udf"\n    >>> func_doc["description"] = "compute median"\n    >>>\n    >>> def compute_median(ctx, array):\n    ...     return pa.scalar(np.median(array))\n    >>>\n    >>> func_name = "py_compute_median"\n    >>> in_types = {"array": pa.int64()}\n    >>> out_type = pa.float64()\n    >>> pc.register_aggregate_function(compute_median, func_name, func_doc,\n    ...                   in_types, out_type)\n    >>>\n    >>> func = pc.get_function(func_name)\n    >>> func.name\n    \'py_compute_median\'\n    >>> answer = pc.call_function(func_name, [pa.array([20, 40])])\n    >>> answer\n    <pyarrow.DoubleScalar: 30.0>\n    >>> table = pa.table([pa.array([1, 1, 2, 2]), pa.array([10, 20, 30, 40])], names=[\'k\', \'v\'])\n    >>> result = table.group_by(\'k\').aggregate([(\'v\', \'py_compute_median\')])\n    >>> result\n    pyarrow.Table\n    k: int64\n    v_py_compute_median: double\n    ----\n    k: [[1,2]]\n    v_py_compute_median: [[15,35]]\n    ',
    'register_scalar_function (line 2821)': '\n    Register a user-defined scalar function.\n\n    This API is EXPERIMENTAL.\n\n    A scalar function is a function that executes elementwise\n    operations on arrays or scalars, i.e. a scalar function must\n    be computed row-by-row with no state where each output row\n    is computed only from its corresponding input row.\n    In other words, all argument arrays have the same length,\n    and the output array is of the same length as the arguments.\n    Scalar functions are the only functions allowed in query engine\n    expressions.\n\n    Parameters\n    ----------\n    func : callable\n        A callable implementing the user-defined function.\n        The first argument is the context argument of type\n        UdfContext.\n        Then, it must take arguments equal to the number of\n        in_types defined. It must return an Array or Scalar\n        matching the out_type. It must return a Scalar if\n        all arguments are scalar, else it must return an Array.\n\n        To define a varargs function, pass a callable that takes\n        *args. The last in_type will be the type of all varargs\n        arguments.\n    function_name : str\n        Name of the function. There should only be one function\n        registered with this name in the function registry.\n    function_doc : dict\n        A dictionary object with keys "summary" (str),\n        and "description" (str).\n    in_types : Dict[str, DataType]\n        A dictionary mapping function argument names to\n        their respective DataType.\n        The argument names will be used to generate\n        documentation for the function. The number of\n        arguments specified here determines the function\n        arity.\n    out_type : DataType\n        Output type of the function.\n    func_registry : FunctionRegistry\n        Optional function registry to use instead of the default global one.\n\n    Examples\n    --------\n    >>> import pyarrow as pa\n    >>> import pyarrow.compute as pc\n    >>>\n    >>> func_doc = {}\n    >>> func_doc["summary"] = "simple udf"\n    >>> func_doc["description"] = "add a constant to a scalar"\n    >>>\n    >>> def add_constant(ctx, array):\n    ...     return pc.add(array, 1, memory_pool=ctx.memory_pool)\n    >>>\n    >>> func_name = "py_add_func"\n    >>> in_types = {"array": pa.int64()}\n    >>> out_type = pa.int64()\n    >>> pc.register_scalar_function(add_constant, func_name, func_doc,\n    ...                   in_types, out_type)\n    >>>\n    >>> func = pc.get_function(func_name)\n    >>> func.name\n    \'py_add_func\'\n    >>> answer = pc.call_function(func_name, [pa.array([20])])\n    >>> answer\n    <pyarrow.lib.Int64Array object at ...>\n    [\n      21\n    ]\n    ',
    'register_vector_function (line 2902)': '\n    Register a user-defined vector function.\n\n    This API is EXPERIMENTAL.\n\n    A vector function is a function that executes vector\n    operations on arrays. Vector function is often used\n    when compute doesn\'t fit other more specific types of\n    functions (e.g., scalar and aggregate).\n\n    Parameters\n    ----------\n    func : callable\n        A callable implementing the user-defined function.\n        The first argument is the context argument of type\n        UdfContext.\n        Then, it must take arguments equal to the number of\n        in_types defined. It must return an Array or Scalar\n        matching the out_type. It must return a Scalar if\n        all arguments are scalar, else it must return an Array.\n\n        To define a varargs function, pass a callable that takes\n        *args. The last in_type will be the type of all varargs\n        arguments.\n    function_name : str\n        Name of the function. There should only be one function\n        registered with this name in the function registry.\n    function_doc : dict\n        A dictionary object with keys "summary" (str),\n        and "description" (str).\n    in_types : Dict[str, DataType]\n        A dictionary mapping function argument names to\n        their respective DataType.\n        The argument names will be used to generate\n        documentation for the function. The number of\n        arguments specified here determines the function\n        arity.\n    out_type : DataType\n        Output type of the function.\n    func_registry : FunctionRegistry\n        Optional function registry to use instead of the default global one.\n\n    Examples\n    --------\n    >>> import pyarrow as pa\n    >>> import pyarrow.compute as pc\n    >>>\n    >>> func_doc = {}\n    >>> func_doc["summary"] = "percent rank"\n    >>> func_doc["description"] = "compute percent rank"\n    >>>\n    >>> def list_flatten_udf(ctx, x):\n    ...     return pc.list_flatten(x)\n    >>>\n    >>> func_name = "list_flatten_udf"\n    >>> in_types = {"array": pa.list_(pa.int64())}\n    >>> out_type = pa.int64()\n    >>> pc.register_vector_function(list_flatten_udf, func_name, func_doc,\n    ...                   in_types, out_type)\n    >>>\n    >>> answer = pc.call_function(func_name, [pa.array([[1, 2], [3, 4]])])\n    >>> answer\n    <pyarrow.lib.Int64Array object at ...>\n    [\n      1,\n      2,\n      3,\n      4\n    ]\n    ',
}

