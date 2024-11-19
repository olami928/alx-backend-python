#!/usr/bin/env python3

from typing import Mapping, Any, Union, TypeVar

# Create a TypeVar to represent the generic type of values in the dictionary

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, None]:
    """
    Safely get the value associated with the key in the dictionary.

    Args:
        dct (Mapping[Any, T]): The dictionary to search for the key.
        key (Any): The key to look up in the dictionary.
        default (Union[T, None], optional): The value to return if the key is not found. Defaults to None.

    Returns:
        Union[T, None]: The value associated with the key, or the default value (or None if not provided).
    """
    if key in dct:
        return dct[key]
    else:
        return default
