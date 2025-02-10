#!/usr/bin/python3
"""
Module documentation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file,
    using a JSON representation.
    """
    with open("my_obj.json", 'w') as filename:
        json.dump(my_obj, filename)
