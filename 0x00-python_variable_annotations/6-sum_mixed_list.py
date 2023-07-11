#!/usr/bi/env python3
"""
defines a type-annotated function `sum_mixed_list`
"""


def sum_mixed_list(mxd_lst: list[int | float]) -> float:
    """
    takes list of integers and floats, sums the elements and
    returns sum as a float
    """
    return sum(mxd_lst)
