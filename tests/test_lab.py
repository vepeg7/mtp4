"""Проверки лабораторной №4."""

from __future__ import annotations

import logging
import subprocess
import sys
from pathlib import Path

import pytest

from endless import endless_records
from iterator import TokenIterator
from logging_deco import logged
from random_range import iter_ranged, ranged_random
from reduce_sum import sum_with_reduce

_ROOT = Path(__file__).resolve().parents[1]


def test_logged_records_name_and_result(caplog: pytest.LogCaptureFixture) -> None:
    @logged
    def total(numbers: list[int]) -> int:
        return sum(numbers)

    with caplog.at_level(logging.INFO, logger="lab.calls"):
        result = total([1, 2, 3])
    assert result == 6
    assert any("total" in message for message in caplog.messages)


def test_ranged_bounds_and_fixed_point() -> None:
    values = list(iter_ranged(1, 10, 30, seed=1))
    assert len(values) == 30
    assert all(1 <= item <= 10 for item in values)
    assert ranged_random(5, 5, 4, 0) == [5, 5, 5, 5]
    assert ranged_random(1, 10, 30, 1) == values


def test_sum_with_reduce() -> None:
    assert sum_with_reduce([1, 2, 3, 4]) == 10
    assert sum_with_reduce([]) == 0
    fixture = [3, 5, 7]
    assert sum_with_reduce(fixture) == 3 + 5 + 7


def test_endless_records() -> None:
    gen = endless_records(1)
    vals = [next(gen) for _ in range(5)]
    extra = next(gen)
    assert all("n" in item for item in vals)
    assert all(isinstance(item["n"], int) for item in [*vals, extra])


def test_token_iterator() -> None:
    walker = TokenIterator([2, 4, 6])
    assert list(walker) == [2, 4, 6]
    with pytest.raises(StopIteration):
        next(walker)


def test_main_cli() -> None:
    completed = subprocess.run(
        [sys.executable, "main.py"],
        cwd=_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr
