#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dictionary = dict(sorted(a_dictionary.items()))
    for i in sorted_dictionary:
        print(f"{i}: {sorted_dictionary[i]}")
