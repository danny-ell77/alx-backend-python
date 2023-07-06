#!/usr/bin/env python3
"""A module that implements an element_length() function
"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Augment the following code with the correct duck-typed annotations:"""
    return [(i, len(i)) for i in lst]
