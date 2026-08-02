#!/usr/bin/env python3
"""Annotate a duck-typed function operating on iterable sequences."""

from typing import Iterable, List, Sequence, Tuple


def element_length(
        lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return each sequence from ``lst`` paired with its length."""
    return [(i, len(i)) for i in lst]
