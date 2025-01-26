#!/usr/bin/python3
"""
This module provides a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each of these characters: ., ? and :
    Arg:
        text: The text to be printed
    Raises:
        TypeError: If text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    chars = ['.', '?', ':'] 
    result = ""

    for char in text:
        result += char
        if char in chars:
            print(result.strip(), end="\n\n")
            result = ""
    if result.strip():
        print(result.strip(), end="")
