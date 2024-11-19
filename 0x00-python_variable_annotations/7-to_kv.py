#!/usr/bin/env python3
"""
This module defines a type-annotated function that returns
a tuple, with the first element being a string
and the second element being the square of an int or float value.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple where the first element is a string and
the second element is the square of a number.

    Args:
        k (str): A string.
        v (Union[int, float]): An integer or a float.

    Returns:
        Tuple[str, float]: A tuple with the
 string and the square of the number as a float.
    """
    return (k, float(v ** 2))
