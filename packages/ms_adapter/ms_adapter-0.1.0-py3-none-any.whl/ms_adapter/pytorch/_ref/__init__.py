#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mindspore as ms
from ms_adapter.utils import unsupported_attr
from ms_adapter.pytorch.tensor import Tensor, cast_to_adapter_tensor

def randn(*size, out=None, dtype=None, layout=None,
    device=None, requires_grad=False):
    unsupported_attr(layout)
    unsupported_attr(device)
    unsupported_attr(requires_grad)

    if isinstance(size[0], (tuple, list)):
        _size = size[0]
    elif isinstance(size[0], int):
        _size = size
    else:
        raise TypeError("`size` type in `randn` only support int, tuple and list")

    if dtype is None:
        dtype = ms.float32

    out_value = ms.numpy.randn(_size, dtype=dtype)

    if out is not None:
        ms.ops.assign(out, out_value)
        return out
    return cast_to_adapter_tensor(out_value)

def typename(o):
    if isinstance(o, Tensor):
        return o.type()

    module = ''
    class_name = ''
    if hasattr(o, '__module__') and o.__module__ != 'builtins' \
            and o.__module__ != '__builtin__' and o.__module__ is not None:
        module = o.__module__ + '.'

    if hasattr(o, '__qualname__'):
        class_name = o.__qualname__
    elif hasattr(o, '__name__'):
        class_name = o.__name__
    else:
        class_name = o.__class__.__name__

    return module + class_name
