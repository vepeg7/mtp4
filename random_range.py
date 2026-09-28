"""Целые в закрытом диапазоне: список и генератор."""

from __future__ import annotations

import random


def iter_ranged(low: int, high: int, count: int, seed: int):
    # randint включает и low, и high.
    source = random.Random(seed)
    for _ in range(count):
        yield source.randint(low, high)


def ranged_random(low: int, high: int, count: int, seed: int) -> list[int]:
    return list(iter_ranged(low, high, count, seed))
