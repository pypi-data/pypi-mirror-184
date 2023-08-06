#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
import warnings
import numpy as np
from scipy import signal
import mindspore as ms
from mindspore import ops
from mindspore.common import dtype as mstype
from mindspore.ops import constexpr
from mindspore.common.seed import _get_graph_seed
from mindspore.ops._primitive_cache import _get_cache_prim

from ms_adapter.pytorch.tensor import tensor, cast_to_ms_tensor, cast_to_adapter_tensor, _div_calcu
from ms_adapter.utils import unsupported_attr, get_backend, pynative_mode_condition, is_under_gpu_context, \
                             is_under_ascend_context, _ascend_tensor_general_cast, _infer_size
from ms_adapter.pytorch.tensor import Tensor as adapter_tensor
from ms_adapter.pytorch.common._inner import _out_inplace_assign, _out_limit_pynative
from ms_adapter.pytorch.common.dtype import _TypeDict, all_int_type
from ms_adapter.pytorch.common.device import Device


def empty(*size, out=None, dtype=None, layout=None, \
          device=None, requires_grad=False, pin_memory=False, \
          memory_format=None):
    unsupported_attr(layout)
    unsupported_attr(device)
    unsupported_attr(requires_grad)
    unsupported_attr(pin_memory)
    unsupported_attr(memory_format)
    if dtype is None:
        dtype = ms.float32

    _size = size
    if isinstance(size[0], (tuple, list)):
        _size = size[0]
    output = ms.numpy.empty(_size, dtype)
    return _out_inplace_assign(out, output, "empty")


def eye(n, m=None, *, out=None, dtype=None, layout=None, \
        device=None, requires_grad=False):
    unsupported_attr(layout)
    unsupported_attr(device)
    unsupported_attr(requires_grad)

    if m is None:
        m = n
    if dtype is None:
        dtype = ms.float32

    output = ms.ops.eye(n, m, dtype)
    return _out_inplace_assign(out, output, "eye")


def cat(tensors, dim=0, *, out=None):
    if tensors is None:
        raise ValueError('`tensors` in `{}` should not be None'.format(cat.__name__))

    if not isinstance(tensors, (tuple, list)):
        raise TypeError('`tensors` in `{}` should be tuple or list'.format(cat.__name__))

    if is_under_ascend_context():
        _rank = len(tensors[0].shape)
        dim = dim if dim >= 0 else dim + _rank

    inputs = cast_to_ms_tensor(tensors)
    output = ops.concat(inputs, dim)
    return _out_inplace_assign(out, output, "cat")

def concat(tensors, dim=0, *, out=None):
    if tensors is None:
        raise ValueError('`tensors` in `{}` should not be None'.format(concat.__name__))

    if not isinstance(tensors, (tuple, list)):
        raise TypeError('`tensors` in `{}` should be tuple or list'.format(concat.__name__))

    if is_under_ascend_context():
        _rank = len(tensors[0].shape)
        dim = dim if dim >= 0 else dim + _rank

    inputs = cast_to_ms_tensor(tensors)
    output = ops.concat(inputs, dim)
    return _out_inplace_assign(out, output, "concat")

def ones(*size, out=None, dtype=None, layout=None,
        device=None, requires_grad=False):
    unsupported_attr(layout)
    unsupported_attr(device)
    unsupported_attr(requires_grad)

    if dtype is None:
        dtype = ms.float32

    if isinstance(size[0], (tuple, list)):
        output = ms.ops.ones(*size, dtype=dtype)
    else:
        output = ms.ops.ones(size, dtype=dtype)
    return _out_inplace_assign(out, output, "ones")


def stack(tensors, dim = 0, *, out=None):
    tensors = cast_to_ms_tensor(tensors)
    output = ops.stack(tensors, dim)
    return _out_inplace_assign(out, output, "stack")


def meshgrid(*tensors, indexing='ij'):
    if isinstance(tensors[0], (list, tuple)):
        input_tensor = tuple(*tensors)
    else:
        input_tensor = tensors

    input_tensor = cast_to_ms_tensor(input_tensor)
    output = ops.meshgrid(input_tensor, indexing=indexing)
    return cast_to_adapter_tensor(output)


def log(input, *, out=None):
    input = cast_to_ms_tensor(input)
    output = ops.log(input)
    return _out_inplace_assign(out, output, "log")


def chunk(input, chunks, dim=0):
    input = cast_to_ms_tensor(input)
    output = ops.chunk(input, chunks, dim)
    return cast_to_adapter_tensor(output)


def diag(input, diagonal=0, *, out=None):
    # TODO
    # May be use mindspore.ops.diag instead. Nowadays, this operator do not support CPU.
    input = cast_to_ms_tensor(input)
    output =  ms.numpy.diag(input, diagonal)
    return _out_inplace_assign(out, output, "diag")


def sqrt(input, *, out=None):
    if input.dtype == mstype.int32 or input.dtype == mstype.int64:
        input = input.astype(mstype.float32)

    input = cast_to_ms_tensor(input)
    output = ops.sqrt(input)
    return _out_inplace_assign(out, output, "sqrt")


def mm(input, mat2, *, out=None):
    output_type = input.dtype
    if input.dtype == mstype.int32 or input.dtype == mstype.int64:
        input = input.astype(mstype.float32)

    input1 = cast_to_ms_tensor(input)
    input2 = cast_to_ms_tensor(mat2)
    output = ops.matmul(input1, input2)
    output = ops.cast(output, output_type)
    return _out_inplace_assign(out, output, "mm")


def zeros(*size, out=None, dtype=None, device=None, requires_grad=False):
    unsupported_attr(device)
    unsupported_attr(requires_grad)

    if isinstance(size[0], (tuple, list)):
        size = tuple(size[0])

    if dtype is None:
        dtype = mstype.float32

    output = ms.ops.zeros(size, dtype)
    return _out_inplace_assign(out, output, "zeros")


def div(input, other, *, rounding_mode=None, out=None):
    output = _div_calcu(input, other, rounding_mode)
    return _out_inplace_assign(out, output, "div")


def divide(input, other, *, rounding_mode=None, out=None):
    output = _div_calcu(input, other, rounding_mode)
    return _out_inplace_assign(out, output, "divide")


def flatten(input, start_dim=0, end_dim=-1):
    @constexpr
    def get_dst_shape():
        input_shape = input.shape
        rank = len(input_shape)
        start = start_dim
        end = end_dim

        if start < 0:
            start += rank

        if end < 0:
            end += rank

        dst_shape = []
        i = 0
        while i != start:
            dst_shape.append(input_shape[i])
            i = i + 1

        flatten_shape = 1
        while i <= end:
            flatten_shape = flatten_shape * input_shape[i]
            i = i + 1
        dst_shape.append(flatten_shape)

        while i < rank:
            dst_shape.append(input_shape[i])
            i = i + 1

        return tuple(dst_shape)

    shape = get_dst_shape()

    input = cast_to_ms_tensor(input)
    output = ops.reshape(input, shape)
    return cast_to_adapter_tensor(output)


def unflatten(input, dim, sizes):
    @constexpr
    def get_unflatten_size():
        input_shape = input.shape
        input_rank = len(input_shape)
        if not isinstance(sizes, (tuple, list)):
            raise TypeError(f"Type of `sizes` should be `Tuple` or `List`, but got {type(sizes)}")

        if len(sizes) == 0:
            raise ValueError("`sizes` must be non-empty")

        if isinstance(dim, str):
            raise TypeError("Until Now, `dim` not support type of str in `unflatten`")

        _dim = dim
        if _dim < 0:
            _dim += input_rank

        if _dim < 0 or _dim >= input_rank:
            raise ValueError("`dim` should be in range [{}, {}), but got {}".format(
                -input_rank, input_rank, dim))

        input_shape_list = list(input_shape)
        sizes_list = list(sizes)
        _sizes_mul = 1
        for s in sizes_list:
            _sizes_mul *= s
        if _sizes_mul != input_shape_list[_dim]:
            raise ValueError(f"unflatten: Provided `sizes` {sizes_list} don't multiply up to the"
                f"size of dim {dim} ({input_shape_list[_dim]}) in the input tensor")

        out_shape = input_shape[:_dim] + tuple(sizes) + input_shape[_dim + 1:]
        return out_shape

    out_shape = get_unflatten_size()
    input = cast_to_ms_tensor(input)
    out = ms.ops.reshape(input, out_shape)
    return cast_to_adapter_tensor(out)


def transpose(input, dim0, dim1):
    @constexpr
    def _check_dim(dim, rank):
        if dim >= rank or dim < -rank:
            raise ValueError("dim is out of bound, should be in range [{}, {})"
                    .format(-rank, rank))

    @constexpr
    def _get_perm():
        rank = len(input.shape)
        _check_dim(dim0, rank)
        _check_dim(dim1, rank)
        _perm = list(range(rank))
        _perm[dim0] = dim1
        _perm[dim1] = dim0
        return tuple(_perm)

    @constexpr
    def _get_perm_ascend():
        rank = len(input.shape)
        _check_dim(dim0, rank)
        _check_dim(dim1, rank)
        _perm = list(range(rank))
        _dim0 = dim0 if dim0 >=0 else dim0 + rank
        _dim1 = dim1 if dim1 >=0 else dim1 + rank
        _perm[_dim0] = _dim1
        _perm[_dim1] = _dim0
        return tuple(_perm)

    if is_under_ascend_context():
        input_ms = cast_to_ms_tensor(input)
        out = ms.ops.transpose(input_ms, _get_perm_ascend())
        return cast_to_adapter_tensor(out)

    input_ms = cast_to_ms_tensor(input)
    out = ops.transpose(input_ms, _get_perm())
    return cast_to_adapter_tensor(out)


def multinomial(input, num_samples, replacement=False, *, generator=None, out=None):
    unsupported_attr(generator)
    if generator is not None:
        warnings.warn("torch.multinomal don't support generator now.")
    input_tensor = cast_to_ms_tensor(input).astype(mstype.float32)

    # TODO: Ascend to support 1-dimention input
    if is_under_ascend_context():
        _input_rank = len(input.shape)
        if _input_rank == 1:
            input_tensor = input_tensor.expand_dims(axis=0)
        if not replacement:
            output = ms.ops.multinomial(input_tensor, num_samples, replacement)
        else:
            # TODO: Multinomial not support on Ascend
            seed0, seed1 = _get_graph_seed(None, "multinomial")
            _op = ms.ops.Multinomial(seed0, seed1)
            _op.set_device("CPU")
            output = _op(input_tensor, num_samples)
        if _input_rank == 1:
            output = output[0]
        return _out_inplace_assign(out, output, "multinomial")

    output = ms.ops.multinomial(input_tensor, num_samples, replacement)
    return _out_inplace_assign(out, output, "multinomial")


def randperm(n, *, generator=None, out=None, dtype=mstype.int64, layout=None, device=None,
             requires_grad=False, pin_memory=False):
    unsupported_attr(generator)
    unsupported_attr(layout)
    unsupported_attr(device)
    unsupported_attr(requires_grad)
    unsupported_attr(pin_memory)

    if generator is not None:
        warnings.warn("torch.randperm don't support generator now.")
    if layout is not None:
        warnings.warn("torch.randperm don't support layout now.")

    output = np.random.permutation(n)
    output = tensor(output, dtype=dtype)
    return _out_inplace_assign(out, output, "randperm")


def randint(low, high, size, *, generator=None, out=None, dtype=None, layout=None,
            device=None, requires_grad=False):
    unsupported_attr(generator)
    unsupported_attr(layout)
    unsupported_attr(device)
    unsupported_attr(requires_grad)

    if generator is not None:
        warnings.warn("torch.randperm don't support generator now.")
    if layout is not None:
        warnings.warn("torch.randperm don't support layout now.")

    output = np.random.randint(low, high, size)
    output = tensor(output, dtype=dtype)
    return _out_inplace_assign(out, output, "randint")


def as_tensor(data, dtype=None, device=None):
    unsupported_attr(device)

    if isinstance(data, (tuple, list)):
        data = [i.data.item() if isinstance(i, adapter_tensor) else i for i in data ]

    output = ms.Tensor(data, dtype=dtype)
    return cast_to_adapter_tensor(output)


def zeros_like(input, dtype=None, layout=None, device=None, requires_grad=False, memory_format=None):
    unsupported_attr(layout)
    unsupported_attr(device)
    unsupported_attr(requires_grad)
    unsupported_attr(memory_format)
    input_x = cast_to_ms_tensor(input)
    # TODO: output = ms.ops.zeros_like(input_x, dtype=dtype)
    output = ms.ops.zeros_like(input_x)
    if dtype:
        output = output.astype(dtype)
    return cast_to_adapter_tensor(output)


def ones_like(input, dtype=None, layout=None, device=None, requires_grad=False, memory_format=None):
    unsupported_attr(layout)
    unsupported_attr(device)
    unsupported_attr(requires_grad)
    unsupported_attr(memory_format)
    input_x = ms.Tensor(input, dtype=dtype)
    output = ms.ops.ones_like(input_x)
    return cast_to_adapter_tensor(output)


def empty_like(input, dtype=None, layout=None, device=None, requires_grad=False, memory_format=None):
    unsupported_attr(layout)
    unsupported_attr(device)
    unsupported_attr(requires_grad)
    unsupported_attr(memory_format)
    if dtype is None:
        dtype = ms.float32
    #TODO:replace whith mindspore.ops.empty_like
    ouput = ms.numpy.empty_like(input, dtype=dtype)
    return cast_to_adapter_tensor(ouput)


def full(size, fill_value, out=None, dtype=None, layout=None, device=None, requires_grad=False):
    unsupported_attr(layout)
    unsupported_attr(device)
    unsupported_attr(requires_grad)
    #TODO:replace whith mindspore.ops.full
    output = ms.numpy.full(size, fill_value, dtype)
    return _out_inplace_assign(out, output, "full")


def full_like(input, fill_value, dtype=None, layout=None, device=None, requires_grad=False, memory_format=None):
    unsupported_attr(layout)
    unsupported_attr(device)
    unsupported_attr(requires_grad)
    unsupported_attr(memory_format)
    #TODO:replace whith mindspore.ops.full_like
    output = ms.numpy.full_like(input, fill_value=fill_value, dtype=dtype)
    return cast_to_adapter_tensor(output)


def where(condition, x=None, y=None):
    if x is None and y is None:
        return nonzero(condition, as_tuple=True)
    # TODO:replace whith mindspore.ops.where
    output = ms.numpy.where(condition, x, y)
    return cast_to_adapter_tensor(output)


def rand(*size, out=None, dtype=None, layout=None, device=None, requires_grad=False, pin_memory=False):
    unsupported_attr(layout)
    unsupported_attr(device)
    unsupported_attr(requires_grad)
    unsupported_attr(pin_memory)
    if dtype is None:
        dtype = ms.float32
    output = ms.numpy.rand(*size, dtype=dtype)
    return _out_inplace_assign(out, output, "rand")


def linspace(start, end, steps, out=None, dtype=None, device=None, requires_grad=False):
    unsupported_attr(device)
    unsupported_attr(requires_grad)
    if dtype is None:
        dtype = ms.float32
    start = ms.Tensor(start, dtype)
    end = ms.Tensor(end, dtype)
    output = ms.ops.linspace(start, end, steps)
    return _out_inplace_assign(out, output, "linspace")


def take(input, index):
    input = cast_to_ms_tensor(input)
    input = ms.numpy.array(input)
    index = ms.numpy.array(index)
    # TODO:replace whith mindspore.ops.take
    output = ms.numpy.take(input, index)
    return cast_to_adapter_tensor(output)


def abs(input, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.abs(input)
    return _out_inplace_assign(out, output, "abs")


def atan2(input, other, out=None):
    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    output = ms.ops.atan2(input, other)
    return _out_inplace_assign(out, output, "atan2")


def clamp(input, min=None, max=None, out=None):
    # TODO:replace whith mindspore.ops.clamp
    input_ms = cast_to_ms_tensor(input)
    type = input_ms.dtype
    if min is not None and max is not None and min > max:
        output = ms.ops.ones_like(input_ms).astype(type)*max
    else:
        if min is not None:
            min = ms.Tensor(min, type)
        if max is not None:
            max = ms.Tensor(max, type)
        output = ms.ops.clip_by_value(input_ms, min, max)
    return _out_inplace_assign(out, output, "clamp")


def cos(input, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.cos(input)
    return _out_inplace_assign(out, output, "cos")


@constexpr
def device(type=None, index=None):
    if type is not None:
        if isinstance(type, str):
            if ':' in type:
                if index is not None:
                    raise ValueError(f"`type` must not include an index because index was passed explicitly: {type}")
                _target, _id = type.split(':')
                _id = int(_id)
            else:
                _target = type
                _id = index
            return Device(_target, _id)

        if isinstance(type, int):
            return Device(get_backend(), type)

        if isinstance(type, Device):
            if index is not None:
                raise ValueError("torch.device(): When input is torch.device, `index` can not be set.")
            return Device(type.type, type.index)

        raise TypeError("torch.device(): `type` must be type of 'str' or 'torch.device'.")

    raise ValueError("torch.device(): `type` can not be None")


def fmod(input, other, out=None):
    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)

    #TODO: repalce with ms.ops.fmod
    output = input - ms.ops.div(input, other, rounding_mode="trunc") * other
    return _out_inplace_assign(out, output, "fmod")


def frac(input, out=None):
    #TODO outout = input - floor(abs(input)) * sing(input)
    input = cast_to_ms_tensor(input)
    input = ms.numpy.array(input)
    output = input - ms.numpy.floor(ms.numpy.abs(input)) * ms.numpy.sign(input)
    return _out_inplace_assign(out, output, "frac")


def log10(input, out=None):
    input = cast_to_ms_tensor(input)
    input = ms.numpy.array(input)
    output = ms.numpy.log10(input)
    return _out_inplace_assign(out, output, "log10")


def log1p(input, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.log1p(input)
    return _out_inplace_assign(out, output, "log1p")


def log2(input, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.log2(input)
    return _out_inplace_assign(out, output, "log2")


def sin(input, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.sin(input)
    return _out_inplace_assign(out, output, "sin")


def max(input, dim=None, keepdim=False, *, out=None):
    #TODO: not supprt GRAPH_MODE, not supper max(input, other)
    input = cast_to_ms_tensor(input)
    type = input.dtype
    input = input.astype(ms.float32)
    if dim is None:
        output = input.max(axis=dim, keepdims=keepdim).astype(type)
        if out is not None:
            ops.assign(out, output)
            return out
        return cast_to_adapter_tensor(output)
    output = list(ms.ops.max(input, axis=dim, keep_dims=keepdim))
    value = output[1].astype(type)
    indice = output[0]
    point = collections.namedtuple('max', 'values,indices')
    rlt = point(cast_to_adapter_tensor(value), cast_to_adapter_tensor(indice))
    if out is not None:
        if pynative_mode_condition():
            if len(out) != 2 or not isinstance(out[0], adapter_tensor) or not isinstance(out[1], adapter_tensor):
                raise TypeError("In ms_adapter.torch.max(), `out` should be tuple of Tensors.")
            out[0].assign_value(value)
            out[1].assign_value(indice)
            return out
        else:
            raise ValueError('In MindSpore static graph mode, `out` in `max` shoud be None, '
                             'please set out=None and use return value instead of `out`.')
    return rlt


def min(input, dim=None, keepdim=False, *, out=None):
    # TODO: Right Now, not support 'min(input, other, *, out=None)'
    input = cast_to_ms_tensor(input)
    if dim is None:
        return cast_to_adapter_tensor(input.min())

    indices, result = ms.ops.min(input, axis=dim, keep_dims=keepdim)
    if out is not None:
        if pynative_mode_condition():
            if len(out) != 2 or not isinstance(out[0], adapter_tensor) or not isinstance(out[1], adapter_tensor):
                raise TypeError("In ms_adapter.torch.min(), `out` should be tuple of Tensors.")
            out[0].assign_value(result)
            out[1].assign_value(indices)
            return out
        else:
            raise ValueError('In MindSpore static graph mode, `out` in `min` shoud be None, '
                             'please set out=None and use return value instead of `out`.')
    return cast_to_adapter_tensor(result), cast_to_adapter_tensor(indices)


def mean(input, dim=None, keepdim=False, *, dtype=None, out=None):
    # TODO: not supprt GRAPH_MODE
    input = cast_to_ms_tensor(input)
    if dtype is not None:
        input = input.astype(dtype)
    if dim is not None:
        output = ms.ops.mean(input, axis=dim, keep_dims=keepdim)
    else:
        output = ms.ops.mean(input, keep_dims=keepdim)
    return _out_inplace_assign(out, output, "mean")


def round(input, *, decimals=0, out=None):
    input = cast_to_ms_tensor(input)
    if decimals == 0:
        output = ms.ops.round(input)
    else:
        p = 10**decimals
        input = input*p
        output = ms.ops.round(input)/p
    return _out_inplace_assign(out, output, "round")


def floor(input, *, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.floor(input)
    return _out_inplace_assign(out, output, "floor")


def ceil(input, *, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.ceil(input)
    return _out_inplace_assign(out, output, "ceil")


def sign(input, *, out=None):
    input = cast_to_ms_tensor(input)
    output = _get_cache_prim(ms.ops.Sign)()(input)
    return _out_inplace_assign(out, output, "sign")


def pow(input, exponent, *, out=None):
    # TODO: not support input that is above 7-dimention on GPU and Ascend
    input = cast_to_ms_tensor(input)
    exponent = cast_to_ms_tensor(exponent)
    output = ms.ops.pow(input, exponent)
    return _out_inplace_assign(out, output, "pow")


def exp(input, *, out=None):
    input = cast_to_ms_tensor(input)
    shape = input.shape
    if len(shape) > 7:
        input = input.flatten()
    if input.dtype != ms.float64:
        input = input.astype(ms.float32)
    output = ms.ops.exp(input)
    if len(shape) > 7:
        output = output.reshape(shape)
    return _out_inplace_assign(out, output, "exp")


def ge(input, other, *, out=None):
    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    output = ms.ops.ge(input, other)
    return _out_inplace_assign(out, output, "ge")


def gt(input, other, *, out=None):
    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    output = ms.ops.gt(input, other)
    return _out_inplace_assign(out, output, "gt")


def le(input, other, *, out=None):
    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    output = ms.ops.le(input, other)
    return _out_inplace_assign(out, output, "le")


def lt(input, other, *, out=None):
    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    output = ms.ops.less(input, other)
    return _out_inplace_assign(out, output, "lt")


def sum(input, dim=None, keepdim=False, *, dtype=None, out=None):
    input = cast_to_ms_tensor(input)
    if dtype is not None:
        input = input.astype(dtype)
    elif input.dtype in (mstype.uint8, mstype.uint16, mstype.uint32,
                         mstype.int8, mstype.int16, mstype.int32):
        dtype = mstype.int64
        input = input.astype(dtype)
    output = input.sum(axis=dim, dtype=dtype, keepdims=keepdim)
    return _out_inplace_assign(out, output, "sum")


def median(input, dim=None, keepdim=False, *, out=None):
    def _process_out(value, indice):
        point = collections.namedtuple('median', 'values,indices')
        rlt = point(cast_to_adapter_tensor(value), cast_to_adapter_tensor(indice))
        if out is not None:
            if pynative_mode_condition():
                if len(out) != 2 or not isinstance(out[0], adapter_tensor) or not isinstance(out[1], adapter_tensor):
                    raise TypeError("In ms_adapter.torch.median(), `out` should be tuple of Tensors.")
                out[0].assign_value(value)
                out[1].assign_value(indice)
                return out
            else:
                raise ValueError('In MindSpore static graph mode, `out` in `median` shoud be None, '
                                 'please set out=None and use return value instead of `out`.')
        return rlt

    input = cast_to_ms_tensor(input)

    if is_under_ascend_context():
        input_dtype = input.dtype
        input = _ascend_tensor_general_cast(input)
        if dim is None:
            _avg = ms.ops.mean(input)
            _distance = ms.ops.abs(input - _avg)
            _min_indice = _distance.argmin()
            out = input.flatten()[_min_indice]
            out = out.astype(input_dtype)
            return cast_to_adapter_tensor(out)
        else:
            _avg = ms.ops.mean(input, axis=dim, keep_dims=True)
            _distance = ms.ops.abs(input - _avg)
            _min_indice, _ = ms.ops.min(_distance, axis=dim, keep_dims=True)
            _min = ms.ops.gather_d(input, dim, _min_indice)
            if not keepdim:
                _min = ms.ops.squeeze(_min, dim)
                _min_indice = ms.ops.squeeze(_min_indice, dim)
            _min = _min.astype(input_dtype)
            return _process_out(_min, _min_indice)

    if dim is None:
        output, _ = ms.ops.median(input, keepdims=keepdim)
        return cast_to_adapter_tensor(output)
    else:
        value, indices = ms.ops.median(input, axis=dim, keepdims=keepdim)
        return _process_out(value, indices)


def matmul(input, other, *, out=None):
    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    output = ms.ops.matmul(input, other)
    return _out_inplace_assign(out, output, "matmul")


def norm(input, p='fro', dim=None, keepdim=False, out=None, dtype=None):
    input = cast_to_ms_tensor(input)
    if dtype is None:
        dtype = ms.float32
    input = ms.numpy.array(input, dtype=dtype)
    output = ms.numpy.norm(input, ord=p, axis=dim, keepdims=keepdim)
    return _out_inplace_assign(out, output, "norm")


def stft(input, n_fft, hop_length=None, win_length=None, window=None, center=True,
         pad_mode='reflect', normalized=False, onesided=None, return_complex=None):
    unsupported_attr(normalized)
    unsupported_attr(onesided)
    unsupported_attr(return_complex)
    input = cast_to_ms_tensor(input)
    input = input.asnumpy()
    if pad_mode == 'reflect':
        pad_mode = 'even'
    if window is None:
        window = 'hann'
    if hop_length is None:
        hop_length = floor(n_fft / 4)
    if win_length is None:
        win_length = n_fft
    output = signal.stft(input, window=window, nperseg=win_length, noverlap=hop_length, padded=center,
                         boundary=pad_mode)
    return output


def istft():
    raise NotImplementedError


def bartlett_window(window_length, periodic=True, dtype=None, layout=None, device=None, requires_grad=False):
    unsupported_attr(layout)
    unsupported_attr(device)
    unsupported_attr(requires_grad)
    input = tensor(window_length)
    output = ms.ops.bartlett_window(input, periodic=periodic, dtype=dtype)
    return cast_to_adapter_tensor(output)


def hamming_window(window_length, periodic=True, alpha=0.54, beta=0.46, dtype=None,
                   layout=None, device=None, requires_grad=False):
    unsupported_attr(periodic)
    unsupported_attr(alpha)
    unsupported_attr(beta)
    unsupported_attr(dtype)
    unsupported_attr(layout)
    unsupported_attr(device)
    unsupported_attr(requires_grad)
    output = ms.numpy.hamming(window_length)
    return cast_to_adapter_tensor(output)


def hann_window(window_length, periodic=False, dtype=None, layout=None, device=None, requires_grad=False):
    unsupported_attr(periodic)
    unsupported_attr(dtype)
    unsupported_attr(layout)
    unsupported_attr(device)
    unsupported_attr(requires_grad)
    if periodic is True:
        raise NotImplementedError("periodic is not supported to True.")
    output = ms.numpy.hanning(window_length)
    return cast_to_adapter_tensor(output)


def cumsum(input, dim, dtype=None, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.cumsum(input, axis=dim, dtype=dtype)
    return _out_inplace_assign(out, output, "cumsum")


def einsum(equation, *operands):
    output = _get_cache_prim(ms.ops.Einsum)(equation=equation)(operands)
    return cast_to_adapter_tensor(output)


def histc(input, bins=100, min=0, max=0, out=None):
    input = cast_to_ms_tensor(input)
    nbins = bins
    hist = _get_cache_prim(ms.ops.HistogramFixedWidth)(nbins)
    rang_op = ms.Tensor([min, max], ms.float32)
    output = hist(input, rang_op)
    return _out_inplace_assign(out, output, "histc")


def triu(input, diagonal=0, out=None):
    input = cast_to_ms_tensor(input)
    input = ms.numpy.array(input)
    output = ms.numpy.triu(input, diagonal)
    output = cast_to_adapter_tensor(output)
    return _out_inplace_assign(out, output, "triu")

def unbind(input, dim=0):
    input = cast_to_ms_tensor(input)
    output = ms.ops.unbind(input, dim)
    return cast_to_adapter_tensor(output)


def unsqueeze(input, dim):
    input = cast_to_ms_tensor(input)
    output = ms.ops.unsqueeze(input, dim)
    return cast_to_adapter_tensor(output)

def reshape(input, shape):
    input = cast_to_ms_tensor(input)
    input_size = input.shape
    if input_size[0] == 0:  # only support first element is 0
        numel = ms.ops.size(input)
        shape = _infer_size(shape, numel)
        output = ms.ops.zeros(shape, input.dtype)
    else:
        shape = tuple(shape)
        output = ms.ops.reshape(input, shape)
    return cast_to_adapter_tensor(output)

def isfinite(input):
    input_ms = cast_to_ms_tensor(input)
    output = ms.ops.isfinite(input_ms)
    return cast_to_adapter_tensor(output)


def isnan(input):
    input_ms = cast_to_ms_tensor(input)
    return cast_to_adapter_tensor(input_ms.isnan())


def view_as_real(input):
    #Todo: not view
    warnings.warn("not support output as a view.")
    input = cast_to_ms_tensor(input)
    input = input.asnumpy()
    real = np.expand_dims(np.real(input), axis=-1)
    imag = np.expand_dims(np.imag(input), axis=-1)
    output_np = np.concatenate((real, imag), axis=-1)
    output = ms.Tensor(output_np)
    return cast_to_adapter_tensor(output)


def bincount(input, weights=None, minlength=0):
    input = cast_to_ms_tensor(input)
    type = 'int64'
    if input.dtype == ms.uint8:
        input = input.astype(ms.int16)
    if weights is not None:
        weights = cast_to_ms_tensor(weights)
        type = weights.dtype
    output = ms.numpy.bincount(input, weights, minlength).astype(type)
    return cast_to_adapter_tensor(output)

def mul(input, other, *, out=None):
    if not isinstance(input, (int, adapter_tensor)):
        raise TypeError(f"mul(): argument 'input' (position 1) must be Tensor, not {type(input)}")
    if not isinstance(other, (int, adapter_tensor)):
        raise TypeError(f"mul(): argument 'other' (position 2) must be Tensor, not {type(other)}")

    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    output = ms.ops.mul(input, other)
    return _out_inplace_assign(out, output, "mul")


def index_select(input, dim, index, *, out=None):
    _input_params = cast_to_ms_tensor(input)
    _axis = dim
    _input_indices = cast_to_ms_tensor(index)

    output = ms.ops.gather(_input_params, _input_indices, _axis)
    return _out_inplace_assign(out, output, "index_select")

def sort(input, dim=-1, descending=False, stable=False, *, out=None):
    unsupported_attr(stable)
    input = cast_to_ms_tensor(input)
    # TODO: ops.sort() should be replaced.
    output = ms.ops.Sort(dim, descending)(input)
    return _out_inplace_assign(out, output, "sort")


def msort(input, *, out=None):
    input = cast_to_ms_tensor(input)
    # TODO: ops.sort() should be replaced.
    output, _  = _get_cache_prim(ms.ops.Sort)(axis=0)(input)
    return _out_inplace_assign(out, output, "msort")


def argsort(input, dim=-1, descending=False, stable=False):
    unsupported_attr(stable)
    input = cast_to_ms_tensor(input)
    # TODO: ops.sort() should be replaced.
    _, output= _get_cache_prim(ms.ops.Sort)(dim, descending)(input)
    return cast_to_adapter_tensor(output)

def t(input):
    input_ms = cast_to_ms_tensor(input)
    if input_ms.ndim > 2:
        raise ValueError("t() expects a tensor with <= 2 dimensions, but self is {}D".format(input_ms.ndim))
    dims = list(range(input_ms.ndim)).reverse()
    output = input_ms.transpose(dims)
    return cast_to_adapter_tensor(output)

def squeeze(input, dim=None):
    input_ms = cast_to_ms_tensor(input)
    if dim is not None:
        if input_ms.shape[dim] != 1:
            output = input
        else:
            output = ms.ops.squeeze(input_ms, dim)
    else:
        output = ms.ops.squeeze(input_ms)
    return cast_to_adapter_tensor(output)


def from_numpy(np_data):
    return cast_to_adapter_tensor(ms.Tensor.from_numpy(np_data))


def absolute(input, *, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.absolute(input)
    return _out_inplace_assign(out, output, "absolute")


def acos(input, *, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.acos(input)
    return _out_inplace_assign(out, output, "acos")


def arccos(input, *, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.acos(input)
    return _out_inplace_assign(out, output, "arccos")


def acosh(input, *, out=None):
    input = cast_to_ms_tensor(input)
    shape = input.shape
    if len(shape) > 7:
        input = input.flatten()
    output = ms.ops.acosh(input)
    if len(shape) > 7:
        output = output.reshape(shape)
    return _out_inplace_assign(out, output, "acosh")

def arccosh(input, *, out=None):
    input = cast_to_ms_tensor(input)
    shape = input.shape
    if len(shape) > 7:
        input = input.flatten()
    output = ms.ops.acosh(input)
    if len(shape) > 7:
        output = output.reshape(shape)
    return _out_inplace_assign(out, output, "arccosh")


def add(input, other, *, alpha=1, out=None):
    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    output = ms.ops.add(input, other*alpha)
    return _out_inplace_assign(out, output, "add")


def addcdiv(input, tensor1, tensor2, *, value=1, out=None):
    input = cast_to_ms_tensor(input)
    tensor1 = cast_to_ms_tensor(tensor1)
    tensor2 = cast_to_ms_tensor(tensor2)
    value = ms.Tensor(value)
    output = ms.ops.addcdiv(input, tensor1, tensor2, value)
    return _out_inplace_assign(out, output, "addcdiv")


def addcmul(input, tensor1, tensor2, *, value=1, out=None):
    #Todo: use ms.ops.addcmul after it has been fixed
    input = cast_to_ms_tensor(input)
    tensor1 = cast_to_ms_tensor(tensor1)
    tensor2 = cast_to_ms_tensor(tensor2)
    value = ms.Tensor(value)
    mul = ms.ops.mul(tensor1, tensor2) * value
    output = ms.ops.add(input, mul)
    return _out_inplace_assign(out, output, "addcmul")


def angle(input, *, out=None):
    input = cast_to_ms_tensor(input)
    shape = input.shape
    if len(shape)>7:
        input = input.flatten()

    real = _get_cache_prim(ms.ops.Real)()(input)
    imag = _get_cache_prim(ms.ops.Imag)()(input)
    #Todo: ms.ops.copysign is not same as torch.copysign when input is -0.0,
    # replace to ms.ops.copysign after it has been fixed
    imag_np = imag.asnumpy()
    sign_imag_np = np.copysign(np.ones_like(imag_np), imag_np)
    sign_imag = ms.Tensor(sign_imag_np)

    denom = ms.ops.sqrt(ms.ops.square(real) + ms.ops.square(imag))
    div = ms.ops.div(real, denom)
    mask = ms.ops.equal(denom, ms.Tensor(0))
    mask_array = ms.ops.ones_like(denom)*sign_imag
    div = ms.ops.select(mask, mask_array, div)
    output = ms.ops.mul(ms.ops.acos(div), sign_imag)

    if len(shape)>7:
        output = output.reshape(shape)
    return _out_inplace_assign(out, output, "angle")


def asin(input, *, out=None):
    input = cast_to_ms_tensor(input)
    if input.dtype in all_int_type:
        input = input.astype(mstype.float32)
    output = ms.ops.asin(input)
    return _out_inplace_assign(out, output, "asin")


def arcsin(input, *, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.asin(input)
    return _out_inplace_assign(out, output, "arcsin")


def asinh(input, *, out=None):
    input = cast_to_ms_tensor(input)
    shape = input.shape
    if len(shape) > 7:
        input = input.flatten()
    output = ms.ops.asinh(input)
    if len(shape) > 7:
        output = output.reshape(shape)
    return _out_inplace_assign(out, output, "asinh")


def arcsinh(input, *, out=None):
    input = cast_to_ms_tensor(input)
    shape = input.shape
    if len(shape) > 7:
        input = input.flatten()
    output = ms.ops.asinh(input)
    if len(shape) > 7:
        output = output.reshape(shape)
    return _out_inplace_assign(out, output, "arcsinh")


def atan(input, *, out=None):
    shape = input.shape
    if len(shape) > 7:
        input = input.flatten()
    input = cast_to_ms_tensor(input)
    output = ms.ops.atan(input)
    if len(shape) > 7:
        output = output.reshape(shape)
    return _out_inplace_assign(out, output, "atan")


def arctan(input, *, out=None):
    shape = input.shape
    if len(shape) > 7:
        input = input.flatten()
    input = cast_to_ms_tensor(input)
    output = ms.ops.atan(input)
    if len(shape) > 7:
        output = output.reshape(shape)
    return _out_inplace_assign(out, output, "arctan")


def atanh(input, *, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.atanh(input)
    return _out_inplace_assign(out, output, "atanh")


def arctanh(input, *, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.atanh(input)
    return _out_inplace_assign(out, output, "arctanh")


def arctan2(input, other, *, out=None):
    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    output = ms.ops.atan2(input, other)
    return _out_inplace_assign(out, output, "arctan2")


def bitwise_not(input, *, out=None):
    input = cast_to_ms_tensor(input)
    type = input.dtype
    if str(type) != 'Bool':
        output = 0 - input - 1
    else:
        output = 1 - input
        output = output.astype(ms.bool_)
    return _out_inplace_assign(out, output, "bitwise_not")


def bitwise_and(input, other, *, out=None):
    if isinstance(input, adapter_tensor):
        input = cast_to_ms_tensor(input)
        input_is_bool = str(input.dtype) == 'Bool'
    else:
        input_is_bool = isinstance(input, bool)
    if isinstance(other, adapter_tensor):
        other = cast_to_ms_tensor(other)
        other_is_bool = str(other.dtype) == 'Bool'
    else:
        other_is_bool = isinstance(other, bool)
    if input_is_bool and other_is_bool:
        if isinstance(input, adapter_tensor):
            input = input.astype(ms.int8)
        else:
            other = other.astype(ms.int8)
    output = ms.ops.bitwise_and(input, other)
    if input_is_bool and other_is_bool:
        output = output.astype(ms.bool_)
    return _out_inplace_assign(out, output, "bitwise_and")


def bitwise_or(input, other, *, out=None):
    if isinstance(input, adapter_tensor):
        input = cast_to_ms_tensor(input)
        input_is_bool = str(input.dtype) == 'Bool'
    else:
        input_is_bool = isinstance(input, bool)
    if isinstance(other, adapter_tensor):
        other = cast_to_ms_tensor(other)
        other_is_bool = str(other.dtype) == 'Bool'
    else:
        other_is_bool = isinstance(other, bool)
    if input_is_bool and other_is_bool:
        if isinstance(input, adapter_tensor):
            input = input.astype(ms.int8)
        else:
            other = other.astype(ms.int8)
    output = ms.ops.bitwise_or(input, other)
    if input_is_bool and other_is_bool:
        output = output.astype(ms.bool_)
    return _out_inplace_assign(out, output, "bitwise_or")


def bitwise_xor(input, other, *, out=None):
    if isinstance(input, adapter_tensor):
        input = cast_to_ms_tensor(input)
        input_is_bool = str(input.dtype) == 'Bool'
    else:
        input_is_bool = isinstance(input, bool)
    if isinstance(other, adapter_tensor):
        other = cast_to_ms_tensor(other)
        other_is_bool = str(other.dtype) == 'Bool'
    else:
        other_is_bool = isinstance(other, bool)
    if input_is_bool and other_is_bool:
        if isinstance(input, adapter_tensor):
            input = input.astype(ms.int8)
        else:
            other = other.astype(ms.int8)
    output = ms.ops.bitwise_xor(input, other)
    if input_is_bool and other_is_bool:
        output = output.astype(ms.bool_)
    return _out_inplace_assign(out, output, "bitwise_xor")


def bitwise_left_shift(input, other, *, out=None):
    if isinstance(input, adapter_tensor):
        input = cast_to_ms_tensor(input).asnumpy()
    if isinstance(other, adapter_tensor):
        other = cast_to_ms_tensor(other).asnumpy()
    output = ms.Tensor(np.left_shift(input, other))
    return _out_inplace_assign(out, output, "bitwise_left_shift")


def bitwise_right_shift(input, other, *, out=None):
    if isinstance(input, adapter_tensor):
        input = cast_to_ms_tensor(input).asnumpy()
    if isinstance(other, adapter_tensor):
        other = cast_to_ms_tensor(other).asnumpy()
    output = ms.Tensor(np.right_shift(input, other))
    return _out_inplace_assign(out, output, "bitwise_right_shift")


def split(tensor, split_size_or_sections, dim=0):
    tensor = cast_to_ms_tensor(tensor)
    output = ms.ops.split(tensor, split_size_or_sections, dim)
    return cast_to_adapter_tensor(output)

def nonzero(input, *, out=None, as_tuple=False):
    input = cast_to_ms_tensor(input)
    if as_tuple:
        if input.ndim == 1:
            res = ms.ops.nonzero(input)
            output = (cast_to_adapter_tensor(res.flatten()), )
        elif input.ndim > 1:
            output = []
            res = ms.ops.nonzero(input)
            res = res.transpose(1,0)
            res = ms.ops.split(res, 1, axis=0)
            output = cast_to_adapter_tensor(res)
        elif input.ndim == 0:
            raise ValueError("Do not support input ndim == 0.")
    else:
        output = ms.ops.nonzero(input)
    return _out_inplace_assign(out, output, "nonzero")

def clip(input, min=None, max=None, *, out=None):
    input = cast_to_ms_tensor(input)
    output = input.clip(min, max)
    return _out_inplace_assign(out, output, "clip")


def conj_physical(input, *, out=None):
    input = cast_to_ms_tensor(input)
    # TODO:　use code below in the future mindspore on Ascend, because Ascend not support input as real number
    #if ms.ops.is_complex(input):
    #    output = ms.ops.conj(input)
    #else:
    #    output = input
    output = ms.ops.conj(input)
    return _out_inplace_assign(out, output, "conj_physical")

def copysign(input, other, *, out=None):
    input = cast_to_ms_tensor(input)
    input_type = input.dtype
    input = input.asnumpy()
    is_num = True
    if isinstance(other, adapter_tensor):
        is_num = False
        other = cast_to_ms_tensor(other)
        other_type = other.dtype
        other = other.asnumpy()
    output = ms.Tensor(np.copysign(input, other))

    if 'Int' in str(input_type):
        if is_num or 'Int' in str(other_type):
            output = output.astype(ms.float32)
        else:
            output = output.astype(other_type)
    elif is_num or 'Int' in str(other_type):
        output = output.astype(input_type)
    return _out_inplace_assign(out, output, "copysign")


def cosh(input, *, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.cosh(input)
    return _out_inplace_assign(out, output, "cosh")


def deg2rad(input, *, out=None):
    input = cast_to_ms_tensor(input)
    if input.dtype not in (ms.float16, ms.float32, ms.float64):
        input = input.astype(ms.float32)
    output = ms.ops.deg2rad(input)
    return _out_inplace_assign(out, output, "cosh")


def devide(input, other, *, rounding_mode=None, out=None):
    _out_limit_pynative(out, "devide")
    return div(input, other, rounding_mode=rounding_mode, out=out)

#Todo: not found class Digamma
#def digamma(input, *, out=None):


def erf(input, *, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.erf(input)
    return _out_inplace_assign(out, output, "erf")


def erfc(input, *, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.erfc(input)
    return _out_inplace_assign(out, output, "erfc")


def erfinv(input, *, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.erfinv(input)
    return _out_inplace_assign(out, output, "erfinv")


def exp2(input, *, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.exp2(input)
    return _out_inplace_assign(out, output, "exp2")


def expm1(input, *, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.expm1(input)
    return _out_inplace_assign(out, output, "expm1")


def fake_quantize_per_channel_affine(input, scale, zero_point, axis, quant_min, quant_max):
    input = cast_to_ms_tensor(input)
    scale = cast_to_ms_tensor(scale)
    zero_point = cast_to_ms_tensor(zero_point)
    if axis not in range(0, input.ndim):
        raise IndexError("`axis` must be between 0 and number of dimensions of input")
    if input.shape[axis] != scale.shape[0] or input.shape[axis] != zero_point.shape[0]:
        raise RuntimeError("dimensions of scale or zero-point are not consistent with input tensor")
    i = axis + 1
    while i < input.ndim:
        scale = scale.expand_dims(-1)
        zero_point = zero_point.expand_dims(-1)
        i += 1
    output = ms.ops.round(input/scale + zero_point)
    output = ms.ops.clip_by_value(output, quant_min, quant_max) - zero_point
    output = output * scale
    return cast_to_adapter_tensor(output)


def fake_quantize_per_tensor_affine(input, scale, zero_point, quant_min, quant_max):
    input = cast_to_ms_tensor(input)
    scale = cast_to_ms_tensor(scale)
    zero_point = cast_to_ms_tensor(zero_point)

    output = ms.ops.round(input/scale + zero_point)
    output = ms.ops.clip_by_value(output, quant_min, quant_max) - zero_point
    output = output * scale
    return cast_to_adapter_tensor(output)


def fix(input, *, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.trunc(input)
    return _out_inplace_assign(out, output, "fix")


def float_power(input, exponent, *, out=None):
    if isinstance(input, adapter_tensor):
        input = cast_to_ms_tensor(input).asnumpy()
    if isinstance(exponent, adapter_tensor):
        exponent = cast_to_ms_tensor(exponent).asnumpy()
    output = ms.Tensor(np.float_power(input, exponent))
    return _out_inplace_assign(out, output, "float_power")


def floor_divide(input, other, *, out=None):
    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    output = ms.ops.floor_div(input, other)
    return _out_inplace_assign(out, output, "floor_divide")


def frexp(input, *, out=None):
    _out_limit_pynative(out, "frexp")
    input = cast_to_ms_tensor(input).asnumpy()
    mantissa, exponent = np.frexp(input)
    out1 = ms.Tensor(mantissa)
    out2 = ms.Tensor(exponent)
    if out is not None and len(out) != 2:
        out[0].assign_value(out1)
        out[1].assign_value(out2)
        return out
    return cast_to_adapter_tensor(out1), cast_to_adapter_tensor(out2)


def gradient(input, *, spacing=1, dim=None, edge_order=1):
    input = cast_to_ms_tensor(input)
    if isinstance(spacing, adapter_tensor):
        spacing = cast_to_ms_tensor(spacing)
    elif isinstance(spacing, tuple) and isinstance(spacing[0], adapter_tensor):
        spacing = cast_to_ms_tensor(spacing)
    output = ms.numpy.gradient(input, spacing, axis=dim, edge_order=edge_order)
    output = cast_to_adapter_tensor(output)
    if not isinstance(output, tuple):
        return (output,)
    else:
        return output


def imag(input):
    input = cast_to_ms_tensor(input)
    output = ms.ops.imag(input)
    return cast_to_adapter_tensor(output)


def ldexp(input, other, *, out=None):
    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    output = ms.ops.ldexp(input, other)
    return _out_inplace_assign(out, output, "ldexp")


def lerp(input, end, weight, *, out=None):
    input = cast_to_ms_tensor(input)
    end = cast_to_ms_tensor(end)
    if isinstance(weight, adapter_tensor):
        weight = cast_to_ms_tensor(weight)
    elif not isinstance(weight, float):
        weight = float(weight)
    output = ms.ops.lerp(input, end, weight)
    return _out_inplace_assign(out, output, "lerp")


#Todo
#def lgamma(input, *, out=None):


def logaddexp(input, other, *, out=None):
    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    output = ms.ops.logaddexp(input, other)
    return _out_inplace_assign(out, output, "logaddexp")


def logaddexp2(input, other, *, out=None):
    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    output = ms.ops.logaddexp2(input, other)
    return _out_inplace_assign(out, output, "logaddexp2")


def logical_and(input, other, *, out=None):
    if isinstance(input, adapter_tensor):
        input = cast_to_ms_tensor(input).astype(ms.bool_)
    if isinstance(other, adapter_tensor):
        other = cast_to_ms_tensor(other).astype(ms.bool_)
    output = ms.ops.logical_and(input, other)
    return _out_inplace_assign(out, output, "logical_and")


def logical_not(input, *, out=None):
    if isinstance(input, adapter_tensor):
        input = cast_to_ms_tensor(input).astype(ms.bool_)
    output = ms.ops.logical_not(input)
    return _out_inplace_assign(out, output, "logical_not")


def logical_or(input, other, *, out=None):
    if isinstance(input, adapter_tensor):
        input = cast_to_ms_tensor(input).astype(ms.bool_)
    if isinstance(other, adapter_tensor):
        other = cast_to_ms_tensor(other).astype(ms.bool_)
    output = ms.ops.logical_or(input, other)
    return _out_inplace_assign(out, output, "logical_or")


def logical_xor(input, other, *, out=None):
    if isinstance(input, adapter_tensor):
        input = cast_to_ms_tensor(input).astype(ms.bool_)
    if isinstance(other, adapter_tensor):
        other = cast_to_ms_tensor(other).astype(ms.bool_)

    # TODO: ms.ops.logical_xor to supported GPU and Ascend
    if is_under_ascend_context() or is_under_gpu_context():
        output = ms.numpy.logical_xor(input, other)
    else:
        output = ms.ops.logical_xor(input, other)
    return _out_inplace_assign(out, output, "logical_xor")


def logit(input, eps=None, *, out=None):
    #TODO: ops.logit not support cpu
    input = cast_to_ms_tensor(input)
    if eps is not None:
        input = ms.ops.clip_by_value(input, eps, 1.0-eps)
    output = ms.ops.log(input/(1.0-input))
    return _out_inplace_assign(out, output, "logit")

def frombuffer(buffer, *, dtype = None, count=- 1, offset=0, requires_grad=False):
    unsupported_attr(requires_grad)
    np_dtype = _TypeDict[dtype]
    output = np.frombuffer(buffer=buffer, dtype=np_dtype, count=count, offset=offset)
    return adapter_tensor(output, dtype=dtype)

def as_strided(input, size, stride, storage_offset=None):
    warnings.warn("not support output as a view.")
    input_ms = cast_to_ms_tensor(input)
    if len(size) != len(stride):
        raise RuntimeError("mismatch in length of strides and shape.")
    index = np.arange(0, size[0] * stride[0], stride[0])
    for i in range(1, len(size)):
        tmp = np.arange(0, size[i] * stride[i], stride[i])
        index = np.expand_dims(index, -1)
        index = index + tmp
    if storage_offset is not None:
        index = index + storage_offset
    input_indices = ms.Tensor(index)
    out = ms.ops.gather(input_ms.reshape(-1), input_indices, 0)
    return cast_to_adapter_tensor(out)

def ne(input, other, *, out=None):
    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    output = ms.ops.ne(input, other)
    return _out_inplace_assign(out, output, "ne")


def tanh(input, *, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.tanh(input)
    return _out_inplace_assign(out, output, "tanh")


def maximum(input, other, *, out=None):
    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    output = ms.ops.maximum(input, other)
    return _out_inplace_assign(out, output, "maximum")


def minimum(input, other, *, out=None):
    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    output = ms.ops.minimum(input, other)
    return _out_inplace_assign(out, output, "minimum")


def sigmoid(input, *, out=None):
    #TODO: ms.ops.sigmoid() not support float64
    input = cast_to_ms_tensor(input)
    # output = 1 / (ms.ops.exp(0 - input) + 1)
    sigmoid_op = _get_cache_prim(ms.ops.Sigmoid)()
    if input.dtype == ms.float64:
        input = input.astype(ms.float32)
        output = sigmoid_op(input)
        output = output.astype(ms.float64)
    else:
        output = sigmoid_op(input)
    return _out_inplace_assign(out, output, "sigmoid")


def softmax(input, dim, dtype=None, *, out=None):
    input = cast_to_ms_tensor(input)
    if dtype is not None:
        input = input.astype(dtype)
    output = ms.ops.softmax(input, dim)
    return _out_inplace_assign(out, output, "softmax")


def prod(input, dim=None, keepdim=False, *, dtype=None, out=None):
    input = cast_to_ms_tensor(input)
    if dtype is not None:
        input = input.astype(dtype)
    if dim is None:
        output = ms.ops.prod(input)
    else:
        output = ms.ops.prod(input, axis=dim, keep_dims=keepdim)
    return _out_inplace_assign(out, output, "prod")


def eq(input, other, *, out=None):
    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    output = ms.ops.equal(input, other)
    return _out_inplace_assign(out, output, "eq")


def hypot(input, other, *, out=None):
    #TODO: can't found ms.ops.hypot()
    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    output = ms.ops.sqrt(input.square() + other.square())
    #output = ms.ops.hypot(input, other)
    return _out_inplace_assign(out, output, "hypot")


def i0(input, *, out=None):
    input = cast_to_ms_tensor(input)
    float_type = [ms.float16, ms.half, ms.float32, ms.single, ms.float64, ms.double]
    if input.dtype not in float_type:
        input = input.astype(ms.float32)
    output = ms.ops.bessel_i0(input)
    return _out_inplace_assign(out, output, "i0")

def _set_type_gamma(input, other):
    float_type = [ms.float16, ms.half, ms.float32, ms.single, ms.float64, ms.double]
    is_float16 = False
    input_type_index = -1
    other_type_index = -1
    if input.dtype in float_type:
        input_type_index = float_type.index(input.dtype)
    if other.dtype in float_type:
        other_type_index = float_type.index(other.dtype)
    if input_type_index < other_type_index:
        input = input.astype(other.dtype)
    elif input_type_index > other_type_index:
        other = other.astype(input.dtype)
    if input.dtype == ms.float16:
        input = input.astype(ms.float32)
        other = other.astype(ms.float32)
        is_float16 = True
    return input, other, is_float16

def igamma(input, other, *, out=None):
    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    #TODO: delete here after ms.ops.igamma support those types as pytorch
    input, other, is_float16 = _set_type_gamma(input, other)
    output = ms.ops.igamma(input, other)
    if is_float16:
        output = output.astype(ms.float16)
    return _out_inplace_assign(out, output, "igamma")


def igammac(input, other, *, out=None):
    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    # TODO: delete here after ms.ops.igammac support those types as pytorch
    input, other, is_float16 = _set_type_gamma(input, other)
    output = ms.ops.igammac(input, other)
    if is_float16:
        output = output.astype(ms.float16)
    return _out_inplace_assign(out, output, "igammac")


def multiply(input, other, *, out=None):
    if not isinstance(input, (int, adapter_tensor)):
        raise TypeError(f"multiply(): argument 'input' (position 1) must be Tensor, not {type(input)}")
    if not isinstance(other, (int, adapter_tensor)):
        raise TypeError(f"multiply(): argument 'other' (position 2) must be Tensor, not {type(other)}")

    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    output = ms.ops.mul(input, other)
    return _out_inplace_assign(out, output, "multiply")


def mvlgamma(input, p, *, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.mvlgamma(input, p)
    return _out_inplace_assign(out, output, "mvlgamma")


def nan_to_num(input, nan=0.0, posinf=None, neginf=None, *, out=None):
    #TODO: not found mindspore.ops.nan_to_num
    input_np = input.asnumpy()
    output_np = np.nan_to_num(input_np, nan=nan, posinf=posinf, neginf=neginf)
    output = ms.Tensor(output_np)
    return _out_inplace_assign(out, output, "nan_to_num")


def neg(input, *, out=None):
    input = cast_to_ms_tensor(input)
    if 'Complex' in str(input.dtype):
        output = input-input-input
    else:
        output = 0 - input
    return _out_inplace_assign(out, output, "neg")


def negative(input, *, out=None):
    input = cast_to_ms_tensor(input)
    if 'Complex' in str(input.dtype):
        output = input-input-input
    else:
        output = 0 - input
    return _out_inplace_assign(out, output, "negative")


def nextafter(input, other, *, out=None):
    # TODO: not found mindspore.ops.nextafter
    input_np = input.asnumpy()
    other_np = other.asnumpy()
    output_np = np.nextafter(input_np, other_np)
    output = ms.Tensor(output_np)
    return _out_inplace_assign(out, output, "nextafter")


def positive(input):
    return input


def rad2deg(input, *, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.rad2deg(input)
    return _out_inplace_assign(out, output, "rad2deg")


def real(input):
    #TODO: replace tp ms.ops.real()
    input = cast_to_ms_tensor(input)
    output = _get_cache_prim(ms.ops.Real)()(input)
    return cast_to_adapter_tensor(output)


def reciprocal(input, *, out=None):
    #TODO: replace tp ms.ops.reciprocal()
    input = cast_to_ms_tensor(input)
    if 'Bool' in str(input.dtype) or 'Int' in str(input.dtype):
        input = input.astype(ms.float32)
    # TODO: future to support ms.ops.reciprocal
    output = ms.Tensor(1.0, dtype=input.dtype)/input
    return _out_inplace_assign(out, output, "reciprocal")


def remainder(input, other, *, out=None):
    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    output = ms.ops.remainder(input, other)
    return _out_inplace_assign(out, output, "remainder")


def rsqrt(input, *, out=None):
    input = cast_to_ms_tensor(input)
    if 'Bool' in str(input.dtype) or 'Int' in str(input.dtype):
        input = input.astype(ms.float32)
    output = _get_cache_prim(ms.ops.Rsqrt)()(input)
    return _out_inplace_assign(out, output, "rsqrt")


def sgn(input, *, out=None):
    input = cast_to_ms_tensor(input)
    sign_op = _get_cache_prim(ms.ops.Sign)()
    if 'Bool' in str(input.dtype) or 'Int' in str(input.dtype):
        type = input.dtype
        input = input.astype(ms.float32)
        output = sign_op(input).astype(type)
    else:
        output = sign_op(input)
    return _out_inplace_assign(out, output, "sgn")


def signbit(input, *, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.numpy.signbit(input)
    return _out_inplace_assign(out, output, "signbit")


def sinc(input, *, out=None):
    input = cast_to_ms_tensor(input)
    pi = 3.141592653589793
    div = ms.ops.sin(pi*input)/(pi*input)
    output = ms.numpy.where(input==0, 1.0, div)
    return _out_inplace_assign(out, output, "sinc")


def sinh(input, *, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.sinh(input)
    return _out_inplace_assign(out, output, "sinh")


def square(input, *, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.square(input)
    return _out_inplace_assign(out, output, "square")


def sub(input, other, *, alpha=1, out=None):
    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    output = ms.ops.sub(input, other * alpha)
    return _out_inplace_assign(out, output, "sub")


def subtract(input, other, *, alpha=1, out=None):
    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    output = ms.ops.sub(input, other * alpha)
    return _out_inplace_assign(out, output, "subtract")


def tan(input, *, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.tan(input)
    return _out_inplace_assign(out, output, "tan")


def _check_isint(input):
    if isinstance(input, int):
        return True
    if isinstance(input, (adapter_tensor, ms.Tensor)) and 'Int' in str(input.dtype):
        return True
    return False

def _int_to_float(input):
    if isinstance(input, int):
        return float(input)
    return input.astype(ms.float32)


def true_divide(dividend, divisor, *, out=None):
    input = cast_to_ms_tensor(dividend)
    other = cast_to_ms_tensor(divisor)

    is_input_int = _check_isint(input)
    is_other_int = _check_isint(other)

    if is_input_int and is_other_int:
        input = _int_to_float(input)
        other = _int_to_float(other)
    if isinstance(input, float) and isinstance(other, float):
        input = ms.Tensor(input)
    output = ms.ops.div(input, other, rounding_mode=None)
    return _out_inplace_assign(out, output, "true_divide")


def trunc(input, *, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.trunc(input)
    return _out_inplace_assign(out, output, "trunc")


def xlogy(input, other, *, out=None):
    if not isinstance(input, adapter_tensor) and not isinstance(other, adapter_tensor):
        raise TypeError("For xlogy: one of the input must be Tensor.")

    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    output = ms.ops.xlogy(input, other)
    return _out_inplace_assign(out, output, "xlogy")


def cov(input, *, correction=1, fweights=None, aweights=None, out=None):
    #TODO： need be replaced with mindspore.ops.cov
    input = cast_to_ms_tensor(input).float()
    if len(input.shape) > 2:
        raise ValueError("cov(): expected input to have two or fewer dimensions")
    if isinstance(input.dtype, ms.dtype.Bool):
        raise TypeError("cov(): bool dtype is not supported for input")
    if len(input.shape) < 2:
        input = ms.ops.reshape(input, (1, -1))
    observations_dim = 1
    num_observations = input.shape[observations_dim]
    # The product of frequencies (fweights) and weights (aweights).
    weights = None
    if fweights is not None:
        fweights = cast_to_ms_tensor(fweights)
        if len(fweights) <= 1:
            raise ValueError("cov(): expected fweights to have one or fewer dimensions")
        if not isinstance(fweights.dtype, ms.dtype.Int):
            raise TypeError("cov(): expected fweights to have integral dtype")
        if ms.ops.size(fweights) != num_observations:
            raise ValueError("cov(): expected fweights to have the same size as there are observations in the input")
        if num_observations != 0 and fweights.min() < 0:
            raise ValueError("cov(): fweights cannot be negative")
        weights = fweights
    if aweights is not None:
        aweights = cast_to_ms_tensor(aweights)
        if len(aweights) <= 1:
            raise ValueError("cov(): expected aweights to have one or fewer dimensions")
        if not isinstance(aweights.dtype, ms.dtype.Float):
            raise TypeError("cov(): expected aweights to have floating point dtype")
        if ms.ops.size(aweights) != num_observations:
            raise ValueError("cov(): expected aweights to have the same size as there are observations in the input")
        if num_observations != 0 and aweights.min() < 0:
            raise ValueError("cov(): aweights cannot be negative")
        if fweights is not None:
            weights = fweights * aweights
        else:
            weights = aweights
    # Compute a weighted average of the obervations
    if weights is not None:
        weights_sum = weights.sum()
        if weights_sum == 0:
            raise ValueError("cov(): weights sum to zero, can't be normalized")
        avg = (input * weights).sum(axis=observations_dim) / weights_sum
    else:
        weights_sum = ms.ops.scalar_to_tensor(num_observations, input.dtype)
        avg = input.sum(axis=observations_dim) / weights_sum
    # Compute the normalization factor
    if weights is not None and aweights is not None and correction != 0:
        norm_factor = weights_sum - correction * (weights * aweights).sum() / weights_sum
    else:
        norm_factor = weights_sum - correction
    # Compute covariance matrix
    input = input - avg[:, None]
    if weights is not None:
        input_T = (input * weights).T
    else:
        input_T = input.T
    # TODO: use code below in future mindspore version, because Ascend not support input as real number for ms.ops.conj
    # TODO: to support complex number in 'cov'
    # if ms.ops.is_complex(input_T):
    #    input_T = ms.ops.conj(input_T)
    output = ms.numpy.dot(input, input_T)
    output = ms.numpy.true_divide(output, norm_factor)
    return _out_inplace_assign(out, output.squeeze(), "cov")


def corrcoef(input, *, out=None):
    input = cast_to_ms_tensor(input)
    if len(input.shape) > 2:
        raise ValueError("corrcoef(): expected input to have two or fewer dimensions")
    output = cov(input)
    if len(output.shape) == 0:
        return output / output
    # normalize covariance
    d = ms.numpy.diag(output)
    # Clip real and imaginary parts to [-1, 1].
    if input.dtype == ms.complex64:
        real_op = _get_cache_prim(ms.ops.Real)()
        imag_op = _get_cache_prim(ms.ops.Imag)()
        complex_op = _get_cache_prim(ms.ops.Complex)()
        d_real = real_op(d)
        stddev = ms.ops.sqrt(d_real)
        output = output / stddev[:, None]
        output = output / stddev[None, :]
        output_real = real_op(output)
        output_imag = imag_op(output)
        output_real = ms.ops.clip_by_value(output_real, -1, 1)
        output_imag = ms.ops.clip_by_value(output_imag, -1, 1)
        output = complex_op(output_real, output_imag)
    else:
        stddev = ms.ops.sqrt(d)
        output = output / stddev[:, None]
        output = output / stddev[None, :]
        output = ms.ops.clip_by_value(output, -1, 1)
    return _out_inplace_assign(out, output, "corrcoef")


def cross(input, other, dim=None, *, out=None):
    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    if is_under_ascend_context() or is_under_gpu_context():
        if dim is None:
            dim = -65530
        _op = _get_cache_prim(ms.ops.Cross)(dim=dim)
        _op.set_device("CPU")
        output = _op(input, other)
    else:
        output = ms.ops.cross(input, other, dim)
    return _out_inplace_assign(out, output, "cross")


def cummax(input, dim, *, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.cummax(input, axis=dim)
    return _out_inplace_assign(out, output, "cummax")


def cummin(input, dim, *, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.cummin(input, dim)
    # the output dtype in ms.ops.cummin is different with ms.ops.cummax
    output[1] = output[1].astype(ms.common.dtype.int64)
    return _out_inplace_assign(out, output, "cummin")


def cumprod(input, dim, *, dtype=None, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.ops.cumprod(input, dim, dtype=dtype)
    return _out_inplace_assign(out, output, "cumprod")

def diagflat(input, offset=0, *, out=None):
    input = cast_to_ms_tensor(input)
    output = ms.numpy.diagflat(input, offset)
    return _out_inplace_assign(out, output, "diagflat")

def diagonal(input, offset=0, dim1=0, dim2=1):
    input = cast_to_ms_tensor(input)
    #TODO float64 not support if offset != 0
    if offset != 0:
        input = input.astype(mstype.float32)
    output = ms.ops.diagonal(input, offset, dim1, dim2)
    return cast_to_adapter_tensor(output)

def diff(input, n=1, dim=-1, prepend=None, append=None):
    input = cast_to_ms_tensor(input)
    output = ms.numpy.diff(input, n, dim, prepend, append)
    return cast_to_adapter_tensor(output)

def flip(input, dims):
    input = cast_to_ms_tensor(input)
    if isinstance(dims, list):
        dims = tuple(dims)
    output = ms.ops.flip(input, dims)
    return cast_to_adapter_tensor(output)

def fliplr(input):
    input = cast_to_ms_tensor(input)
    output = ms.ops.fliplr(input)
    return cast_to_adapter_tensor(output)


def gather(input, dim, index, *, sparse_grad=False, out=None):
    if sparse_grad:
        raise ValueError("`sparse_grad` in `sparse_grad` can not be True.")

    input = cast_to_ms_tensor(input)
    index = cast_to_ms_tensor(index)
    output = ms.ops.gather_elements(input, dim, index)
    return _out_inplace_assign(out, output, "gather")

def bmm(input, mat2, *, out=None) :
    input_x = cast_to_ms_tensor(input)
    mat2 = cast_to_ms_tensor(mat2)
    output = ms.ops.bmm(input_x, mat2)
    return _out_inplace_assign(out, output, "bmm")

def equal(input, other):
    if not isinstance(input, adapter_tensor) or not isinstance(other, adapter_tensor):
        raise ValueError("`input` and `other` must be Tensor")
    x = cast_to_ms_tensor(input)
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

def greater_equal(input, other, *, out=None):
    x = cast_to_ms_tensor(input)
    y = cast_to_ms_tensor(other)
    output = ms.ops.greater_equal(x, y)
    return _out_inplace_assign(out, output, "greater_equal")

def greater(input, other, *, out=None):
    x = cast_to_ms_tensor(input)
    y = cast_to_ms_tensor(other)
    output = ms.ops.greater(x, y)
    return _out_inplace_assign(out, output, "greater")

def less_equal(input, other, *, out=None):
    x = cast_to_ms_tensor(input)
    y = cast_to_ms_tensor(other)
    output = ms.ops.less_equal(x, y)
    return _out_inplace_assign(out, output, "less_equal")

def less(input, other, *, out=None):
    x = cast_to_ms_tensor(input)
    y = cast_to_ms_tensor(other)
    output = ms.ops.less(x, y)
    return _out_inplace_assign(out, output, "less")

def not_equal(input, other, *, out=None):
    input = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    output = ms.ops.ne(input, other)
    return _out_inplace_assign(out, output, "not_equal")

def baddbmm(input, batch1, batch2, *, beta=1, alpha=1, out=None):
    x = cast_to_ms_tensor(input)
    batch1 = cast_to_ms_tensor(batch1)
    batch2 = cast_to_ms_tensor(batch2)
    output = ms.ops.baddbmm(x, batch1, batch2, beta, alpha)
    return _out_inplace_assign(out, output, "baddbmm")

def masked_select(input, mask, *, out=None):
    x = cast_to_ms_tensor(input)
    mask = cast_to_ms_tensor(mask)
    output = ms.ops.masked_select(x, mask)
    return _out_inplace_assign(out, output, "masked_select")

def select(input, dim, index):
    input = cast_to_ms_tensor(input)
    _input_indices = ms.Tensor(index)
    output = ms.ops.gather(input, _input_indices, dim)

    @constexpr
    def _get_out_shape(input_shape, dim):
        shape = [input_shape[i] for i in range(len(input_shape)) if i != dim]
        return tuple(shape)

    output_shape = _get_out_shape(input.shape, dim)
    output = output.reshape(output_shape)
    return cast_to_adapter_tensor(output)

def argmin(input, dim=None, keepdim=False):
    input = cast_to_ms_tensor(input)
    # TODO: output = ms.ops.argmin(input, axis=dim, keepdims=keepdim)
    if keepdim:
        raise NotImplementedError("keepdim is not supported.")
    output = ms.ops.argmin(input, axis=dim)
    return cast_to_adapter_tensor(output)

def argmax(input, dim=None, keepdim=False):
    input = cast_to_ms_tensor(input)
    # TODO: output = ms.ops.argmax(input, axis=dim, keepdims=keepdim)
    if keepdim:
        raise NotImplementedError("keepdim is not supported.")
    output = ms.ops.argmax(input, axis=dim)
    return cast_to_adapter_tensor(output)

def broadcast_to(input, shape):
    input = cast_to_ms_tensor(input)
    output = ms.ops.broadcast_to(input, shape)
    return cast_to_adapter_tensor(output)

def ravel(input):
    x = cast_to_ms_tensor(input)
    output = ms.ops.reshape(x, (-1,))
    return cast_to_adapter_tensor(output)

def unique(input, sorted=True, return_inverse=False, return_counts=False, dim=None):
    unsupported_attr(dim)
    unsupported_attr(return_counts)
    input = cast_to_ms_tensor(input)
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

def permute(input, dims):
    ms_input = cast_to_ms_tensor(input)
    output = ms_input.transpose(dims)
    return cast_to_adapter_tensor(output)

def numel(input):
    input = cast_to_ms_tensor(input)
    return ms.ops.size(input)

def logsumexp(input, dim, keepdim=False, *, out=None):
    ms_input = cast_to_ms_tensor(input)
    if ms_input.dtype != mstype.float32:
        ms_input = ms_input.astype(mstype.float32)
    output = ms.ops.logsumexp(ms_input, dim, keepdim)
    return _out_inplace_assign(out, output, "logsumexp")

def addmv(input, mat, vec, *, beta=1, alpha=1, out=None):
    input = cast_to_ms_tensor(input)
    mat = cast_to_ms_tensor(mat)
    vec = cast_to_ms_tensor(vec)
    output = ms.ops.addmv(input, mat, vec, beta=beta, alpha=alpha)
    return _out_inplace_assign(out, output, "addmv")

def dot(input, other, *, out=None):
    input = cast_to_ms_tensor(input)
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
    return _out_inplace_assign(out, output, "dot")

def inverse(input, *, out=None):
    input = cast_to_ms_tensor(input)
    #TODO: Ascend has no ms.ops.inverse
    # output = ms.ops.inverse(input)  # ops.inverse is not ready at 11-13
    if input.dtype in all_int_type:
        input = input.astype(mstype.float32)
    output = _get_cache_prim(ms.ops.MatrixInverse)()(input)
    return _out_inplace_assign(out, output, "inverse")

def count_nonzero(input, dim=None):
    input = cast_to_ms_tensor(input)
    if dim is None:
        dim = ()
    output = ms.ops.count_nonzero(input, axis=dim)
    return cast_to_adapter_tensor(output)

def all(input, dim=(), keepdim=False, *, out=None):
    input = cast_to_ms_tensor(input)
    output = input.all(axis=dim, keep_dims=keepdim)
    return _out_inplace_assign(out, output, "all")

def scatter(input, dim, index, src):
    return input.scatter(dim, index, src)

def topk(input, k, dim=None, largest=True, sorted=True, *, out=None):
    unsupported_attr(dim)
    unsupported_attr(largest)
    input_x = cast_to_ms_tensor(input)
    output = ms.ops.top_k(input_x, k, sorted=sorted)
    return _out_inplace_assign(out, output, "topk")
