#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mindspore.common.api import set_adapter_config
from mindspore._extends.parse import trope as T
from mindspore._extends.parse.resources import convert_object_map

from ms_adapter.pytorch.tensor import Tensor
from ms_adapter.pytorch.nn import Parameter
from ms_adapter.pytorch._register import register_multitype_ops
from ms_adapter.pytorch._register import register_standard_method as S


convert_object_map[T.add] = register_multitype_ops.add
convert_object_map[T.sub] = register_multitype_ops.sub
convert_object_map[T.mul] = register_multitype_ops.mul
convert_object_map[T.truediv] = register_multitype_ops.div
convert_object_map[T.getitem] = register_multitype_ops.getitem
convert_object_map[T.setitem] = register_multitype_ops.setitem
convert_object_map[T.floordiv] = register_multitype_ops.floordiv
convert_object_map[T.mod] = register_multitype_ops.mod
convert_object_map[T.pow] = register_multitype_ops.pow_
convert_object_map[T.and_] = register_multitype_ops.bitwise_and
convert_object_map[T.or_] = register_multitype_ops.bitwise_or
convert_object_map[T.xor] = register_multitype_ops.bitwise_xor
convert_object_map[T.neg] = register_multitype_ops.negative
convert_object_map[T.not_] = register_multitype_ops.logical_not
convert_object_map[T.eq] = register_multitype_ops.equal
convert_object_map[T.ne] = register_multitype_ops.not_equal
convert_object_map[T.lt] = register_multitype_ops.less
convert_object_map[T.gt] = register_multitype_ops.greater
convert_object_map[T.le] = register_multitype_ops.less_equal
convert_object_map[T.ge] = register_multitype_ops.greater_equal
convert_object_map[T.contains] = register_multitype_ops.in_
convert_object_map[T.not_contains] = register_multitype_ops.not_in_
convert_object_map[T.matmul] = S.adapter_matmul
convert_object_map[T.invert] = S.adapter_invert
convert_object_map[T.abs] = S.adapter_abs
convert_object_map[T.round] = S.adapter_round
convert_object_map[T.max] = S.adapter_max
convert_object_map[T.min] = S.adapter_min
convert_object_map[T.sum] = S.adapter_sum


def register_msadapter_tensor():
    adapter_config = {"Tensor": Tensor, "convert_object_map": convert_object_map}
    set_adapter_config(adapter_config)

register_msadapter_tensor()
