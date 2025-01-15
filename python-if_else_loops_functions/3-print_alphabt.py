#!/usr/bin/python3
for i in range(98, 123):
    if chr(i) not in ('e', 'q'):
        print("{}".format(chr(i)), end="")
