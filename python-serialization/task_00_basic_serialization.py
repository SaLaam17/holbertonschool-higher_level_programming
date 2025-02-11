#!/usr/bin/env python3
"""
Basic serialization module.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Loads data from a JSON file and deserializes it into a Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
