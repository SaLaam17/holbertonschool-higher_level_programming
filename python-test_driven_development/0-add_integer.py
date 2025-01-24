#!/usr/bin/python3
"""
Return the sum of two integers or floats.
"""
import doctest

def add_integer(a, b=98):

    """
    """
    if not isinstance(a, int):
        raise TypeError("a must be an integer or a float")
    if not isinstance(b, int):
        raise TypeError("b must be an integer or a float")

    sum = a +b
    return sum

if __name__ == "__main__":
    doctest.testfile("0-add_integer.txt")
