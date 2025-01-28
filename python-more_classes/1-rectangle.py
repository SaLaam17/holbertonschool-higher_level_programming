#!/usr/bin/python3
"""
This module defines a rectangle.
"""


class Rectangle:
    """
    Represent a rectangle with width and height attributs
    """

    def __init__(self, width = 0, height = 0 ):
        """
        Initializes the square with a given size.
        Args:
            width (int): the width of the rectangle
        height (int): the height of the rectangle
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """
        Getter method for the width attribute.
        Returns:
        int: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.
        Returns:
            value (int): the new width of thr rectangle. 
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the heigth attribute.
        Returns:
            int: the heigth of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.
        Returns:
            value (int): the new height of thr rectangle. 
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
