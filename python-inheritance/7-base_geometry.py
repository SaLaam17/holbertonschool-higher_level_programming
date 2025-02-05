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
        Public instance method that raises an exception
        indicating that the area() method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        method that validates value
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
