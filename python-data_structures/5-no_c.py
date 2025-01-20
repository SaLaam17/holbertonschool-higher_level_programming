#!/usr/bin/python3
def no_c(my_string):
    no_c = "cC"
    new_string = ''.join([c for c in my_string if c not in no_c])
    return new_string
