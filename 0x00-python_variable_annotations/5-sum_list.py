#!/usr/bin/env python3
"""
defines a type-annotated function `sum_list`
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    returns the sum of all elements in a list
    """
    return sum(input_list)
