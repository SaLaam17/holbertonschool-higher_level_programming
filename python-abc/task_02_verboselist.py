#!/usr/bin/python3
"""
Module that create a class named VerboseList
that extends the Python list class.
"""


class VerboseList(list):
    """
    Class that inherits from the built-in list class.
    """

    def append(self, item):
        """
        Override the append method to add a message.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """
        Override the extend method to add a message.
        """
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, item):
        """
        Override the remove method to add a message.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
        Override the pop method to add a message.
        """
        item = super().pop(index)
        print("Popped [{}] from the list.".format(index))
        return item
