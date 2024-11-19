#!/usr/bin/env python3
"""
This module defines a type-annotated function to 
calculate the sum of a list of floats.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    Args:
        input_list (List[float]): A list of floats to sum.

    Returns:
        float: The sum of the floats in the list.
    """
    return sum(input_list)
