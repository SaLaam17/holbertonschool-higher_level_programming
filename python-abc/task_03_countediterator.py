#!/usr/bin/env python3
"""
Module that defines a class named CountedIterator.
"""


class CountedIterator:
    """
    Class that extends the built-in iterator obtained from the iter function.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator class.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Return the next item in the sequence,
        increment the counter,
        and raise StopIteration if necessary.
        """
        try:
            next_item = next(self.iterator)
            self.count += 1
            return next_item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """
        Method to return the current value of the counter.
        """
        return self.count
