#!/usr/bin/python3
append_write = __import__('2-append_write').append_write

nb_characters_added = append_write("file_append.txt", "is not so cool!\n")
print(nb_characters_added)
