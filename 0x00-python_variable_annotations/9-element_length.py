#!/usr/bin/env python3
"""
task to annotate a function's parameter and
return values with appropriate types
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    returns a list of tuples
    """
    return [(i, len(i)) for i in lst]
