#!/usr/bin/env python3
"""
defines a type-annotated function `sum_mixed_list`
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    takes list of integers and floats, sums the elements and
    returns sum as a float
    """
    return sum(mxd_lst)
