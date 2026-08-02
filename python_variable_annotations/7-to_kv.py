#!/usr/bin/env python3
"""Provide a function that builds a key and squared-value tuple."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return ``k`` paired with the square of ``v`` as a float."""
    return (k, float(v ** 2))
