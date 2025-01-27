#!/usr/bin/python3
"""
This module defines class named Square with a size attirbute.
"""


class Square:
    """
    Represents a square with a length equal to size.
    """
    def __init__(self, size=0):
        """
        Initializes the square with a given size.
        Args:
            size (int): the size of the square
        """

        self.__size = size
