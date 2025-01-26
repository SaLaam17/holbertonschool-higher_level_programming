#!/usr/bin/python3
"""
That function prints a square with the character #.
"""


def print_square(size):
    """
        Arg: size, the length of the square
    Raises:
        TypeError: If size is not an integer
        TypeError: If size is a float and is less than 0
        ValueError: If size size is less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
