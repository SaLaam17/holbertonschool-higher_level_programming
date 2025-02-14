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
    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)

    with open(filename, 'w') as file:
        tree.write(filename, encoding="utf-8", xml_declaration=True)


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
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {child.tag: child.text for child in root}

    return dictionary
