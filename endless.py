"""Поток записей без конечного yield."""

from __future__ import annotations

import random


def endless_records(seed: int):
    source = random.Random(seed)
    while True:
        yield {"n": source.randint(0, 9999)}
