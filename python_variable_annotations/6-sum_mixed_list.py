#!/usr/bin/env python3
"""Provide a function that sums integers and floats in one list."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the numeric sum of all values in ``mxd_lst``."""
    return sum(mxd_lst)
