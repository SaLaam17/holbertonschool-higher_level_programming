#!/usr/bin/python3
"""
Return the sum of two integers or floats.
"""

def add_integer(a, b=98):

    """
    'add_integer(a, b)': return the sum (a + b) of two integers or floats.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    sum = a +b
    return sum
