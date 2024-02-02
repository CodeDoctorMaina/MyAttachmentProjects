# encoding: utf-8
# module torch._C
# from C:\Users\hp\PycharmProjects\Text_Summarizer\venv\lib\site-packages\torch\_C.cp38-win_amd64.pyd
# by generator 1.147
""" An Enum that contains tags that can be assigned to an operator registered in C++. """

# imports
import torch._C._onnx as _onnx # <module 'torch._C._onnx'>
import torch._C._jit as _jit # <module 'torch._C._jit'>
import torch._C._jit_tree_views as _jit_tree_views # <module 'torch._C._jit_tree_views'>
import torch._C._te as _te # <module 'torch._C._te'>
import torch._C._monitor as _monitor # <module 'torch._C._monitor'>
import torch._C._dynamo as _dynamo # <module 'torch._C._dynamo'>
import torch._C._functorch as _functorch # <module 'torch._C._functorch'>
import torch._C._return_types as _return_types # <module 'torch._C._return_types'>
import torch._C._nn as _nn # <module 'torch._C._nn'>
import torch._C._fft as _fft # <module 'torch._C._fft'>
import torch._C._linalg as _linalg # <module 'torch._C._linalg'>
import torch._C._nested as _nested # <module 'torch._C._nested'>
import torch._C._sparse as _sparse # <module 'torch._C._sparse'>
import torch._C._special as _special # <module 'torch._C._special'>
import torch._C._profiler as _profiler # <module 'torch._C._profiler'>
import torch._C.cpp as cpp # <module 'torch._C.cpp'>
import torch._C._lazy as _lazy # <module 'torch._C._lazy'>
import torch._C._lazy_ts_backend as _lazy_ts_backend # <module 'torch._C._lazy_ts_backend'>
import torch._C._itt as _itt # <module 'torch._C._itt'>
import torch._C._cpu as _cpu # <module 'torch._C._cpu'>
import torch._C._verbose as _verbose # <module 'torch._C._verbose'>
import torch._C._functions as _functions # <module 'torch._C._functions'>
import torch._C._distributed_c10d as _distributed_c10d # <module 'torch._C._distributed_c10d'>
import torch._C._autograd as _autograd # <module 'torch._C._autograd'>
import pybind11_builtins as __pybind11_builtins
import torch as __torch


class ScriptFunction(__pybind11_builtins.pybind11_object):
    """
    Functionally equivalent to a :class:`ScriptModule`, but represents a single
    function and does not have any attributes or Parameters.
    """
    def get_debug_state(self): # real signature unknown; restored from __doc__
        """ get_debug_state(self: torch._C.ScriptFunction) -> torch._C.GraphExecutorState """
        pass

    def graph_for(self, *args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def save(self, filename, _extra_files, p_str=None, p_str=None_1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ save(self: torch._C.ScriptFunction, filename: str, _extra_files: Dict[str, str] = {}) -> None """
        pass

    def save_to_buffer(self, _extra_files, p_str=None, p_str=None_1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ save_to_buffer(self: torch._C.ScriptFunction, _extra_files: Dict[str, str] = {}) -> bytes """
        pass

    def _debug_flush_compilation_cache(self): # real signature unknown; restored from __doc__
        """ _debug_flush_compilation_cache(self: torch._C.ScriptFunction) -> None """
        pass

    def _set_ignore_amp(self, arg0): # real signature unknown; restored from __doc__
        """ _set_ignore_amp(self: torch._C.ScriptFunction, arg0: bool) -> None """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """ __call__(*args, **kwargs) -> object """
        return object()

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(cls): # reliably restored by inspect
        # no doc
        pass

    code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    graph = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    inlined_graph = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qualified_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'__init__': <slot wrapper '__init__' of 'torch._C.ScriptFunction' objects>, '__dict__': <attribute '__dict__' of 'torch._C.ScriptFunction' objects>, '__doc__': '\\nFunctionally equivalent to a :class:`ScriptModule`, but represents a single\\nfunction and does not have any attributes or Parameters.\\n', '__module__': 'torch.jit', '__call__': <instancemethod __call__ at 0x0000028525EA6730>, 'save': <instancemethod save at 0x0000028525EA6760>, 'save_to_buffer': <instancemethod save_to_buffer at 0x0000028525EA67C0>, 'graph': <property object at 0x0000028525EA8180>, 'inlined_graph': <property object at 0x0000028525EA8220>, 'schema': <property object at 0x0000028525EA82C0>, 'code': <property object at 0x0000028525EA8360>, 'get_debug_state': <instancemethod get_debug_state at 0x0000028525EA68E0>, '_debug_flush_compilation_cache': <instancemethod _debug_flush_compilation_cache at 0x0000028525EA6940>, 'name': <property object at 0x0000028525EA84F0>, '_set_ignore_amp': <instancemethod _set_ignore_amp at 0x0000028525EA69D0>, 'qualified_name': <property object at 0x0000028525EA85E0>, 'graph_for': <function _graph_for at 0x0000028526934F70>, '__reduce__': <function _reduce at 0x00000285269340D0>})"


