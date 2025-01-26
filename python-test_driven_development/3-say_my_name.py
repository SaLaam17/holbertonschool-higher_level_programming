#!/usr/bin/python3
"""
That function prints 'My name is <first name> <last name>'
"""


def say_my_name(first_name, last_name=""):
    """
        Print the sentence 'My name is <first name> <last name>'.

        Args:
            first name: The first name.
            last name: The last name.

        Raises:
            TypeError: If first name or last_name are not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if first_name == "":
        raise ValueError("first_name must be provided")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
