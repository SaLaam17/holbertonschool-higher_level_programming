#!/usr/bin/python3
"""
This module provides a function that adds two integers or floats.
"""


def add_integer(a, b=98):

    """
    'add_integer(a, b)': return the sum (a + b) of two integers or floats.

    Args:
        a: The first integer or float.
        b: The second integer or float, default is 98.

    Returns:
        int: The sum of a and b after casting them to integers.

    Raises:
        TypeError: If a or b are not integers or floats.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or a float")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
