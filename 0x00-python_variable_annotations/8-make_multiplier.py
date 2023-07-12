#!/usr/bin/env python3
"""
defines a type-annotated function `make_multiplier`
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function that multiplies a float by `multiplier`
    """
    def multiply(value: float) -> float:
        """
        returns product of value and multiplier
        """
        return value * multiplier

    return multiply
