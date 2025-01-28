#!/usr/bin/python3
"""
Module that defines a rectangle.
"""


class Rectangle:
    """
    Represent a rectangle with width and height attributs.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with a given size.
        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
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
        int: the width of the rectangle.
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
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.
        Returns:
            int: the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.
        Returns:
            value(int): the new height of thr rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Method that returns the rectangle area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Method that returns the rectangle perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))
