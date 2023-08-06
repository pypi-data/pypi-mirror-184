#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
import mindspore as ms
from ms_adapter.pytorch.tensor import cast_to_ms_tensor, cast_to_adapter_tensor

def fft(input, n=None, dim=-1, norm=None, out=None):
    input = cast_to_ms_tensor(input)
    input = input.asnumpy()
    output = np.fft.fft(input, n, axis=dim, norm=norm)
    output = cast_to_adapter_tensor(ms.Tensor(output))
    if out is not None:
        out.assign_value(output)
    return output
