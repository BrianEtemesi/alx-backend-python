#!/usr/bin/env python3
"""
defines a type-annotated function `sum_list`
"""


def sum_list(input_list: list[float]) -> float:
    """
    returns the sum of all elements in a list
    """
    return sum(input_list)
