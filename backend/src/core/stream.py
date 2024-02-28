import itertools
from typing import Iterable, Callable


class Stream[T]:
    def __init__(self, iterable: Iterable[T]):
        self._iterable = iterable

    def map[U](self, func: Callable[[T], U]) -> "Stream[U]":
        return Stream(map(func, self._iterable))

    def flatmap[U](self, func: Callable[[T], U]) -> "Stream[U]":
        iter1 = map(func, self._iterable)
        return Stream(itertools.chain.from_iterable(iter1))

    def filter(self, func: Callable[[T], bool]) -> "Stream[T]":
        return Stream(filter(func, self._iterable))

    def foreach(self, func) -> None:
        for item in self._iterable:
            func(item)

    def collect[U](self, func: Callable[[T], U]) -> U:
        return func(self._iterable)

