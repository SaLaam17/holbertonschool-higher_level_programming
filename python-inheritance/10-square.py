#!/usr/bin/python3
"""
This module defines class named BaseGeometry.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class that inherits from Rectangle
    """
    def __init__(self, size):
        """
        Initialises the square.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return the string representation of the Rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
