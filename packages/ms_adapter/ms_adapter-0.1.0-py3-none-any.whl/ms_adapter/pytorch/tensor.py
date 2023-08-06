#!/usr/bin/env python
# -*- coding: utf-8 -*-
import warnings
import numbers
import numpy as np
import mindspore as ms
from mindspore.common import dtype as mstype
from mindspore.common._register_for_tensor import tensor_operator_registry
import mindspore.ops as P
from mindspore.ops import constexpr
from mindspore.ops._primitive_cache import _get_cache_prim
from mindspore.ops.operations import _inner_ops as inner
from mindspore.common.initializer import _init_random_normal, _init_random_uniform, Zero
from mindspore._c_expression import Tensor as Tensor_
from ms_adapter.utils import unsupported_attr, is_under_gpu_context, get_backend, \
                             is_under_ascend_context, _infer_size, _ascend_tensor_general_cast
import ms_adapter.pytorch.common.dtype as msdapter_dtype
from ms_adapter.pytorch.common.device import Device
from ms_adapter.pytorch.storage import _TypedStorage

_dtypeDict = {
    'float16': mstype.float16,
    'float32': mstype.float32,
    'float64': mstype.float64,
    'int8': mstype.int8,
    'int16': mstype.int16,
    'int32': mstype.int32,
    'int64': mstype.int64,
    'uint8': mstype.uint8,
    'uint16': mstype.uint16,
    'uint32': mstype.uint32,
    'uint64': mstype.uint64,
    'bool': mstype.bool_,
    'complex64': mstype.complex64,
    'complex128': mstype.complex128,
    'long': mstype.int64,
    'half': mstype.float16,
    'int': mstype.int32,
    'double': mstype.float64,
    'float': mstype.float32,
    'char': mstype.int8,
    'byte': mstype.uint8,
    'short': mstype.int16
}

kMaxInt8 = 2 ** 7 - 1
kMaxInt16 = 2 ** 15 - 1
kMaxInt32 = 2 ** 31 - 1
kMaxInt64 = 2 ** 63 - 1
kMaxUint8 = 2 ** 8 - 1
kMaxUint16 = 2 ** 16 - 1
kMaxUint32 = 2 ** 32 - 1
kMaxUint64 = 2 ** 64 - 1
kMantissaFloat16 = 2 ** 11
kMantissaFloat32 = 2 ** 24
kMantissaFloat64 = 2 ** 53

_dtype2typeDict = {
    'float32': 'FloatTensor',
    'float': 'FloatTensor',
    'float64': 'DoubleTensor',
    'double': 'DoubleTensor',
    'complex64': 'ComplexFloatTensor',
    'cfloat': 'ComplexFloatTensor',
    'complex128': 'ComplexDoubleTensor',
    'cdouble': 'ComplexDoubleTensor',
    'float16': 'HalfTensor',
    'half': 'HalfTensor',
    'bfloat16': 'BFloat16Tensor',
    'uint8': 'ByteTensor',
    'int8': 'CharTensor',
    'int16': 'ShortTensor',
    'short': 'ShortTensor',
    'int32': 'IntTensor',
    'int': 'IntTensor',
    'int64': 'LongTensor',
    'long': 'LongTensor',
    'bool': 'BoolTensor'
}

_type2dtypeDict = {
    'FloatTensor': msdapter_dtype.float32,
    'DoubleTensor': msdapter_dtype.float64,
    'ComplexFloatTensor': msdapter_dtype.complex64,
    'ComplexDoubleTensor': msdapter_dtype.complex128,
    'HalfTensor': msdapter_dtype.float16,
    'BFloat16Tensor': msdapter_dtype.bfloat16,
    'ByteTensor': msdapter_dtype.uint8,
    'CharTensor' : msdapter_dtype.int8,
    'ShortTensor': msdapter_dtype.int16,
    'IntTensor': msdapter_dtype.int32,
    'LongTensor': msdapter_dtype.int64,
    'BoolTensor': msdapter_dtype.bool
}

class Tensor(ms.Tensor):

    def __init__(self, *data, dtype=None, inner=False):
        def _process_data(data):
            _shape = None
            _input_data = None
            if len(data) == 1:
                if isinstance(data[0], int):
                    _shape = data
                elif isinstance(data[0], (np.ndarray, ms.Tensor, list, Tensor_)):
                    _input_data = data[0]
                elif isinstance(data[0], tuple):
                    if len(data[0]) == 1:
                        _shape = data[0]
                    else:
                        _input_data = data[0]
                elif isinstance(data[0], _TypedStorage):
                    _input_data=data[0].data
                else:
                    raise TypeError(f"For Tensor, data must be a sequence, got {type(data[0])}")
            elif len(data) > 1:
                if not isinstance(data[0], int):
                    raise TypeError("For Tensor, elements of shape must be int.")
                _shape = data
            else:
                _input_data = ()
            return _input_data, _shape

        if dtype is not None:
            dtype = _dtypeDict[str(dtype).split('.')[-1].lower()]

        if inner is True:
            super(Tensor, self).__init__(*data, dtype=dtype)
        else:
            _input_data, _shape = _process_data(data)
            if _shape:
                if dtype is None:
                    dtype = mstype.float32
                super(Tensor, self).__init__(shape=_shape, dtype=dtype, init=Zero())
                self.init_data()
            else:
                if dtype is None:
                    if not isinstance(_input_data, (ms.Tensor, Tensor_, _TypedStorage)):
                        dtype=mstype.float32
                super(Tensor, self).__init__(input_data=_input_data, dtype=dtype)

    def __neg__(self):
        tensor_ms = cast_to_ms_tensor(self)
        out = tensor_ms.__neg__()
        return cast_to_adapter_tensor(out)

    def __invert__(self):
        tensor_ms = cast_to_ms_tensor(self)
        if tensor_ms.dtype != ms.bool_:
            out = - 1 - tensor_ms
        else:
            out = tensor_ms.__invert__()
        return cast_to_adapter_tensor(out)

    def __round__(self):
        tensor_ms = cast_to_ms_tensor(self)
        out = tensor_ms.__round__()
        return cast_to_adapter_tensor(out)

    def __pos__(self):
        tensor_ms = cast_to_ms_tensor(self)
        out = tensor_ms.__pos__()
        return cast_to_adapter_tensor(out)

    def __abs__(self):
        tensor_ms = cast_to_ms_tensor(self)
        out = tensor_ms.__abs__()
        return cast_to_adapter_tensor(out)

    def __add__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__add__(other_ms)
        return cast_to_adapter_tensor(out)

    def __and__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        input_dtype = tensor_ms.dtype
        if input_dtype == mstype.bool_:
            # avoid BitwiseAnd op has not corresponding bprop.
            tensor_ms = tensor_ms.astype(mstype.int8)
            out = tensor_ms.mul(other_ms)
            out = out.astype(mstype.bool_)
        else:
            out = tensor_ms.__and__(other_ms)
        return cast_to_adapter_tensor(out)

    def __xor__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__xor__(other_ms)
        return cast_to_adapter_tensor(out)

    def __or__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        input_dtype = tensor_ms.dtype
        if input_dtype == mstype.bool_:
            # avoid BitwiseOr op has not corresponding bprop.
            tensor_ms = tensor_ms.astype(mstype.int8)
            out = tensor_ms.add(other_ms)
            out = out.astype(mstype.bool_)
        else:
            out = tensor_ms.__or__(other_ms)
        return cast_to_adapter_tensor(out)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__sub__(other_ms)
        return cast_to_adapter_tensor(out)

    def __rsub__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__rsub__(other_ms)
        return cast_to_adapter_tensor(out)

    def __isub__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__isub__(other_ms)
        return cast_to_adapter_tensor(out)

    def __mul__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__mul__(other_ms)
        return cast_to_adapter_tensor(out)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        tensor_type = tensor_ms.dtype
        if 'Int' in str(tensor_type):
            tensor_ms = ms.ops.cast(tensor_ms, mstype.float32)
        out = tensor_ms.__truediv__(other_ms)
        return cast_to_adapter_tensor(out)

    def __rtruediv__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        tensor_type = tensor_ms.dtype
        if 'Int' in str(tensor_type):
            tensor_ms = ms.ops.cast(tensor_ms, mstype.float32)
        out = tensor_ms.__rtruediv__(other_ms)
        return cast_to_adapter_tensor(out)

    def __mod__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__mod__(other_ms)
        return cast_to_adapter_tensor(out)

    def __rmod__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__rmod__(other_ms)
        return cast_to_adapter_tensor(out)

    def __imod__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__imod__(other_ms)
        return cast_to_adapter_tensor(out)

    def __pow__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__pow__(other_ms)
        return cast_to_adapter_tensor(out)

    def __rpow__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__rpow__(other_ms)
        return cast_to_adapter_tensor(out)

    def __floordiv__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__floordiv__(other_ms)
        return cast_to_adapter_tensor(out)

    def __rfloordiv__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__rfloordiv__(other_ms)
        return cast_to_adapter_tensor(out)

    def __ifloordiv__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__ifloordiv__(other_ms)
        return cast_to_adapter_tensor(out)

    def __lt__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__lt__(other_ms)
        return cast_to_adapter_tensor(out)

    def __le__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__le__(other_ms)
        return cast_to_adapter_tensor(out)

    def __gt__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__gt__(other_ms)
        return cast_to_adapter_tensor(out)

    def __ge__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__ge__(other_ms)
        return cast_to_adapter_tensor(out)

    def __eq__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__eq__(other_ms)
        return cast_to_adapter_tensor(out)

    def __hash__(self):
        return hash(id(self))

    def __ne__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__ne__(other_ms)
        return cast_to_adapter_tensor(out)

    # __setitem__ no need to overload
    def _getitem_handler(self, index):
        tensor_ms = cast_to_ms_tensor(self)
        if isinstance(index, bool):
            if index:
                return tensor_ms.expand_dims(0)
            else:
                index = ms.Tensor(False)
                out = ms.ops.masked_select(tensor_ms, index)
                return out
        if isinstance(index, tuple) and isinstance(index[0], bool):
            if False in index:
                index = ms.Tensor(False)
                out = ms.ops.masked_select(tensor_ms, index)
                return out
            else:
                return tensor_ms.expand_dims(0)
        if isinstance(index, ms.Tensor) and index.dtype == ms.bool_:
            ms_shape_len = len(tensor_ms.shape)
            index_shape_len = len(index.shape)
            out_shape = [-1]
            while index_shape_len < ms_shape_len:
                out_shape.append(tensor_ms.shape[index_shape_len])
                index = index.expand_dims(-1)
                index_shape_len += 1
            out = ms.ops.masked_select(tensor_ms, index)
            if len(out_shape) > 1:
                out = out.reshape(out_shape)
        else:
            out = tensor_ms.__getitem__(index)
        return out

    def __getitem__(self, index):
        out = cast_to_adapter_tensor(self._getitem_handler(index))
        if out is not self:
            out.parent_tensor_ = self
            out.index_of_parent_ = index
        return out

    def __getstate__(self):
        pickled = {"input_data": self.asnumpy(), "dtype": self.dtype, "const_arg": self.const_arg}
        return pickled

    def __setstate__(self, state):
        self.__init__(state["input_data"], dtype=state["dtype"])

    def fill_adapter(self, val):
        if not isinstance(val, (int, float, bool)):
            raise TypeError("For 'Tensor.fill', the type of the argument 'value' must be int, float or bool, "
                            "but got {}.".format(type(val)))
        output = tensor_operator_registry.get("fill")(self.dtype, self.shape, val)
        return cast_to_adapter_tensor(output)

    def fill_(self, val):
        output = self.fill_adapter(val)
        return _tensor_inplace_assign(self, output, "fill_", "fill_adapter")

    def normal_adapter(self, mean=0, std=1, *, generator=None):
        if generator is not None:
            raise ValueError("`generator` can not be supportted.")
        output = ms.Tensor(_init_random_normal(mean, std, self.shape), ms.float32)
        return cast_to_adapter_tensor(output)

    def normal_(self, mean=0, std=1, *, generator=None):
        output = self.normal_adapter(mean, std, generator=generator)
        return _tensor_inplace_assign(self, output, "normal_", "normal_adapter")

    def size(self, dim=None):
        """
        tensor.size() has the same function as tensor.size() in PyTorch,
        but different from the tensor.size in MindSpore.
        """
        if dim is None:
            return self.shape
        return self.shape[dim]

    def uniform_adpater(self, from_alias=0, to=1):  #TODO: from_alias->from
        self_dtype = self.dtype
        output = ms.Tensor(_init_random_uniform(from_alias, to, self.shape), self_dtype)
        return cast_to_adapter_tensor(output)

    def uniform_(self, from_alias=0, to=1):
        output = self.uniform_adpater(from_alias, to)
        return _tensor_inplace_assign(self, output, "uniform_", "uniform_adpater")

    def random_adapter(self, from_alias=0, to=None, *, generator=None):  #TODO: from_alias->from
        unsupported_attr(generator)
        if generator:
            raise NotImplementedError("generator is not supported.")

        self_dtype = self.dtype

        if not to:
            if self_dtype == ms.float64:
                return self.uniform_adpater(from_alias, kMantissaFloat64)
            elif self_dtype == ms.float32:
                return self.uniform_adpater(from_alias, kMantissaFloat32)
            elif self_dtype == ms.float16:
                return self.uniform_adpater(from_alias, kMantissaFloat16)
            elif self_dtype == ms.uint64:
                return self.uniform_adpater(from_alias, kMaxUint64)
            elif self_dtype == ms.uint32:
                return self.uniform_adpater(from_alias, kMaxUint32)
            elif self_dtype == ms.uint16:
                return self.uniform_adpater(from_alias, kMaxUint16)
            elif self_dtype == ms.uint8:
                return self.uniform_adpater(from_alias, kMaxUint8)
            elif self_dtype == ms.int64:
                return self.uniform_adpater(from_alias, kMaxInt64)
            elif self_dtype == ms.int32:
                return self.uniform_adpater(from_alias, kMaxInt32)
            elif self_dtype == ms.int16:
                return self.uniform_adpater(from_alias, kMaxInt16)
            elif self_dtype == ms.int8:
                return self.uniform_adpater(from_alias, kMaxInt8)
        return self.uniform_adpater(from_alias, to)

    def random_(self, from_alias=0, to=None, *, generator=None):
        output = self.random_adapter(from_alias, to, generator=generator)
        return _tensor_inplace_assign(self, output, "random_", "random_adapter")

    def zero_adapter(self):
        output = tensor_operator_registry.get("fill")(self.dtype, self.shape, 0.0)
        return cast_to_adapter_tensor(output)

    def zero_(self):
        output = self.zero_adapter()
        return _tensor_inplace_assign(self, output, "zero_", "zero_adapter")

    def new_zeros(self, size, *, dtype=None, device=None, requires_grad=False, layout=None, pin_memory=False):
        unsupported_attr(device)
        unsupported_attr(requires_grad)
        unsupported_attr(layout)
        if layout:
            raise NotImplementedError("layout is not supported.")
        unsupported_attr(pin_memory)
        if pin_memory is True:
            raise NotImplementedError("pin_memory is not supported to True.")

        output = tensor_operator_registry.get("fill")(dtype, size, 0.0)
        return cast_to_adapter_tensor(output)

    def new_full(self, size, fill_value, *, dtype=None, device=None, requires_grad=False,
                 layout=None, pin_memory=False):
        unsupported_attr(device)
        unsupported_attr(requires_grad)
        unsupported_attr(layout)
        if layout:
            raise NotImplementedError("layout is not supported.")
        unsupported_attr(pin_memory)
        if pin_memory is True:
            raise NotImplementedError("pin_memory is not supported to True.")

        if not dtype:
            dtype = self.dtype

        output = tensor_operator_registry.get("fill")(dtype, size, fill_value)
        return cast_to_adapter_tensor(output)

    def add(self, other, *, alpha=1):
        input = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        output = ms.ops.add(input, other*alpha)
        return cast_to_adapter_tensor(output)

    def add_(self, other, *, alpha=1):
        output = self.add(other, alpha=alpha)
        return _tensor_inplace_assign(self, output, "add_", "add")

    def erfinv(self):
        input = cast_to_ms_tensor(self)
        output = ms.ops.erfinv(input)
        return cast_to_adapter_tensor(output)

    def erfinv_(self):
        output = self.erfinv()
        return _tensor_inplace_assign(self, output, "erfinv_", "erfinv")

    def permute(self, *dims):
        ms_input = cast_to_ms_tensor(self)
        output = ms_input.transpose(*dims)
        return cast_to_adapter_tensor(output)

    def contiguous(self, memory_format=None):
        #TODO
        unsupported_attr(memory_format)
        return self

    def new_tensor(self, data, *, dtype=None, device=None, requires_grad=False, layout=None, pin_memory=False):
        unsupported_attr(device)
        unsupported_attr(requires_grad)
        unsupported_attr(layout)
        unsupported_attr(pin_memory)
        if isinstance(data, Tensor):
            raise ValueError("To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() "
                             "or sourceTensor.clone().detach().requires_grad_(True), "
                             "rather than tensor.new_tensor(sourceTensor).")
        return tensor(data, dtype)

    def copy_(self, src, non_blocking=False):
        unsupported_attr(non_blocking)
        input_ms = cast_to_ms_tensor(src)
        output = ms.ops.broadcast_to(input_ms, self.shape)
        output = output.astype(self.dtype)
        return _tensor_inplace_assign(self, output, "copy_", "new_tensor")

    def expand(self, *size):
        input_ms = cast_to_ms_tensor(self)
        if isinstance(size[0], (list, tuple)):
            size = size[0]
        out = ms.ops.broadcast_to(input_ms, size)
        return cast_to_adapter_tensor(out)

    def sigmoid(self):
        input = cast_to_ms_tensor(self)
        output = _get_cache_prim(P.Sigmoid)()(input)
        return cast_to_adapter_tensor(output)

    def sigmoid_(self):
        output = self.sigmoid()
        return _tensor_inplace_assign(self, output, "sigmoid_", "sigmoid")

    def float(self, memory_format=None):
        unsupported_attr(memory_format)
        if memory_format:
            raise NotImplementedError("memory_format is not supported.")
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.float())

    def flip(self, dims): # TODO ms.numpy.flip -> Tensor.flip
        input_ms = cast_to_ms_tensor(self)
        output = ms.numpy.flip(input_ms, dims)
        return cast_to_adapter_tensor(output)

    def sign(self):
        input = cast_to_ms_tensor(self)
        output = _get_cache_prim(P.Sign)()(input)
        return cast_to_adapter_tensor(output)

    def mul(self, value):
        input = cast_to_ms_tensor(self)
        ms_value = cast_to_ms_tensor(value)
        output = ms.ops.mul(input, ms_value)
        return cast_to_adapter_tensor(output)

    def mul_(self, value):
        output = self.mul(value)
        return _tensor_inplace_assign(self, output, "mul_", "mul")

    def device(self):
        #TODO
        pass

    def div(self, value, *, rounding_mode=None) :
        output = _div_calcu(self, value, rounding_mode)
        return cast_to_adapter_tensor(output)

    def div_(self, value, *, rounding_mode=None):
        output = _div_calcu(self, value, rounding_mode)
        return _tensor_inplace_assign(self, output, "div_", "div")

    def cpu(self):
        #TODO
        return self

    def min(self, dim=None, keepdim=False):
        input = cast_to_ms_tensor(self)
        if dim is None:
            return cast_to_adapter_tensor(input.min())
        #TODO
        # Until now, P.min do not support when `input` is type of `int32`, `int64``.
        if self.dtype == mstype.int64 or self.dtype == mstype.int32:
            if self.dtype == mstype.int64:
                dtype_name = 'torch.int64'
            else:
                dtype_name = 'torch.int32'
            raise TypeError("For 'Tensor.min', the type of `input` do not support `torch.int64` and "
                            "`torch.int32`, got {}.".format(dtype_name))

        indices, result = P.min(input, axis=dim, keep_dims=keepdim)
        return cast_to_adapter_tensor(result), cast_to_adapter_tensor(indices)

    def max(self, dim=None, keepdim=False):
        input = cast_to_ms_tensor(self)
        if dim is None:
            return cast_to_adapter_tensor(input.max())
        # TODO: Until now, P.max do not support when `input` is type of `int32`, `int64``.
        if self.dtype == mstype.int64 or self.dtype == mstype.int32:
            if self.dtype == mstype.int64:
                dtype_name = 'torch.int64'
            else:
                dtype_name = 'torch.int32'
            raise TypeError("For 'Tensor.max', the type of `input` do not support `torch.int64` and "
                            "`torch.int32`, got {}.".format(dtype_name))

        indices, result = P.max(input, axis=dim, keep_dims=keepdim)
        return cast_to_adapter_tensor(result), cast_to_adapter_tensor(indices)

    def numel(self):
        input = cast_to_ms_tensor(self)
        return P.size(input)

    def detach(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.stop_gradient(input_ms)
        return cast_to_adapter_tensor(output)

    def sum(self, dim=None, keepdim=False, dtype=None):
        input = cast_to_ms_tensor(self)
        if not dtype and self.dtype in (mstype.uint8, mstype.uint16, mstype.uint32,
                                        mstype.int8, mstype.int16, mstype.int32):
            dtype = mstype.int64
            input = input.astype(dtype)
        return cast_to_adapter_tensor(input.sum(axis=dim, dtype=dtype, keepdims=keepdim))

    def mean(self, dim=None, keepdim=False, dtype=None):
        if dim is None:
            axis = ()
        else:
            axis = dim

        input = cast_to_adapter_tensor(self)
        if dtype:
            input = self.astype(dtype)

        output = ms.ops.mean(input, axis, keepdim)
        return cast_to_adapter_tensor(output)

    def prod(self, dim=None, keepdim=False, dtype=None):
        if dim is None:
            axis = ()
        else:
            axis = dim

        input = cast_to_adapter_tensor(self)
        if dtype:
            input = self.astype(dtype)

        output = ms.ops.prod(input, axis, keepdim)
        return cast_to_adapter_tensor(output)

    def split(self, split_size, dim=0):
        tensor = cast_to_ms_tensor(self)
        output = ms.ops.split(tensor, split_size, dim)
        return cast_to_adapter_tensor(output)

    def numpy(self):
        return self.asnumpy()

    def view(self, *shape):
        self._init_check()
        if not shape:
            raise ValueError("The shape variable should not be empty")
        if isinstance(shape[0], (tuple, list)):
            if len(shape) != 1:
                raise ValueError(f"Only one tuple is needed, but got {shape}")
            shape = shape[0]
        if isinstance(shape, list):
            shape = tuple(shape)

        input_size = self.shape
        if input_size[0] == 0:  # only support first element is 0
            numel = ms.ops.size(self)
            shape = _infer_size(shape, numel)
            output = ms.ops.zeros(shape, self.dtype)
        else:
            input = cast_to_ms_tensor(self)
            output = tensor_operator_registry.get('reshape')()(input, shape)
        return cast_to_adapter_tensor(output)

    def view_as(self, other):
        return self.view(other.shape)

    def ndimension(self):
        input_ms = cast_to_ms_tensor(self)
        return input_ms.ndimension()

    def pow(self, exponent):
        power = cast_to_ms_tensor(exponent)
        input_ms = cast_to_ms_tensor(self)
        output = input_ms.pow(power)
        return cast_to_adapter_tensor(output)

    def repeat(self, *sizes):
        input_x = cast_to_ms_tensor(self)
        if isinstance(sizes[0], (tuple, list)):
            output = ms.ops.tile(input_x, *sizes)
        else:
            output = ms.ops.tile(input_x, sizes)
        return cast_to_adapter_tensor(output)

    def repeat_interleave(self, repeats, dim=None, *, output_size=None):
        unsupported_attr(output_size)

        if isinstance(repeats, Tensor):
            new_repeats = []
            for index in repeats:
                new_repeats.append(int(index))
            repeats = new_repeats
        input_ms = cast_to_ms_tensor(self)
        output = input_ms.repeat(repeats, dim)
        return cast_to_adapter_tensor(output)

    def reshape(self, *shape):
        input_ms = cast_to_ms_tensor(self)
        input_size = input_ms.shape
        if input_size[0] == 0:  # only support first element is 0
            numel = ms.ops.size(input_ms)
            shape = _infer_size(shape, numel)
            output = ms.ops.zeros(shape, input_ms.dtype)
        else:
            output = input_ms.reshape(*shape)
        return cast_to_adapter_tensor(output)

    def reshape_as(self, other):
        return self.reshape(other.shape)

    def arcsinh(self):
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.arcsinh())

    def arctanh(self):
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.arctanh())

    def det(self):
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.det())

    def negative(self):
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.negative())

    def negative_(self):
        output = self.negative()
        return _tensor_inplace_assign(self, output, "negative_", "negative")

    def abs(self):
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.abs())

    def abs_(self):
        output = self.abs()
        return _tensor_inplace_assign(self, output, "abs_", "abs")

    @property
    def ndim(self):
        return len(self.shape)

    def amax(self, dim=None, keepdim=False):
        input_ms = cast_to_ms_tensor(self)
        if dim is not None:
            return cast_to_adapter_tensor(input_ms.amax(axis=dim, keep_dims=keepdim))
        return cast_to_adapter_tensor(input_ms.amax(keep_dims=keepdim))

    def amin(self, dim=None, keepdim=False):
        input_ms = cast_to_ms_tensor(self)
        if dim is not None:
            return cast_to_adapter_tensor(input_ms.amin(axis=dim, keep_dims=keepdim))
        return cast_to_adapter_tensor(input_ms.amin(keep_dims=keepdim))

    def as_strided(self, size, stride, storage_offset=None):
        warnings.warn("not support output as a view.")
        input_ms = cast_to_ms_tensor(self)
        if len(size) != len(stride):
            raise RuntimeError("mismatch in length of strides and shape.")
        index = np.arange(0, size[0]*stride[0], stride[0])
        for i in range(1, len(size)):
            tmp = np.arange(0, size[i]*stride[i], stride[i])
            index = np.expand_dims(index, -1)
            index = index + tmp
        if storage_offset is not None:
            index = index + storage_offset
        input_indices = ms.Tensor(index)
        out = ms.ops.gather(input_ms.reshape(-1), input_indices, 0)
        return cast_to_adapter_tensor(out)

    def bmm(self, batch2):
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.bmm(batch2))

    def clamp(self, min=None, max=None):
        input_ms = cast_to_ms_tensor(self)
        type = input_ms.dtype
        if min is not None and max is not None and min > max:
            output = ms.ops.ones_like(input_ms).astype(type)*max
        else:
            if min is not None:
                min = ms.Tensor(min, type)
            if max is not None:
                max = ms.Tensor(max, type)
            output = ms.ops.clip_by_value(input_ms, min, max)
        return cast_to_adapter_tensor(output)

    def clamp_(self, min=None, max=None):
        output = self.clamp(min, max)
        return _tensor_inplace_assign(self, output, "clamp_", "clamp")

    def dim(self):
        return len(self.shape)

    def expand_as(self, other):
        input_ms = cast_to_ms_tensor(self)
        output = input_ms.expand_as(other)
        return cast_to_adapter_tensor(output)

    def item(self):
        input_ms = cast_to_ms_tensor(self)
        if input_ms.size > 1:
            raise ValueError("only one element tensors can be converted to Python scalars")
        output = input_ms.reshape(-1).asnumpy().tolist()
        return output[0]

    def log(self):
        input_ms = cast_to_ms_tensor(self)
        output = input_ms.log()
        return cast_to_adapter_tensor(output)

    def log2(self):
        input = cast_to_ms_tensor(self)
        output = ms.ops.log2(input)
        return cast_to_adapter_tensor(output)

    def matmul(self, tensor2):
        input_ms = cast_to_ms_tensor(self)
        tensor2_ms = cast_to_ms_tensor(tensor2)
        output = ms.ops.matmul(input_ms, tensor2_ms)
        return cast_to_adapter_tensor(output)

    def squeeze(self, dim=None):
        input_ms = cast_to_ms_tensor(self)
        if dim is not None:
            if input_ms.shape[dim] != 1:
                output = input_ms
            else:
                output = ms.ops.squeeze(input_ms, dim)
        else:
            output = ms.ops.squeeze(input_ms)
        return cast_to_adapter_tensor(output)

    def squeeze_(self, dim=None):
        output = self.squeeze(dim)
        return _tensor_inplace_assign(self, output, "squeeze_", "squeeze")

    def stride(self, dim=None):
        input_ms = cast_to_ms_tensor(self)
        bytelen = input_ms.nbytes//input_ms.size
        output = list(input_ms.strides)
        for i in range(len(output)):
            output[i] = output[i]//bytelen
        output = tuple(output)
        if dim is not None:
            output = output[dim]
        return output

    def sub(self, other, *, alpha=1):
        input_ms = cast_to_ms_tensor(self)
        input_other = cast_to_ms_tensor(other) * alpha
        output = ms.ops.sub(input_ms, input_other)
        return cast_to_adapter_tensor(output)

    def sub_(self, other, *, alpha=1):
        output = self.sub(other, alpha=alpha)
        return _tensor_inplace_assign(self, output, "sub_", "sub")

    # TODO: delete it, apply ms.Tensor.is_floating_point
    def is_floating_point(self):
        return self._dtype in (mstype.float16, mstype.float32, mstype.float64)

    def unbind(self, dim=0):
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.unbind(dim))

    def unsqueeze(self, dim):
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.unsqueeze(dim))

    def unsqueeze_(self, dim):
        output = self.unsqueeze(dim)
        return _tensor_inplace_assign(self, output, "unsqueeze_", "unsqueeze")

    def is_signed(self):
        # input_ms = cast_to_ms_tensor(self)
        # return input_ms.is_signed() #TODO mindspore 11/17 2.0nightly supported
        pass

    def transpose(self, dim0, dim1):
        input_ms = cast_to_ms_tensor(self)
        dims = list(range(input_ms.ndim))
        dims[dim0], dims[dim1] = dim1, dim0
        output = input_ms.transpose(dims)
        return cast_to_adapter_tensor(output)

    def transpose_(self, dim0, dim1):
        output = self.transpose(dim0, dim1)
        return _tensor_inplace_assign(self, output, "transpose_", "transpose")

    def floor(self):
        input_ms = cast_to_ms_tensor(self)
        output = input_ms.floor()
        return cast_to_adapter_tensor(output)

    def floor_(self):
        output = self.floor()
        return _tensor_inplace_assign(self, output, "floor_", "floor")

    def isfinite(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.isfinite(input_ms)
        return cast_to_adapter_tensor(output)

    def isnan(self):
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.isnan())

    def clone(self):
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.copy())

    def to(self, *args, **kwargs):
        # TODO:
        # Note that this API requires the user to ensure the correctness of the input currently,
        # and only the function of modifying dtype is available.

        if len(args) == 0 and len(kwargs) == 0:
            raise ValueError("Tensor.to is missing inputs, please check.")
        input_ms = cast_to_ms_tensor(self)

        if "dtype" in kwargs:
            set_dtype = kwargs.get("dtype")
            return cast_to_adapter_tensor(input_ms.astype(set_dtype))
        elif "other" in kwargs:
            set_dtype = kwargs.get("other")._dtype
            return cast_to_adapter_tensor(input_ms.astype(set_dtype))
        elif "device" in kwargs:
            return self

        if len(args) == 0:
            raise ValueError("The inputs of Tensor.to is abnormal, please check.")

        if args[0] in _dtypeDict.values():
            return cast_to_adapter_tensor(input_ms.astype(args[0]))
        elif isinstance(args[0], Tensor):
            set_dtype = args[0]._dtype
            return cast_to_adapter_tensor(input_ms.astype(set_dtype))
        elif not isinstance(args[0], (str, Device)):
            raise ValueError("The inputs of Tensor.to is abnormal, please check.")

        if len(args) > 1 and args[1] in _dtypeDict.values():
            return cast_to_adapter_tensor(input_ms.astype(args[1]))
        return self

    def sort(self, dim=-1, descending=False):
        # TODO: ops.sort() should be replaced.
        input_ms = cast_to_ms_tensor(self)
        input_type = input_ms.dtype
        if 'Int' in str(input_type):
            input_ms = input_ms.astype(ms.float32)
            sort_tensor, sort_index = ms.ops.Sort(dim, descending)(input_ms)
            sort_tensor = sort_tensor.astype(input_type)
            sort_index = sort_index.astype(ms.int64)
            return cast_to_adapter_tensor((sort_tensor, sort_index))
        else:
            output = _get_cache_prim(ms.ops.Sort)(dim, descending)(input_ms)
        return cast_to_adapter_tensor(output)

    def msort(self):
        # TODO: ops.sort() should be replaced.
        input_ms = cast_to_ms_tensor(self)
        sort_op = _get_cache_prim(ms.ops.Sort)(axis=0)
        input_type = input_ms.dtype
        if 'Int' in str(input_type):
            input_ms = input_ms.astype(ms.float32)
            output, _ = sort_op(input_ms)
            output = output.astype(input_type)
        else:
            output, _ = sort_op(input_ms)
        return cast_to_adapter_tensor(output)

    def argsort(self, dim=-1, descending=False):
        # TODO: ops.sort() should be replaced.
        input_ms = cast_to_ms_tensor(self)
        sort_op = _get_cache_prim(ms.ops.Sort)(dim, descending)
        input_type = input_ms.dtype
        if 'Int' in str(input_type):
            input_ms = input_ms.astype(ms.float32)
            _, output = sort_op(input_ms)
            output = output.astype(ms.int64)
        else:
            _, output = sort_op(input_ms)
        return cast_to_adapter_tensor(output)

    def sqrt(self):
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(ms.ops.sqrt(input_ms))

    def sqrt_(self):
        output = self.sqrt()
        return _tensor_inplace_assign(self, output, "sqrt_", "sqrt")

    def rsqrt(self):
        input = cast_to_ms_tensor(self)
        if 'Bool' in str(input.dtype) or 'Int' in str(input.dtype):
            input = input.astype(ms.float32)
        output = _get_cache_prim(ms.ops.Rsqrt)()(input)
        return cast_to_adapter_tensor(output)

    def rsqrt_(self):
        output = self.rsqrt()
        return _tensor_inplace_assign(self, output, "rsqrt_", "rsqrt")

    def resize(self, *size, memory_format=None):
        unsupported_attr(memory_format)
        input = cast_to_ms_tensor(self)
        input_size = input.shape
        if len(input_size) == 1 and input_size[0] == 0:
            out = ms.ops.zeros(size, self.dtype)
        elif len(size) > 0 and isinstance(size[0], tuple):
            out = input.resize(size[0])
        else:
            out = input.resize(size)
        return cast_to_adapter_tensor(out)

    def resize_(self, *size, memory_format=None):
        output = self.resize(*size, memory_format=memory_format)
        return _tensor_inplace_assign(self, output, "resize_", "resize")

    def resize_as(self, tensor, memory_format=None):
        unsupported_attr(memory_format)
        if not isinstance(tensor, Tensor):
            raise TypeError("resize_as(): argument 'tensor' must be Tensor.")
        input = cast_to_ms_tensor(self)
        size = tensor.shape
        input_size = input.shape
        if len(input_size) == 1 and input_size[0] == 0:
            out = ms.ops.zeros(size, self.dtype)
        else:
            out = input.resize(size)
        return cast_to_adapter_tensor(out)

    def resize_as_(self, tensor, memory_format=None):
        output = self.resize_as(tensor, memory_format)
        return _tensor_inplace_assign(self, output, "resize_as_", "resize_as")

    def index_fill(self, dim, index, value):
        input = cast_to_ms_tensor(self)
        index = cast_to_ms_tensor(index)
        index = ms.ops.cast(index, mstype.int32)

        if is_under_ascend_context():
            raise NotImplementedError("for adapter, index_fill not supported on ascend.")
        out = input.index_fill(dim, index, value)
        return cast_to_adapter_tensor(out)

    def index_fill_(self, dim, index, value):
        output = self.index_fill(dim, index, value)
        return _tensor_inplace_assign(self, output, "index_fill_", "index_fill")

    def index_select(self, dim, index):
        _input_params = cast_to_ms_tensor(self)
        _input_indices = cast_to_ms_tensor(index)

        output = ms.ops.gather(_input_params, _input_indices, dim)
        return cast_to_adapter_tensor(output)

    @property
    def data(self):
        return self.detach()

    def new(self, *size):
        if len(size) > 0 and isinstance(size[0], tuple):
            size = size[0]
        return Tensor(*size, dtype=self.dtype)

    def cuda(self, device=None, non_blocking=False, memory_format=None):
        unsupported_attr(device)
        unsupported_attr(non_blocking)
        unsupported_attr(memory_format)
        if not is_under_gpu_context():
            backend = get_backend()
            warning = f"MsAdater.pytorch.Tensor.cuda() didn't work because it is under {backend} context."
            warnings.warn(warning)
        return self

    def is_cuda(self):
        return is_under_gpu_context()

    def le(self, other):
        input = cast_to_ms_tensor(self)
        if isinstance(other, Tensor):
            other = cast_to_ms_tensor(other)
        out = ms.ops.le(input, other)
        return cast_to_adapter_tensor(out)

    def le_(self, other):
        output = self.le(other)
        return _tensor_inplace_assign(self, output, "le_", "le")

    def t(self):
        input_ms = cast_to_ms_tensor(self)
        if input_ms.ndim > 2:
            raise ValueError("t() expects a tensor with <= 2 dimensions, but self is {}D".format(input_ms.ndim))
        dims = list(range(input_ms.ndim)).reverse()
        output = input_ms.transpose(dims)
        return cast_to_adapter_tensor(output)

    @property
    def T(self):
        input_ms = cast_to_ms_tensor(self)
        if input_ms.ndim <= 2:
            warning = ("The use of Tensor.T() on tensors of dimension other than 2 to reverse "
                       "their shape is deprecated and it will throw an error in a future release. ")
            warnings.warn(warning)
        dims = list(range(input_ms.ndim)).reverse()
        output = input_ms.transpose(dims)
        return cast_to_adapter_tensor(output)

    @property
    def requires_grad(self):
        return True

    def requires_grad_(self, requires_grad=True):
        if requires_grad is False:
            warnings.warn("requires_grad is always True in Tensor.")
        return self

    def nonzero(self,  *, out=None, as_tuple=False):
        if out is not None:
            warnings.warn("Do not support parameter 'out'.")
        input = cast_to_ms_tensor(self)
        output = None
        if as_tuple:
            if input.ndim == 1:
                res = ms.ops.nonzero(input)
                output = (cast_to_adapter_tensor(res.flatten()),)
            elif input.ndim > 1:
                output = []
                res = ms.ops.nonzero(input)
                res = res.transpose(1, 0)
                res = ms.ops.split(res, input.ndim, axis=0)
                for cur in res:
                    output.append(cast_to_adapter_tensor(cur))
                output = tuple(output)
            elif input.ndim == 0:
                raise ValueError("Do not support input ndim == 0.")
            return output
        return cast_to_adapter_tensor(ms.ops.nonzero(input))

    def bool(self, memory_format=None):
        unsupported_attr(memory_format)
        input = cast_to_ms_tensor(self)
        output = input.bool()
        return cast_to_adapter_tensor(output)

    def eq(self, other):
        input_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        output = input_ms.equal(other_ms)
        return cast_to_adapter_tensor(output)

    def eq_(self, other):
        output = self.eq(other)
        return _tensor_inplace_assign(self, output, "eq_", "eq")

    def std(self, dim=None, unbiased=True, keepdim=False):
        #TODO: not support float64 or complex input
        input_ms = cast_to_ms_tensor(self)
        type_float64 = False
        if input_ms.dtype == ms.float64:
            input_ms = input_ms.astype(ms.float32)
            type_float64 = True

        # TODO: mindspore.ops.std() not supported GPU, use tensor.std() instead, which means ms.ops.var().
        if is_under_gpu_context():
            _dim = dim if dim is not None else ()
            _ddof = 1 if unbiased else 0
            output = input_ms.std(_dim, _ddof, keepdim)
        else:
            if dim is not None:
                output, _ = ms.ops.std(input_ms, dim, unbiased, keepdim)
            else:
                output, _ = ms.ops.std(input_ms,  unbiased=unbiased, keep_dims=keepdim)

        if type_float64:
            output = output.astype(ms.float64)
        return cast_to_adapter_tensor(output)

    def exp(self):
        input_ms = cast_to_ms_tensor(self)
        output = input_ms.exp()
        return cast_to_adapter_tensor(output)

    def masked_fill(self, mask, value):
        input_ms = cast_to_ms_tensor(self)
        output = input_ms.masked_fill(mask, value)
        return cast_to_adapter_tensor(output)

    def masked_fill_(self, mask, value):
        output = self.masked_fill(mask, value)
        return _tensor_inplace_assign(self, output, "masked_fill_", "masked_fill")

    def tolist(self):
        return self.numpy().tolist()

    def bernoulli(self, *, generator=None):
        unsupported_attr(generator)
        if generator:
            raise NotImplementedError("generator is not supported.")
        input_ms = cast_to_ms_tensor(self)

        bernoulli_seed = ms.get_seed()
        if not bernoulli_seed:
            bernoulli_seed = -1
        return cast_to_adapter_tensor(input_ms.bernoulli(input_ms, bernoulli_seed))

    def bernoulli_(self, p=0.5, *, generator=None):
        output = self.bernoulli_adapter(p, generator=generator)
        return _tensor_inplace_assign(self, output, "bernoulli_", "bernoulli_adapter")

    def bernoulli_adapter(self, p=0.5, *, generator=None):
        unsupported_attr(generator)
        if generator:
            raise NotImplementedError("generator is not supported.")
        input_ms = cast_to_ms_tensor(self)

        bernoulli_seed = ms.get_seed()
        if not bernoulli_seed:
            bernoulli_seed = -1
        return cast_to_adapter_tensor(input_ms.bernoulli(p, bernoulli_seed))

    def round(self, decimals=0):
        input = cast_to_ms_tensor(self)
        if decimals == 0:
            output = ms.ops.round(input)
        else:
            p = 10 ** decimals
            input = input * p
            output = ms.ops.round(input) / p
        return cast_to_adapter_tensor(output)

    def long(self, memory_format=None):
        unsupported_attr(memory_format)
        if memory_format:
            raise NotImplementedError("memory_format is not supported.")
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.astype(_dtypeDict["long"]))

    def half(self, memory_format=None):
        unsupported_attr(memory_format)
        if memory_format:
            raise NotImplementedError("memory_format is not supported.")
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.astype(_dtypeDict["half"]))

    def int(self, memory_format=None):
        unsupported_attr(memory_format)
        if memory_format:
            raise NotImplementedError("memory_format is not supported.")
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.int())

    def double(self, memory_format=None):
        unsupported_attr(memory_format)
        if memory_format:
            raise NotImplementedError("memory_format is not supported.")
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.astype(_dtypeDict["double"]))

    def char(self, memory_format=None):
        unsupported_attr(memory_format)
        if memory_format:
            raise NotImplementedError("memory_format is not supported.")
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.astype(_dtypeDict["char"]))

    def byte(self, memory_format=None):
        unsupported_attr(memory_format)
        if memory_format:
            raise NotImplementedError("memory_format is not supported.")
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.astype(_dtypeDict["byte"]))

    def short(self, memory_format=None):
        unsupported_attr(memory_format)
        if memory_format:
            raise NotImplementedError("memory_format is not supported.")
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.astype(_dtypeDict["short"]))


    def chunk(self, chunks, dim=0):
        input = cast_to_ms_tensor(self)
        output = ms.ops.chunk(input, chunks, dim)
        return cast_to_adapter_tensor(output)

    def flatten(self, start_dim=0, end_dim=-1):
        @constexpr
        def get_dst_shape():
            self_shape = self.shape
            rank = len(self_shape)
            start = start_dim
            end = end_dim

            if start < 0:
                start += rank

            if end < 0:
                end += rank

            dst_shape = []
            i = 0
            while i != start:
                dst_shape.append(self_shape[i])
                i = i + 1

            flatten_shape = 1
            while i <= end:
                flatten_shape = flatten_shape * self_shape[i]
                i = i + 1
            dst_shape.append(flatten_shape)

            while i < rank:
                dst_shape.append(self_shape[i])
                i = i + 1

            return tuple(dst_shape)

        shape = get_dst_shape()

        input_ms = cast_to_ms_tensor(self)
        input_ms.reshape(shape)
        return cast_to_adapter_tensor(input_ms.reshape(shape))

    def sin(self):
        input = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(ms.ops.sin(input))

    def sin_(self):
        output = self.sin()
        return _tensor_inplace_assign(self, output, "sin_", "sin")

    def ge(self, other):
        input = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        output = input.ge(other)
        return cast_to_adapter_tensor(output)

    def ge_(self, other):
        output = self.ge(other)
        return _tensor_inplace_assign(self, output, "ge_", "ge")

    def cumsum(self, dim, dtype=None):
        input = cast_to_ms_tensor(self)
        output = input.cumsum(axis=dim, dtype=dtype)
        return cast_to_adapter_tensor(output)

    def absolute(self):
        return self.abs()

    def absolute_(self):
        output = self.abs()
        return _tensor_inplace_assign(self, output, "absolute_", "absolute")

    def acos(self):
        input = cast_to_ms_tensor(self)
        output = ms.ops.acos(input)
        return cast_to_adapter_tensor(output)

    def acos_(self):
        output = self.acos()
        return _tensor_inplace_assign(self, output, "acos_", "acos")

    def arccos(self):
        return self.acos()

    def arccos_(self):
        output = self.acos()
        return _tensor_inplace_assign(self, output, "arccos_", "arccos")

    def asinh(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.asinh(input_ms)
        return cast_to_adapter_tensor(output)

    def asinh_(self):
        output = self.asinh()
        return _tensor_inplace_assign(self, output, "asinh_", "asinh")

    def atanh(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.atanh(input_ms)
        return cast_to_adapter_tensor(output)

    def atanh_(self):
        output = self.atanh()
        return _tensor_inplace_assign(self, output, "atanh_", "atanh")

    def addcdiv(self, tensor1, tensor2, *, value=1):
        input = cast_to_ms_tensor(self)
        tensor1 = cast_to_ms_tensor(tensor1)
        tensor2 = cast_to_ms_tensor(tensor2)
        value = ms.Tensor(value)
        output = ms.ops.addcdiv(input, tensor1, tensor2, value)
        return cast_to_adapter_tensor(output)

    def addcdiv_(self, tensor1, tensor2, *, value=1):
        output = self.addcdiv(tensor1, tensor2, value=value)
        return _tensor_inplace_assign(self, output, "addcdiv_", "addcdiv")

    def gather(self, dim, index):
        input = cast_to_ms_tensor(self)
        index = cast_to_ms_tensor(index)
        output = ms.ops.gather_elements(input, dim, index)
        return cast_to_adapter_tensor(output)

    def fmod(self, divisor):
        x = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(divisor)
        #TODO: repalce with ms.ops.fmod
        if not (isinstance(x, (Tensor, Tensor_)) or isinstance(other, (Tensor, Tensor_))):
            raise TypeError("At least one of the types of inputs must be tensor, " + \
                            f"but the type of 'x' got is {type(x)}, " + \
                            f"and the type of 'other' is {type(other)}.")
        return x - ms.ops.div(x, other, rounding_mode="trunc") * other

    def fmod_(self, divisor):
        output = self.fmod(divisor)
        return _tensor_inplace_assign(self, output, "fmod_", "fmod")

    def lt(self, other):
        input = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        output = ms.ops.less(input, other)
        return cast_to_adapter_tensor(output)

    def lt_(self, other):
        output = self.lt(other)
        return _tensor_inplace_assign(self, output, "lt_", "lt")

    def less(self, other):
        return self.lt(other)

    def less_(self, other):
        output = self.lt(other)
        return _tensor_inplace_assign(self, output, "less_", "less")

    def less_equal(self, other):
        input = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        output = ms.ops.less_equal(input, other)
        return cast_to_adapter_tensor(output)

    def less_equal_(self, other):
        output = self.less_equal(other)
        return _tensor_inplace_assign(self, output, "less_equal_", "less_equal")

    def ne(self, other):
        input = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        output = ms.ops.ne(input, other)
        return cast_to_adapter_tensor(output)

    def ne_(self, other):
        output = self.ne(other)
        return _tensor_inplace_assign(self, output, "ne_", "ne")

    def not_equal(self, other):
        return self.ne(other)

    def not_equal_(self, other):
        output = self.ne(other)
        return _tensor_inplace_assign(self, output, "not_equal_", "not_equal")

    def equal(self, other):
        if not isinstance(other, Tensor):
            raise ValueError("`other` must be Tensor")
        x = cast_to_ms_tensor(self)
        y = cast_to_ms_tensor(other)

        if x.dtype != y.dtype:
            return False
        if x.shape == y.shape:
            size = x.size
            output = ms.ops.equal(x, y)
            output = output.sum()
            if output == size:
                return True
        return False

    def greater(self, other):
        input = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        output = ms.ops.greater(input, other)
        return cast_to_adapter_tensor(output)

    def greater_(self, other):
        output = self.greater(other)
        return _tensor_inplace_assign(self, output, "greater_", "greater")

    def gt(self, other):
        input = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        output = ms.ops.gt(input, other)
        return cast_to_adapter_tensor(output)

    def gt_(self, other):
        output = self.greater(other)
        return _tensor_inplace_assign(self, output, "gt_", "gt")

    def greater_equal(self, other):
        x = cast_to_ms_tensor(self)
        y = cast_to_ms_tensor(other)
        output = ms.ops.greater_equal(x, y)
        return cast_to_adapter_tensor(output)

    def greater_equal_(self, other):
        output = self.greater_equal(other)
        return _tensor_inplace_assign(self, output, "greater_equal_", "greater_equal")

    def argmin(self, dim=None, keepdim=False):
        input = cast_to_ms_tensor(self)
        # TODO: output = ms.ops.argmin(input, axis=dim, keepdims=keepdim)
        if keepdim:
            raise NotImplementedError("keepdim is not supported.")

        # TODO: ascend not support argmin
        if is_under_ascend_context():
            input = input * -1
            output = ms.ops.argmax(input, axis=dim)
        else:
            output = ms.ops.argmin(input, axis=dim)
        return cast_to_adapter_tensor(output)

    def argmax(self, dim=None, keepdim=False):
        input = cast_to_ms_tensor(self)
        # TODO: output = ms.ops.argmax(input, axis=dim, keepdims=keepdim)
        if keepdim:
            raise NotImplementedError("keepdim is not supported.")
        output = ms.ops.argmax(input, axis=dim)
        return cast_to_adapter_tensor(output)

    def type(self, dtype=None, non_blocking=False, **kwargs):
        def _get_type_from_dtype(dtype):
            str_dtype = str(dtype).split('.')[-1].lower()
            _type = _dtype2typeDict.get(str_dtype)
            return _type

        def _get_dtype_from_type(type):
            _dtype = _type2dtypeDict.get(type, 'None')
            if _dtype == 'None':
                _dtype = type
            return _dtype

        unsupported_attr(non_blocking)
        unsupported_attr(kwargs)
        if dtype is None:
            return _get_type_from_dtype(self.dtype)

        _dtype =  _get_dtype_from_type(dtype)
        if _dtype == self.dtype:
            return self
        x = cast_to_ms_tensor(self)
        output = x.astype(_dtype)
        return cast_to_adapter_tensor(output)

    def type_as(self, tensor):
        if self.dtype == tensor.dtype:
            return self
        x = cast_to_ms_tensor(self)
        output = x.astype(tensor.dtype)
        return cast_to_adapter_tensor(output)

    def get_device(self):
        return -1

    def baddbmm(self, batch1, batch2, *, beta=1, alpha=1):
        x = cast_to_ms_tensor(self)
        batch1 = cast_to_ms_tensor(batch1)
        batch2 = cast_to_ms_tensor(batch2)
        output = ms.ops.baddbmm(x, batch1, batch2, beta, alpha)
        return cast_to_adapter_tensor(output)

    def baddbmm_(self, batch1, batch2, *, beta=1, alpha=1):
        output = self.baddbmm(batch1, batch2, beta=beta, alpha=alpha)
        return _tensor_inplace_assign(self, output, "baddbmm_", "baddbmm")

    def topk(self, k, dim=None, largest=True, sorted=True):
        unsupported_attr(dim)
        unsupported_attr(largest)
        input = cast_to_ms_tensor(self)
        output = input.top_k(k, sorted=sorted)
        return cast_to_adapter_tensor(output)

    def maximum(self, other):
        x = cast_to_ms_tensor(self)
        y = cast_to_ms_tensor(other)
        #TODO: NAN is different
        output = ms.ops.maximum(x, y)
        return cast_to_adapter_tensor(output)

    def minimum(self, other):
        x = cast_to_ms_tensor(self)
        y = cast_to_ms_tensor(other)
        #TODO: NAN is different
        output = ms.ops.minimum(x, y)
        return cast_to_adapter_tensor(output)

    def multiply(self, value):
        x = cast_to_ms_tensor(self)
        y = cast_to_ms_tensor(value)
        output = ms.ops.mul(x, y)
        return cast_to_adapter_tensor(output)

    def multiply_(self, value):
        output = self.multiply(value)
        return _tensor_inplace_assign(self, output, "multiply_", "multiply")

    def neg(self):
        x = cast_to_ms_tensor(self)
        output = ms.ops.neg(x)
        return cast_to_adapter_tensor(output)

    def neg_(self):
        output = self.neg()
        return _tensor_inplace_assign(self, output, "neg_", "neg")

    def ravel(self):
        x = cast_to_ms_tensor(self)
        output = x.ravel()
        return cast_to_adapter_tensor(output)

    def select(self, dim, index):
        input = cast_to_ms_tensor(self)
        _input_indices = ms.Tensor(index)
        output = ms.ops.gather(input, _input_indices, dim)

        @constexpr
        def _get_out_shape(input_shape, dim):
            shape = [input_shape[i] for i in range(len(input_shape)) if i != dim]
            return tuple(shape)

        output_shape = _get_out_shape(input.shape, dim)
        output = output.reshape(output_shape)
        return cast_to_adapter_tensor(output)

    def square(self):
        x = cast_to_ms_tensor(self)
        output = ms.ops.square(x)
        return cast_to_adapter_tensor(output)

    def broadcast_to(self, shape):
        input = cast_to_ms_tensor(self)
        output = ms.ops.broadcast_to(input, shape)
        return cast_to_adapter_tensor(output)

    def divide(self, value, *, rounding_mode=None) :
        output = _div_calcu(self, value, rounding_mode)
        return cast_to_adapter_tensor(output)

    def divide_(self, value, *, rounding_mode=None) :
        output = _div_calcu(self, value, rounding_mode)
        return _tensor_inplace_assign(self, output, "divide_", "divide")

    def unique(self, sorted=True, return_inverse=False, return_counts=False, dim=None):
        unsupported_attr(dim)
        unsupported_attr(return_counts)
        input = cast_to_ms_tensor(self)
        data_type = input.dtype
        if sorted and return_inverse:
            raise ValueError("Don't support sorted=True and return_inverse=True.")

        res, idx = ms.ops.unique(input)
        if sorted:
            res = ms.ops.cast(res, ms.float32)
            res, _ = ms.ops.sort(res)
            res = ms.ops.cast(res, data_type)
        if return_inverse:
            res = cast_to_adapter_tensor(res)
            idx = cast_to_adapter_tensor(idx)
            return (res, idx)
        else:
            res = cast_to_adapter_tensor(res)
            return res

    def mm(self, mat2):
        input = cast_to_ms_tensor(self)
        input2 = cast_to_ms_tensor(mat2)
        input_type = input.dtype
        if input_type in (mstype.int32,mstype.int64):
            input = self.astype(mstype.float32)
            output = ms.ops.matmul(input, input2)
            output = ms.ops.cast(output, input_type)
        else:
            output = ms.ops.matmul(input, input2)
        return cast_to_adapter_tensor(output)

    def logsumexp(self, dim, keepdim=False):
        ms_input = cast_to_ms_tensor(self)
        if ms_input.dtype != mstype.float32:
            ms_input = ms_input.astype(mstype.float32)
        output = ms.ops.logsumexp(ms_input, dim, keepdim)
        return cast_to_adapter_tensor(output)

    def addmv(self, mat, vec, *, beta=1, alpha=1):
        input = cast_to_ms_tensor(self)
        mat = cast_to_ms_tensor(mat)
        vec = cast_to_ms_tensor(vec)
        output = ms.ops.addmv(input, mat, vec, beta=beta, alpha=alpha)
        return cast_to_adapter_tensor(output)

    def dot(self, other):
        input = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        #TODO: ms.ops.tensor_dot only supports float16/float32
        input_dtype = input.dtype
        if input_dtype in (mstype.float32, mstype.float16):
            output = ms.ops.tensor_dot(input, other, 1)
        else:
            input = input.astype(ms.float32)
            other = other.astype(ms.float32)
            output = ms.ops.tensor_dot(input, other, 1)
            output = output.astype(input_dtype)
        return cast_to_adapter_tensor(output)

    def inverse(self):
        input = cast_to_ms_tensor(self)
        #TODO: Ascend has no ms.ops.inverse
        # output = ms.ops.inverse(input)  # ops.inverse is not ready at 11-13
        if self.dtype in msdapter_dtype.all_int_type:
            input = input.astype(mstype.float32)
        output = _get_cache_prim(P.MatrixInverse)()(input)
        return cast_to_adapter_tensor(output)

    def asin(self):
        input = cast_to_ms_tensor(self)
        if self.dtype in msdapter_dtype.all_int_type:
            input = input.astype(mstype.float32)
        output = ms.ops.asin(input)
        return cast_to_adapter_tensor(output)

    def asin_(self):
        output = self.asin()
        return _tensor_inplace_assign(self, output, "asin_", "asin")

    def atan(self):
        input = cast_to_ms_tensor(self)
        if self.dtype in msdapter_dtype.all_int_type:
            input = input.astype(mstype.float32)
        output = ms.ops.atan(input)
        return cast_to_adapter_tensor(output)

    def atan_(self):
        output = self.atan()
        return _tensor_inplace_assign(self, output, "atan_", "atan")

    def atan2(self, other):
        input = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        if self.dtype in msdapter_dtype.all_int_type:
            input = input.astype(mstype.float32)
            other = other.astype(mstype.float32)
        output = ms.ops.atan2(input, other)
        return cast_to_adapter_tensor(output)

    def atan2_(self, other):
        output = self.atan2(other)
        return _tensor_inplace_assign(self, output, "atan2_", "atan2")


    def count_nonzero(self, dim=None):
        input = cast_to_ms_tensor(self)
        if dim is None:
            dim = ()
        output = ms.ops.count_nonzero(input, axis=dim)
        return cast_to_adapter_tensor(output)

    def scatter(self, dim, index, src, reduce=None):
        if not reduce:
            reduce = 'none'
        else:
            # TODO: to supported 'multiply'
            if reduce not in ('none', 'add'):
                raise ValueError("For tensor.scatter or scatter_, `reduce` only support 'none', "
                                 f"'add', but got '{reduce}'.")

            # TODO: add not supported on Ascend yet
            if reduce == 'add' and is_under_ascend_context():
                raise NotImplementedError("For tensor.scatter or scatter_, `reduce` == 'add' not supported on Ascend")

        input, index, src = cast_to_ms_tensor((self, index, src))

        if isinstance(src, numbers.Number):
            src = ms.ops.scalar_to_tensor(src, dtype=input.dtype)
            src = ms.ops.broadcast_to(src, index.shape)
        elif isinstance(src, ms.Tensor):
            src_shape = src.shape
            index_shape = index.shape
            if src_shape != index_shape:
                # TODO
                raise NotImplementedError("For scatter, not support src.shape != index.shape yet")
        else:
            raise TypeError(f"For scatter, `src` must be number or tensor, but got {type(src)}")

        if is_under_ascend_context():
            input_dtype = input.dtype
            input = _ascend_tensor_general_cast(input)
            src = _ascend_tensor_general_cast(src)
            output = ms.ops.tensor_scatter_elements(input, index, src, dim, reduce)
            output = output.astype(input_dtype)
        else:
            output = ms.ops.tensor_scatter_elements(input, index, src, dim, reduce)

        return cast_to_adapter_tensor(output)

    def scatter_(self, dim, index, src, reduce=None):
        output = self.scatter(dim, index, src, reduce)
        return _tensor_inplace_assign(self, output, "scatter_", "scatter")


class _TypeTensor(Tensor):
    def __init__(self, *input_data, dtype_name):
        super(_TypeTensor, self).__init__(*input_data, dtype=dtype_name, inner=False)


class ByteTensor(_TypeTensor):
    def __init__(self, *input_data):
        super(ByteTensor, self).__init__(*input_data, dtype_name='uint8')


class CharTensor(_TypeTensor):
    def __init__(self, *input_data):
        super(CharTensor, self).__init__(*input_data, dtype_name='int8')


class ShortTensor(_TypeTensor):
    def __init__(self, *input_data):
        super(ShortTensor, self).__init__(*input_data, dtype_name='int16')


class IntTensor(_TypeTensor):
    def __init__(self, *input_data):
        super(IntTensor, self).__init__(*input_data, dtype_name='int32')


class HalfTensor(_TypeTensor):
    def __init__(self, *input_data):
        super(HalfTensor, self).__init__(*input_data, dtype_name='float16')


class FloatTensor(_TypeTensor):
    def __init__(self, *input_data):
        super(FloatTensor, self).__init__(*input_data, dtype_name='float32')


class DoubleTensor(_TypeTensor):
    def __init__(self, *input_data):
        super(DoubleTensor, self).__init__(*input_data, dtype_name='float64')


class LongTensor(_TypeTensor):
    def __init__(self, *input_data):
        super(LongTensor, self).__init__(*input_data, dtype_name='int64')


def tensor(data, dtype=None, device=None, requires_grad=True):
    unsupported_attr(device)
    if requires_grad is False:
        msg = ("In Adapter, Tensor's `requires_grad` is always 'True', can not be set to 'False'. ")
        warnings.warn(msg)
    return Tensor(data, dtype=dtype, inner=True)

def cast_to_ms_tensor(inputs):
    """
    Cast MSAdapter.Tensor to MindSpore.Tensor before call mindspore API.
    """
    def _cast(inputs):
        if isinstance(inputs, Tensor):
            inputs = inner.convert_to_ms_tensor(inputs)
        elif isinstance(inputs, (tuple, list)):
            inputs = list(inputs)
            for id, value in enumerate(inputs):
                inputs[id] = _cast(value)
            inputs = tuple(inputs)
        return inputs

    inputs = _cast(inputs)
    return inputs


def cast_to_adapter_tensor(outputs):
    """
    Cast MindSpore.Tensor to MSAdapter.Tensor after call mindspore API.
    """
    def _cast(outputs):
        if isinstance(outputs, (ms.Tensor, Tensor_)):
            outputs = inner.convert_to_adapter_tensor(outputs)
        elif isinstance(outputs, (tuple, list)):
            outputs = list(outputs)
            for id, value in enumerate(outputs):
                outputs[id] = _cast(value)
            outputs = tuple(outputs)
        return outputs

    outputs = _cast(outputs)
    return outputs


def _tensor_inplace_assign(input, output, op_name, replace_op):
    # if pynative_mode_condition():  # TODO: ms_function
    #     input.assign_value(output)
    #     return input

    # raise RuntimeError('`Tensor.{a}` is an in-place operation and "x.{a}()" is not encouraged to use '
    #                    'in MindSpore static graph mode. Please use "x = x.{b}()" or other API '
    #                    'instead.'.format(a=op_name, b=replace_op))

    # TODO: tensor api will be used in init data, but it can not be used in graph.
    unsupported_attr(op_name)
    unsupported_attr(replace_op)
    input.assign_value(output)
    return input


def _div_calcu(input, other, rounding_mode):
    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    if rounding_mode is None:
        if input.dtype == mstype.int64 or input.dtype == mstype.int32:
            input = ms.ops.cast(input, mstype.float32)
        output = ms.ops.div(input, other)

    if rounding_mode == "trunc":
        output = ms.ops.div(input, other)
        if input.dtype == ms.int64:
            dtype_ = output.dtype
            output = ms.numpy.trunc(output, dtype=dtype_)
        else:
            output = ms.ops.trunc(output)

    if rounding_mode == "floor":
        input_dtype = input.dtype
        output = ms.ops.floor_div(input, other)
        output = ms.ops.cast(output, input_dtype)
    return output
