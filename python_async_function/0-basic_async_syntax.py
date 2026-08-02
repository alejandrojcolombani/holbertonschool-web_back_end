#!/usr/bin/env python3
"""Provide a coroutine that waits for a random amount of time."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for and return a random delay from zero to ``max_delay``."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
