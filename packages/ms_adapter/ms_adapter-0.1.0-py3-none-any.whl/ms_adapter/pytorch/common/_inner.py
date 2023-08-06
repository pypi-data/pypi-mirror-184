#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mindspore.ops import constexpr
from ms_adapter.pytorch.tensor import cast_to_adapter_tensor
from ms_adapter.utils import pynative_mode_condition, graph_mode_condition


def _out_limit_pynative(out, op_name):
    if out is not None and graph_mode_condition():  # TODO: ms_function
        raise ValueError('In MindSpore static graph mode, `out` in `{}` shoud be None, '
                         'please set out=None and use return value instead of `out`.'.format(op_name))


def _out_inplace_assign(out, output, op_name):
    if out is None:
        return cast_to_adapter_tensor(output)

    if pynative_mode_condition():  # TODO: ms_function
        out.assign_value(output)
        return out

    raise ValueError('In MindSpore static graph mode, `out` in `{}` shoud be None, '
                     'please set out=None and use return value instead of `out`.'.format(op_name))


def _inplace_assign_pynative(input, inplace, output, op_name):
    if inplace is True:
        if pynative_mode_condition():  # TODO: ms_function
            input.assign_value(output)
            return input

        raise ValueError('In MindSpore static graph mode, `inplace` in `{}` shoud not be Ture, '
                         'please set inplace=False and use return value instead of `input`.'.format(op_name))

    return cast_to_adapter_tensor(output)


@constexpr
def _inplace_limit_pynative(inplace, op_name):
    if inplace is True and graph_mode_condition(): # TODO: ms_function
        raise ValueError('In MindSpore static graph mode, `inplace` in `{}` shoud not be Ture, '
                         'please set inplace=False and use return value instead of `input`.'.format(op_name))

def _inplace_assign(input, inplace, output):
    if inplace is True:
        input.assign_value(output)
        return input
    return cast_to_adapter_tensor(output)
