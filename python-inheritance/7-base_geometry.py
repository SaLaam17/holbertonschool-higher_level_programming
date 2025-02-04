#!/usr/bin/python3
"""
This module defines class named BaseGeometry.
"""


class BaseGeometry:
    """
    represent a class named BaseGeometry
    """
    def area(self):
        """
        Public instance method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        method that validates value
        """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")

        if value <= 0:
            raise ValueError("<name> must be greater than 0")
