#!/usr/bin/env python3

from typing import List, Union


def zoom_array(lst: List[int], factor: Union[int, float] = 2) -> List[int]:
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(int(factor))  # Use int(factor) to ensure factor is an integer
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)

