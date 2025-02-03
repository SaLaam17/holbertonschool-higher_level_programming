#!/usr/bin/python3
"""
Module that defines a class MyList
that inherits from list
"""


class MyList(list):
    """
    A custom list class that inherits from list
    """
    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order
        """
        print(sorted(self))
