#!/usr/bin/python3
"""
This module contains the CountedIterator class
"""


class CountedIterator:
    """CountedIterator class"""

    def __init__(self, iterable):
        """Instantiation with iterator and counter

        Args:
            iterable: Iterator object
        """
        self._iterator = iter(iterable)
        self._counter = 0

    def __iter__(self):
        """Returns the iterator object"""
        return self

    def __next__(self):
        """Fetches and returns the next item in the iterator"""
        item = next(self._iterator)
        self._counter += 1
        return item

    def get_count(self):
        """Returns the current value of the counter"""
        return self._counter
