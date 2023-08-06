# -*- coding: utf-8 -*-

from marshmallow.validate import (
    URL, Email, Range, Length, Equal, Regexp,
    Predicate, NoneOf, OneOf, ContainsOnly
)
from ..validator import debug, info, warn, error


class LengthValid(Length):
    def __init__(self, param_str):
        if '-' in param_str:
            param_arr = param_str.split('-')
            min_v = param_arr[0]
            max_v = param_arr[1]
            super(LengthValid, self).__init__(int(min_v), int(max_v))
        else:
            error("range的输入需要用-号隔开:{}".format(param_str))
            super(LengthValid, self).__init__(0, 65535)
