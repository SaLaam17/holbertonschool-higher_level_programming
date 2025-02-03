#!/usr/bin/python3
"""
Module that defines a class MyList
that extends the built-in list class
"""


class MyList(list):
    """
    A custom list class that extends the built-in list
    """
    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order
        """
        print(sorted(self))
