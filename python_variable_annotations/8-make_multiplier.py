#!/usr/bin/env python3
"""Provide a factory for type-annotated multiplier functions."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by ``multiplier``."""
    def multiply(value: float) -> float:
        """Multiply ``value`` by the multiplier captured by the closure."""
        return value * multiplier

    return multiply
