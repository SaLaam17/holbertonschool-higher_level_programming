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

    @property
    def size(self):
        """
        Getter method for the size attribute.
        Returns:
            int: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.
         Returns:
            value (int): the new size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Method that calculate the square area
        Returns:
            int: The area of the square
        """

        return self.__size ** 2
