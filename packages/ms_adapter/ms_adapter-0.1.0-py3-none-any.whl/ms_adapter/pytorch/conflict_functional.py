#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
from mindspore.common import dtype as mstype
from ms_adapter.utils import unsupported_attr
from ms_adapter.pytorch.common._inner import _out_inplace_assign


def range(start, end, step=1, out=None, dtype=None, layout=None, device=None, requires_grad=False):
    unsupported_attr(layout)
    unsupported_attr(device)
    unsupported_attr(requires_grad)
    if dtype is None:
        dtype = ms.float32
    start = ms.Tensor(start, dtype=dtype)
    end = ms.Tensor(end+0.001, dtype=dtype)
    # TODO This function is deprecated and will be removed in a future release
    # because its behavior is inconsistent with Python’s range builtin. Instead, use torch.arange(),
    # which produces values in [start, end).
    step = ms.Tensor(step, dtype=dtype)
    output = ms.ops.range(start, end, step)
    return _out_inplace_assign(out, output, "range")


def arange(start, end, step=1, *, out=None, dtype=None,
        layout=None, device=None, requires_grad=False):
    unsupported_attr(layout)
    unsupported_attr(device)
    unsupported_attr(requires_grad)

    # TODO: use code below in future version
    # output =  ms.ops.arange(start, end, step)
    # return _out_inplace_assign(out, output, "arange")
    if dtype is None:
        if isinstance(start, float) or isinstance(end, float) or isinstance(step, float):
            dtype = mstype.float32
        else:
            #TODO
            # For now, `range` do not support `mstype.int64`, it should be changed
            # to 'dtype = mstype.int64' in mindspore 2.0
            dtype = mstype.int32

    start = ms.Tensor(start, dtype)
    end = ms.Tensor(end, dtype)
    step = ms.Tensor(step, dtype)

    output =  ms.ops.range(start=start, limit=end, delta=step)
    return _out_inplace_assign(out, output, "arange")
