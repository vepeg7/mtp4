"""Сумма последовательности через functools.reduce."""

from __future__ import annotations

from functools import reduce


def sum_with_reduce(numbers: list[int]) -> int:
    return reduce(lambda acc, item: acc + item, numbers, 0)
