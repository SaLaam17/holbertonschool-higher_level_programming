#!/usr/bin/python3
import sys


def main():
    argv = sys.argv[1:]
    total = 0
    for arg in argv:
        total += int (arg)
    print(total)


if __name__ == "__main__":
    main()
