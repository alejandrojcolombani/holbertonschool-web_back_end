#!/usr/bin/env python3
"""Execute several random-delay coroutines concurrently."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run ``wait_random`` ``n`` times and return delays in ascending order."""
    delays: List[float] = []
    coroutines = [wait_random(max_delay) for _ in range(n)]

    for coroutine in asyncio.as_completed(coroutines):
        delays.append(await coroutine)

    return delays
