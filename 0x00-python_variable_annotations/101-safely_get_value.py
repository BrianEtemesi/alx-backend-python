#!/usr/bin/env python3
"""
task to add correct type annotations to a function
"""
from typing import Mapping, Union, Any, TypeVar


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[TypeVar('T'), None] = None)\
                     -> Union[Any, TypeVar('T')]:
    """
    gets the value to the given key in a dictionary
    """
    if key in dct:
        return dct[key]
    else:
        return default
