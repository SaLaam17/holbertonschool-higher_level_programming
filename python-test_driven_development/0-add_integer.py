#!/usr/bin/python3
"""
Return the sum of two integers or floats.
"""
import doctest

def add_integer(a, b=98):

    """
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or a float")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    sum = a +b
    return sum
