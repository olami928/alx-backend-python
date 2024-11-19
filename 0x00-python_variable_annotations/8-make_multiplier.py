#!/usr/bin/env python3
"""
This module defines a function that returns a multiplier function.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a number by a given multiplier.

    Args:
        multiplier (float): The multiplier.

    Returns:
        Callable[[float], float]: A function that takes a float and multiplies it by the multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier
    
    return multiplier_function
