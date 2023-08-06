#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Register MSAdapter Tensor/Parameter to MindSpore, it should be executed at the top of all.
from ms_adapter.pytorch._register import *
from ms_adapter.pytorch.common import *
from ms_adapter.pytorch.tensor import *
from ms_adapter.pytorch import nn
from ms_adapter.pytorch import optim
from ms_adapter.pytorch.functional import *
from ms_adapter.pytorch.utils import data
from ms_adapter.pytorch._ref import *
from ms_adapter.pytorch import cuda
from ms_adapter.pytorch.conflict_functional import *
import ms_adapter.pytorch.fft as fft
from ms_adapter.pytorch import autograd
from ms_adapter.pytorch.package_info import __version__, VERSION, version
from ms_adapter.pytorch.random import *
from ms_adapter.pytorch.storage import *

# Variables with simple values, from math.py
e = 2.718281828459045

pi = 3.141592653589793

tau = 6.283185307179586

def _assert(condition, message):
    assert condition, message

def is_tensor(obj):
    r"""Returns True if `obj` is a ms_adapter.pytorch tensor.

    Note that this function is simply doing ``isinstance(obj, Tensor)``.
    Using that ``isinstance`` check is better for typechecking with mypy,
    and more explicit - so it's recommended to use that instead of
    ``is_tensor``.
    """
    return isinstance(obj, Tensor)

def is_floating_point(obj):
    # TODO: return mindspore.ops.is_floating_point(obj)
    if not is_tensor(obj):
        raise TypeError("is_floating_point(): argument 'input' (position 1) must be Tensor, not {}.".format(type(obj)))

    return obj._dtype in (mstype.float16, mstype.float32, mstype.float64)

class Size(tuple):
    def __new__(cls, shape):
        if isinstance(shape, Tensor):
            _shape = shape.tolist()
        else:
            _shape = shape
        if not isinstance(_shape, (tuple, list)):
            raise TypeError("{} object is not supportted.".format(type(shape)))

        return tuple.__new__(Size, _shape)
