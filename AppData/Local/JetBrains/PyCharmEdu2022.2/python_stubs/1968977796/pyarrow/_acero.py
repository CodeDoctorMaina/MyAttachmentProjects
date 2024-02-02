# encoding: utf-8
# module pyarrow._acero
# from C:\Users\hp\PycharmProjects\Text_Summarizer\venv\lib\site-packages\pyarrow\_acero.cp38-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from pyarrow.lib import frombytes, tobytes

import pyarrow.lib as __pyarrow_lib


# no functions
# classes

class ExecNodeOptions(__pyarrow_lib._Weakrefable):
    """
    Base class for the node options.
    
        Use one of the subclasses to construct an options object.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ExecNodeOptions.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ExecNodeOptions.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000028BFF56E390>'
    __slots__ = ()


class _AggregateNodeOptions(ExecNodeOptions):
    # no doc
    def _set_options(self, aggregates, keys=None): # real signature unknown; restored from __doc__
        """ _AggregateNodeOptions._set_options(self, aggregates, keys=None) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _AggregateNodeOptions.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _AggregateNodeOptions.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000028BFF56E4E0>'


class AggregateNodeOptions(_AggregateNodeOptions):
    """
    Make a node which aggregates input batches, optionally grouped by keys.
    
        This is the option class for the "aggregate" node factory.
    
        Acero supports two types of aggregates: "scalar" aggregates,
        and "hash" aggregates. Scalar aggregates reduce an array or scalar
        input to a single scalar output (e.g. computing the mean of a column).
        Hash aggregates act like GROUP BY in SQL and first partition data
        based on one or more key columns, then reduce the data in each partition.
        The aggregate node supports both types of computation, and can compute
        any number of aggregations at once.
    
        Parameters
        ----------
        aggregates : list of tuples
            Aggregations which will be applied to the targeted fields.
            Specified as a list of tuples, where each tuple is one aggregation
            specification and consists of: aggregation target column(s) followed
            by function name, aggregation function options object and the
            output field name.
            The target column(s) specification can be a single field reference,
            an empty list or a list of fields unary, nullary and n-ary aggregation
            functions respectively. Each field reference can be a string
            column name or expression.
        keys : list of field references, optional
            Keys by which aggregations will be grouped. Each key can reference
            a field using a string name or expression.
    """
    def __init__(self, aggregates, keys=None): # real signature unknown; restored from __doc__
        """ AggregateNodeOptions.__init__(self, aggregates, keys=None) """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._acero\', \'__doc__\': \'\\n    Make a node which aggregates input batches, optionally grouped by keys.\\n\\n    This is the option class for the "aggregate" node factory.\\n\\n    Acero supports two types of aggregates: "scalar" aggregates,\\n    and "hash" aggregates. Scalar aggregates reduce an array or scalar\\n    input to a single scalar output (e.g. computing the mean of a column).\\n    Hash aggregates act like GROUP BY in SQL and first partition data\\n    based on one or more key columns, then reduce the data in each partition.\\n    The aggregate node supports both types of computation, and can compute\\n    any number of aggregations at once.\\n\\n    Parameters\\n    ----------\\n    aggregates : list of tuples\\n        Aggregations which will be applied to the targeted fields.\\n        Specified as a list of tuples, where each tuple is one aggregation\\n        specification and consists of: aggregation target column(s) followed\\n        by function name, aggregation function options object and the\\n        output field name.\\n        The target column(s) specification can be a single field reference,\\n        an empty list or a list of fields unary, nullary and n-ary aggregation\\n        functions respectively. Each field reference can be a string\\n        column name or expression.\\n    keys : list of field references, optional\\n        Keys by which aggregations will be grouped. Each key can reference\\n        a field using a string name or expression.\\n    \', \'__init__\': <cyfunction AggregateNodeOptions.__init__ at 0x0000028BFF5F6790>, \'__dict__\': <attribute \'__dict__\' of \'AggregateNodeOptions\' objects>})'


class Declaration(__pyarrow_lib._Weakrefable):
    """
    Declaration(factory_name, ExecNodeOptions options, inputs=None)
    
        Helper class for declaring the nodes of an ExecPlan.
    
        A Declaration represents an unconstructed ExecNode, and potentially
        more since its inputs may also be Declarations or when constructed
        with ``from_sequence``.
    
        The possible ExecNodes to use are registered with a name,
        the "factory name", and need to be specified using this name, together
        with its corresponding ExecNodeOptions subclass.
    
        Parameters
        ----------
        factory_name : str
            The ExecNode factory name, such as "table_source", "filter",
            "project" etc. See the ExecNodeOptions subclasses for the exact
            factory names to use.
        options : ExecNodeOptions
            Corresponding ExecNodeOptions subclass (matching the factory name).
        inputs : list of Declaration, optional
            Input nodes for this declaration. Optional if the node is a source
            node, or when the declaration gets combined later with
            ``from_sequence``.
    
        Returns
        -------
        Declaration
    """
    def from_sequence(self, decls): # real signature unknown; restored from __doc__
        """
        Declaration.from_sequence(decls)
        
                Convenience factory for the common case of a simple sequence of nodes.
        
                Each of the declarations will be appended to the inputs of the
                subsequent declaration, and the final modified declaration will
                be returned.
        
                Parameters
                ----------
                decls : list of Declaration
        
                Returns
                -------
                Declaration
        """
        pass

    def to_reader(self, bool_use_threads=True): # real signature unknown; restored from __doc__
        """
        Declaration.to_reader(self, bool use_threads=True)
        Run the declaration and return results as a RecordBatchReader.
        
                For details about the parameters, see `to_table`.
        
                Returns
                -------
                pyarrow.RecordBatchReader
        """
        pass

    def to_table(self, bool_use_threads=True): # real signature unknown; restored from __doc__
        """
        Declaration.to_table(self, bool use_threads=True)
        
                Run the declaration and collect the results into a table.
        
                This method will implicitly add a sink node to the declaration
                to collect results into a table. It will then create an ExecPlan
                from the declaration, start the exec plan, block until the plan
                has finished, and return the created table.
        
                Parameters
                ----------
                use_threads : bool, default True
                    If set to False, then all CPU work will be done on the calling
                    thread. I/O tasks will still happen on the I/O executor
                    and may be multi-threaded (but should not use significant CPU
                    resources).
        
                Returns
                -------
                pyarrow.Table
        """
        pass

    def __init__(self, factory_name, ExecNodeOptions_options, inputs=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Declaration.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Declaration.__setstate_cython__(self, __pyx_state) """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000028BFF56E330>'


class _FilterNodeOptions(ExecNodeOptions):
    # no doc
    def _set_options(self, Expression_filter_expression): # real signature unknown; restored from __doc__
        """ _FilterNodeOptions._set_options(self, Expression filter_expression) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _FilterNodeOptions.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _FilterNodeOptions.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000028BFF56E420>'


class FilterNodeOptions(_FilterNodeOptions):
    """
    Make a node which excludes some rows from batches passed through it.
    
        This is the option class for the "filter" node factory.
    
        The "filter" operation provides an option to define data filtering
        criteria. It selects rows where the given expression evaluates to true.
        Filters can be written using pyarrow.compute.Expression, and the
        expression must have a return type of boolean.
    
        Parameters
        ----------
        filter_expression : pyarrow.compute.Expression
    """
    def __init__(self, Expression_filter_expression): # real signature unknown; restored from __doc__
        """ FilterNodeOptions.__init__(self, Expression filter_expression) """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._acero\', \'__doc__\': \'\\n    Make a node which excludes some rows from batches passed through it.\\n\\n    This is the option class for the "filter" node factory.\\n\\n    The "filter" operation provides an option to define data filtering\\n    criteria. It selects rows where the given expression evaluates to true.\\n    Filters can be written using pyarrow.compute.Expression, and the\\n    expression must have a return type of boolean.\\n\\n    Parameters\\n    ----------\\n    filter_expression : pyarrow.compute.Expression\\n    \', \'__init__\': <cyfunction FilterNodeOptions.__init__ at 0x0000028BFF5F65F0>, \'__dict__\': <attribute \'__dict__\' of \'FilterNodeOptions\' objects>})'


class _HashJoinNodeOptions(ExecNodeOptions):
    # no doc
    def _set_options(self, join_type, left_keys, right_keys, left_output=None, right_output=None, output_suffix_for_left=None, output_suffix_for_right=None): # real signature unknown; restored from __doc__
        """ _HashJoinNodeOptions._set_options(self, join_type, left_keys, right_keys, left_output=None, right_output=None, output_suffix_for_left=u'', output_suffix_for_right=u'') """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _HashJoinNodeOptions.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _HashJoinNodeOptions.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000028BFF56E5A0>'


class HashJoinNodeOptions(_HashJoinNodeOptions):
    """
    Make a node which implements join operation using hash join strategy.
    
        This is the option class for the "hashjoin" node factory.
    
        Parameters
        ----------
        join_type : str
            Type of join. One of "left semi", "right semi", "left anti",
            "right anti", "inner", "left outer", "right outer", "full outer".
        left_keys : str, Expression or list
            Key fields from left input. Each key can be a string column name
            or a field expression, or a list of such field references.
        right_keys : str, Expression or list
            Key fields from right input. See `left_keys` for details.
        left_output : list, optional
            List of output fields passed from left input. If left and right
            output fields are not specified, all valid fields from both left and
            right input will be output. Each field can be a string column name
            or a field expression.
        right_output : list, optional
            List of output fields passed from right input. If left and right
            output fields are not specified, all valid fields from both left and
            right input will be output. Each field can be a string column name
            or a field expression.
        output_suffix_for_left : str
            Suffix added to names of output fields coming from left input
            (used to distinguish, if necessary, between fields of the same
            name in left and right input and can be left empty if there are
            no name collisions).
        output_suffix_for_right : str
            Suffix added to names of output fields coming from right input,
            see `output_suffix_for_left` for details.
    """
    def __init__(self, join_type, left_keys, right_keys, left_output=None, right_output=None, output_suffix_for_left=None, output_suffix_for_right=None): # real signature unknown; restored from __doc__
        """ HashJoinNodeOptions.__init__(self, join_type, left_keys, right_keys, left_output=None, right_output=None, output_suffix_for_left=u'', output_suffix_for_right=u'') """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._acero\', \'__doc__\': \'\\n    Make a node which implements join operation using hash join strategy.\\n\\n    This is the option class for the "hashjoin" node factory.\\n\\n    Parameters\\n    ----------\\n    join_type : str\\n        Type of join. One of "left semi", "right semi", "left anti",\\n        "right anti", "inner", "left outer", "right outer", "full outer".\\n    left_keys : str, Expression or list\\n        Key fields from left input. Each key can be a string column name\\n        or a field expression, or a list of such field references.\\n    right_keys : str, Expression or list\\n        Key fields from right input. See `left_keys` for details.\\n    left_output : list, optional\\n        List of output fields passed from left input. If left and right\\n        output fields are not specified, all valid fields from both left and\\n        right input will be output. Each field can be a string column name\\n        or a field expression.\\n    right_output : list, optional\\n        List of output fields passed from right input. If left and right\\n        output fields are not specified, all valid fields from both left and\\n        right input will be output. Each field can be a string column name\\n        or a field expression.\\n    output_suffix_for_left : str\\n        Suffix added to names of output fields coming from left input\\n        (used to distinguish, if necessary, between fields of the same\\n        name in left and right input and can be left empty if there are\\n        no name collisions).\\n    output_suffix_for_right : str\\n        Suffix added to names of output fields coming from right input,\\n        see `output_suffix_for_left` for details.\\n    \', \'__init__\': <cyfunction HashJoinNodeOptions.__init__ at 0x0000028BFF5F6930>, \'__dict__\': <attribute \'__dict__\' of \'HashJoinNodeOptions\' objects>})'


class _OrderByNodeOptions(ExecNodeOptions):
    # no doc
    def _set_options(self, sort_keys, null_placement): # real signature unknown; restored from __doc__
        """ _OrderByNodeOptions._set_options(self, sort_keys, null_placement) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _OrderByNodeOptions.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _OrderByNodeOptions.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000028BFF56E540>'


class OrderByNodeOptions(_OrderByNodeOptions):
    """
    Make a node which applies a new ordering to the data.
    
        Currently this node works by accumulating all data, sorting, and then
        emitting the new data with an updated batch index.
        Larger-than-memory sort is not currently supported.
    
        This is the option class for the "order_by" node factory.
    
        Parameters
        ----------
        sort_keys : sequence of (name, order) tuples
            Names of field/column keys to sort the input on,
            along with the order each field/column is sorted in.
            Accepted values for `order` are "ascending", "descending".
            Each field reference can be a string column name or expression.
        null_placement : str, default "at_end"
            Where nulls in input should be sorted, only applying to
            columns/fields mentioned in `sort_keys`.
            Accepted values are "at_start", "at_end".
    """
    def __init__(self, sort_keys=(), *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ OrderByNodeOptions.__init__(self, sort_keys=(), *, null_placement=u'at_end') """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._acero\', \'__doc__\': \'\\n    Make a node which applies a new ordering to the data.\\n\\n    Currently this node works by accumulating all data, sorting, and then\\n    emitting the new data with an updated batch index.\\n    Larger-than-memory sort is not currently supported.\\n\\n    This is the option class for the "order_by" node factory.\\n\\n    Parameters\\n    ----------\\n    sort_keys : sequence of (name, order) tuples\\n        Names of field/column keys to sort the input on,\\n        along with the order each field/column is sorted in.\\n        Accepted values for `order` are "ascending", "descending".\\n        Each field reference can be a string column name or expression.\\n    null_placement : str, default "at_end"\\n        Where nulls in input should be sorted, only applying to\\n        columns/fields mentioned in `sort_keys`.\\n        Accepted values are "at_start", "at_end".\\n    \', \'__init__\': <cyfunction OrderByNodeOptions.__init__ at 0x0000028BFF5F6860>, \'__dict__\': <attribute \'__dict__\' of \'OrderByNodeOptions\' objects>})'


class _ProjectNodeOptions(ExecNodeOptions):
    # no doc
    def _set_options(self, expressions, names=None): # real signature unknown; restored from __doc__
        """ _ProjectNodeOptions._set_options(self, expressions, names=None) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _ProjectNodeOptions.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _ProjectNodeOptions.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000028BFF56E480>'


class ProjectNodeOptions(_ProjectNodeOptions):
    """
    Make a node which executes expressions on input batches,
        producing batches of the same length with new columns.
    
        This is the option class for the "project" node factory.
    
        The "project" operation rearranges, deletes, transforms, and
        creates columns. Each output column is computed by evaluating
        an expression against the source record batch. These must be
        scalar expressions (expressions consisting of scalar literals,
        field references and scalar functions, i.e. elementwise functions
        that return one value for each input row independent of the value
        of all other rows).
    
        Parameters
        ----------
        expressions : list of pyarrow.compute.Expression
            List of expressions to evaluate against the source batch. This must
            be scalar expressions.
        names : list of str, optional
            List of names for each of the output columns (same length as
            `expressions`). If `names` is not provided, the string
            representations of exprs will be used.
    """
    def __init__(self, expressions, names=None): # real signature unknown; restored from __doc__
        """ ProjectNodeOptions.__init__(self, expressions, names=None) """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._acero\', \'__doc__\': \'\\n    Make a node which executes expressions on input batches,\\n    producing batches of the same length with new columns.\\n\\n    This is the option class for the "project" node factory.\\n\\n    The "project" operation rearranges, deletes, transforms, and\\n    creates columns. Each output column is computed by evaluating\\n    an expression against the source record batch. These must be\\n    scalar expressions (expressions consisting of scalar literals,\\n    field references and scalar functions, i.e. elementwise functions\\n    that return one value for each input row independent of the value\\n    of all other rows).\\n\\n    Parameters\\n    ----------\\n    expressions : list of pyarrow.compute.Expression\\n        List of expressions to evaluate against the source batch. This must\\n        be scalar expressions.\\n    names : list of str, optional\\n        List of names for each of the output columns (same length as\\n        `expressions`). If `names` is not provided, the string\\n        representations of exprs will be used.\\n    \', \'__init__\': <cyfunction ProjectNodeOptions.__init__ at 0x0000028BFF5F66C0>, \'__dict__\': <attribute \'__dict__\' of \'ProjectNodeOptions\' objects>})'


class _TableSourceNodeOptions(ExecNodeOptions):
    # no doc
    def _set_options(self, Table_table): # real signature unknown; restored from __doc__
        """ _TableSourceNodeOptions._set_options(self, Table table) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _TableSourceNodeOptions.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _TableSourceNodeOptions.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000028BFF56E3F0>'


class TableSourceNodeOptions(_TableSourceNodeOptions):
    """
    A Source node which accepts a table.
    
        This is the option class for the "table_source" node factory.
    
        Parameters
        ----------
        table : pyarrow.Table
            The table which acts as the data source.
    """
    def __init__(self, Table_table): # real signature unknown; restored from __doc__
        """ TableSourceNodeOptions.__init__(self, Table table) """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._acero\', \'__doc__\': \'\\n    A Source node which accepts a table.\\n\\n    This is the option class for the "table_source" node factory.\\n\\n    Parameters\\n    ----------\\n    table : pyarrow.Table\\n        The table which acts as the data source.\\n    \', \'__init__\': <cyfunction TableSourceNodeOptions.__init__ at 0x0000028BFF5F6520>, \'__dict__\': <attribute \'__dict__\' of \'TableSourceNodeOptions\' objects>})'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000028BFCB19100>'

__spec__ = None # (!) real value is "ModuleSpec(name='pyarrow._acero', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000028BFCB19100>, origin='C:\\\\Users\\\\hp\\\\PycharmProjects\\\\Text_Summarizer\\\\venv\\\\lib\\\\site-packages\\\\pyarrow\\\\_acero.cp38-win_amd64.pyd')"

__test__ = {}

