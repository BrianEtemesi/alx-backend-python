#!/usr/bin/env python3
"""
task to annotate function with correct duck types
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    returns the first element of a list
    """
    if lst:
        return lst[0]
    else:
        return None
