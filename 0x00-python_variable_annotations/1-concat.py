#!/usr/bin/env python3
"""
This module defines a type-annotated function to concatenate two strings.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenate two strings and return the result.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenated result of str1 and str2.
    """
    return str1 + str2
