#!/usr/bin/env python3
"""A module that implements an safe_first_element() function
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """safely returns the first elemen of a Sequence"""
    if lst:
        return lst[0]
    else:
        return None
