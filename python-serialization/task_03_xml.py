#!/usr/bin/python3
"""
Module to serialization and deserialization
using XML as an alternative format to JSON.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Function that serializes the dictionary into XML
    and saves it to the given filename.
    Args:
        dictionary (dict): The Python dictionary to serialize.
        filename (str): The path to the output XML file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        item = ET.Element(key)
        item.text = str(value)
        root.append(item)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Function that takes a filename as its parameter,
    reads the XML data from that file,
    and returns a deserialized Python dictionary.
    Args:
        filename (str): The path to the input XML file.
    Returns:
        dict: The deserialized Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        dictionary = {}
        for item in root:
            key = item.tag
            value = item.text

            # Conversion des types de données
            if value.isdigit():
                value = int(value)
            elif value.lower() == 'true':
                value = True
            elif value.lower() == 'false':
                value = False
            else:
                try:
                    value = float(value)
                except ValueError:
                    pass

            dictionary[key] = value

        return dictionary
    except FileNotFoundError:
        print("File not found")
        return {}
    except ET.ParseError:
        print("Error parsing the XML file")
        return {}
