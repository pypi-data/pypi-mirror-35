# -*- coding: utf-8 -*-

from marshmallow.validate import (
    URL, Email, Range, Length, Equal, Regexp,
    Predicate, NoneOf, OneOf, ContainsOnly
)


class OneOfValid(OneOf):
    """
    单选中校验只能是备选项中的一个
    """

    def __init__(self, param_str):
        param_arr = param_str.split('|')
        super(OneOfValid, self).__init__(param_arr)
