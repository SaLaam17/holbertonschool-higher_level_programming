#!/usr/bin/python3
"""
Module that defines class Student.
"""


class Student:
    """
    class Student that defines a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiation with first_name, last_name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings,
        only attribute names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved.
        """
        if attrs is None:
            return self.__dict__

        if isinstance(attrs, list) and all(
            isinstance(attr, str) for attr in attrs
        ):
            return {
                key: value for key, value in self.__dict__.items()
                if key in attrs
            }

        return self.__dict__

    def reload_from_json(self, json):
        """
        Public method that replaces all attributes of the Student instance
        with those in the json dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
