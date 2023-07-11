#!/usr/bin/python3
"""
defines a type-annotated function `to_kv`
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    returns string and square of v
    """
    return (k, v ** 2)
