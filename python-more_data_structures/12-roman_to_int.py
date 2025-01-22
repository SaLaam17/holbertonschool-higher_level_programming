#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    arabic_number = 0
    previous_roman_value = 0
    for char in reversed(roman_string):
        current_roman_value = roman.get(char, 0)
        if current_roman_value < previous_roman_value:
            arabic_number -= current_roman_value
        else:
            arabic_number += current_roman_value
        previous_roman_value = current_roman_value
    return arabic_number
