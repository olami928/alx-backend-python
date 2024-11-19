#!/usr/bin/env python3
"""
This module defines a function that returns the first element of a sequence.
If the sequence is empty, it returns None.
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Given a sequence, return its first element if the sequence is non-empty.
    If the sequence is empty, return None.

    Args:
        lst (Sequence[Any]): A sequence (list, tuple, etc.) containing elements of any type.

    Returns:
        Union[Any, None]: The first element of the sequence or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
