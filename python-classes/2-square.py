#!/usr/bin/python3
"""
This module defines class named Square with a size attribute.
"""


class Square:
    """
    Represents a square with his side equal to size.
    """
    def __init__(self, size=0):
        """
        Initializes the square with a given size.
        Args:
            size (int): the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
