#!/usr/bin/python3
"""
./11-main.py student.json
"""


class Student:
    """
    class Student that defines a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        IInstantiation with first_name, last_name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
