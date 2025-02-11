#!/usr/bin/env python3
"""
Module that defines class CustomObject.
"""
import pickle


class CustomObject:
    """
    CustomObject class with name, age, and is_student attributes.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes the square with a given size.
        Args:
            name (a string): The name of the person.
            age (an integer): The age of the person.
            is_student (a boolean): True if the person
            is a student, otherwise False.
        """

        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        method to print out the object’s attributes
        """
        print("Name: {}\nAge: {}\nIs Student: {}".format(
            self.name, self.age, self.is_student))

    def serialize(self, filename):
        """
        Method to serialize the current instance
        of the object and save it to the provided filename.
        """
        if not filename:
            return None
        try:
            with open("filename", "wb") as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error during serialization: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Method to load and return an instance
        of the CustomObject from the provided filename.
        """
        if not filename:
            return None
        try:
            with open("filename", "rb") as file:
                return pickle.load(file)
        except Exception as e:
            print(f"Error during deserialization: {e}")
            return None
