"""Декоратор, который отмечает вызов в журнале."""

from __future__ import annotations

import functools
import logging

_CALLS = logging.getLogger("lab.calls")


def logged(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        _CALLS.info("вызов %s", func.__name__)
        return func(*args, **kwargs)

    return wrapper
