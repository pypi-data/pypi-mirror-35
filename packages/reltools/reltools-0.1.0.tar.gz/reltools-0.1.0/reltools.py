"""Relation tools for Python."""

from itertools import dropwhile, groupby
from operator import itemgetter
from typing import Callable, Generic, Iterable, Iterator, Tuple, TypeVar

from more_itertools import peekable

__version__ = '0.1.0'
__author__ = 'Yu Mochizuki'
__author_email__ = 'ymoch.dev@gmail.com'


Key = TypeVar('Key')
Value = TypeVar('Value')
Left = TypeVar('Left')
Right = TypeVar('Right')

DEFAULT_KEY = itemgetter(0)


class _UnidirectionalFinder(Generic[Value, Key]):
    """
    This class finds items in `iterable` unidirectionally
    and groups them by the given `key`.

    Note that the `Key` must be 'comparable'
    (supports `__lt__()` and  `__gt__()`)
    and `iterable` must be sorted by `key`.

    Here are some normal cases.
    Collections are sorted by the first items.
    >>> iterable = [(0, 'a'), (1, 'b'), (1, 'c'), (2, 'd')]
    >>> finder = _UnidirectionalFinder(iterable, itemgetter(0))

    When given a waiting key, then finds items and groups them by the key.
    >>> list(finder.find(1))
    [(1, 'b'), (1, 'c')]

    When given passed keys, then cannot find items.
    >>> list(finder.find(1))
    []
    >>> list(finder.find(0))
    []

    When given too large keys, then cannot find items.
    >>> list(finder.find(3))
    []

    Once given a too large key,
    when given an existing key, then cannot find items.
    >>> list(finder.find(2))
    []

    Here are some seminormal cases.
    When given an empty collection, then cannot find any items.
    >>> finder = _UnidirectionalFinder([], itemgetter(0))
    >>> list(finder.find(0))
    []

    When given a not sorted `iterable`,
    then skips the reverse-ordering segments.
    >>> iterable = [(0, 'a'), (2, 'b'), (1, 'c'), (3, 'd')]
    >>> finder = _UnidirectionalFinder(iterable, itemgetter(0))
    >>> list(finder.find(2))
    [(2, 'b')]
    >>> list(finder.find(1))
    []
    >>> list(finder.find(3))
    [(3, 'd')]
    """
    __EMPTY_LIST = []  # type: List[Value]

    def __init__(self, iterable: Iterable[Value], key: Callable[[Value], Key]):
        """Initialize"""
        self._groups = groupby(iterable, key)

    def find(self, key: Key) -> Iterator[Value]:
        """Find items that have the given key."""
        self.seek_to(key)

        try:
            group = self._groups.peek()
        except StopIteration:
            return iter(self.__EMPTY_LIST)

        group_key, group_items = group
        if group_key > key:
            return iter(self.__EMPTY_LIST)

        return group_items

    def seek_to(self, key: Key) -> None:
        """Seek to the given key."""
        seeked_groups = dropwhile(lambda group: group[0] < key, self._groups)
        self._groups = peekable(seeked_groups)


def relate_one_to_many(
    lhs: Iterable[Left],
    rhs: Iterable[Right],
    lhs_key: Callable[[Left], Key]=DEFAULT_KEY,
    rhs_key: Callable[[Right], Key]=DEFAULT_KEY,
) -> Iterator[Tuple[Left, Iterator[Right]]]:
    """
    Relates `rhs` items to each `lhs` items.

    Note that:
    - `Key` must be 'comparable' (supports `__lt__()` and  `__gt__()`).
    - `lhs` must be sorted by keys that `lhs_key` provides.
    - `rhs` must be sorted by keys that `rhs_key` provides.

    `lhs_key` and `rhs_key` are optional.
    When not given, then relates `rhs` to `lhs`
    by their first items (`left[0]` and `right[0]`).

    Here are some normal cases.
    These collections are sorted by the first items.
    >>> lhs = [(0, 'a'), (1, 'b'), (2, 'c')]
    >>> rhs = [(1, 's'), (2, 't'), (2, 'u'), (3, 'v')]

    When not given any keys,
    then relates `rhs` to `lhs` by their first items.
    >>> relations = relate_one_to_many(lhs, rhs)
    >>> for left, right in relations:
    ...     left, list(right)
    ((0, 'a'), [])
    ((1, 'b'), [(1, 's')])
    ((2, 'c'), [(2, 't'), (2, 'u')])

    When given custom keys, then relates `rhs` to `lhs` by that keys.
    Note that the custom keys *must not* break the key ordering.
    >>> relations = relate_one_to_many(
    ...     lhs, rhs,
    ...     lhs_key=lambda l: l[0] * 2,
    ...     rhs_key=lambda r: r[0] - 1)
    >>> for left, right in relations:
    ...     left, list(right)
    ((0, 'a'), [(1, 's')])
    ((1, 'b'), [(3, 'v')])
    ((2, 'c'), [])

    Here are some seminormal cases.
    When given an empty `lhs`, then returns an empty iterator.
    >>> relations = relate_one_to_many([], [(1, 's')])
    >>> next(relations)
    Traceback (most recent call last):
        ...
    StopIteration

    When given an empty `rhs`, then returns an iterator that relates nothing.
    >>> relations = relate_one_to_many([(1, 'a')], [])
    >>> for left, right in relations:
    ...     left, list(right)
    ((1, 'a'), [])

    When given unordered `lhs`, then skips relationing
    on reverse-ordering segments.
    >>> lhs = [(0, 'a'), (2, 'b'), (1, 'c'), (4, 'd'), (3, 'e')]
    >>> rhs = [(1, 's'), (2, 't'), (2, 'u'), (3, 'v'), (4, 'w')]
    >>> relations = relate_one_to_many(lhs, rhs)
    >>> for left, right in relations:
    ...     left, list(right)
    ((0, 'a'), [])
    ((2, 'b'), [(2, 't'), (2, 'u')])
    ((1, 'c'), [])
    ((4, 'd'), [(4, 'w')])
    ((3, 'e'), [])

    When given unordered `rhs, then skips relationing
    on reverse-ordering segments.
    >>> lhs = [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]
    >>> rhs = [(1, 's'), (3, 't'), (3, 'u'), (2, 'v'), (4, 'w')]
    >>> relations = relate_one_to_many(lhs, rhs)
    >>> for left, right in relations:
    ...     left, list(right)
    ((0, 'a'), [])
    ((1, 'b'), [(1, 's')])
    ((2, 'c'), [])
    ((3, 'd'), [(3, 't'), (3, 'u')])
    ((4, 'e'), [(4, 'w')])
    """
    rhs_finder = _UnidirectionalFinder(rhs, rhs_key)
    return ((l, rhs_finder.find(lhs_key(l))) for l in lhs)
