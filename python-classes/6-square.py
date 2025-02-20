#!/usr/bin/python3
"""
This module defines class named Square with a size attribute.
"""


class Square:
    """
    Represents a square with his side equal to size.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with a given size and a square position.
        Args:
            size (int): the size of the square
            position (tuple): coordinates of a square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2 or not all(
            isinstance(num, int) and num >= 0 for num in position):
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Getter method for the position attribute.
        Returns:
            int: the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute.
        Returns:
            value (int): the new position of the square.
        """
        if not isinstance(value, tuple):
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Method that calculate the square area
        Returns:
            int: The area of the square
        """

        return self.__size ** 2

    def my_print(self):
        """
        Method that prints in stdout the square with the character #
        If size is equal to 0, print an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
