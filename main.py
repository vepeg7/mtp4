"""Демонстрация четвёртой лабораторной на фиксированных seed."""

from __future__ import annotations

import logging

from endless import endless_records
from iterator import TokenIterator
from logging_deco import logged
from random_range import iter_ranged, ranged_random
from reduce_sum import sum_with_reduce


@logged
def boxed_sum(numbers: list[int]) -> int:
    return sum_with_reduce(numbers)


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(name)s: %(message)s")
    print(f"свёртка: {boxed_sum([3, 5, 7])}")
    print(f"диапазон: {ranged_random(1, 10, 6, seed=2)}")
    print(f"тот же генератор: {list(iter_ranged(5, 5, 4, 0))}")
    stream = endless_records(7)
    print(f"первые записи: {[next(stream) for _ in range(4)]}")
    print(f"итератор: {list(TokenIterator([2, 4, 6]))}")


if __name__ == "__main__":
    main()
