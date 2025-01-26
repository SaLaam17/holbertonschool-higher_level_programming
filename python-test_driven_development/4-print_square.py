#!/usr/bin/python3
"""
That function prints a square with the character #.
"""


def print_square(size):
    """
    Print a square with the character '#'.

    Arg:
        size, the length of the square
    Raises:
        TypeError: If size is not an integer
        ValueError: If size size is less than 0
    """
    if size is None:
        raise ValueError("size must be provided")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
