#!/usr/bin/env python3
"""
This module defines a type-annotated function to return the floor of a float.
"""


import math


def floor(n: float) -> int:
    """
    Return the floor of a given float.

    Args:
        n (float): The float whose floor is to be calculated.

    Returns:
        int: The largest integer less than or equal to n.
    """
    return math.floor(n)
