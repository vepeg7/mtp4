"""Итератор, который сам хранит позицию."""

from __future__ import annotations


class TokenIterator:
    def __init__(self, items) -> None:
        self._items = list(items)
        self._pos = 0

    def __iter__(self) -> TokenIterator:
        return self

    def __next__(self):
        if self._pos >= len(self._items):
            raise StopIteration
        item = self._items[self._pos]
        self._pos += 1
        return item
