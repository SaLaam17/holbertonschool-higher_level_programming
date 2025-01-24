#!/usr/bin/python3
"""
Return the sum of two integers or floats.
"""


def add_integer(a, b=98):

    """
    """
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    if not isinstance(a, float):
        raise TypeError("a must be a float")
    if not isinstance(b, int):
        raise TypeError("b must be an float")

    return

if __name__ == "__main__":
    import doctest
doctest.testfile("0-add_integer.txt")
