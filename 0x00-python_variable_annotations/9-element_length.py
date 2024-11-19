#!/usr/bin/env python3
"""
This module defines a function that returns the length of 
each element in a list of sequences.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Given a list of sequences, return a list of tuples, where each tuple contains:
    - A sequence (e.g., string or list)
    - The length of that sequence

    Args:
        lst (Iterable[Sequence]): An iterable of sequences (e.g., list of strings or list of lists).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each containing a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
