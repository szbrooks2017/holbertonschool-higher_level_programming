#!/usr/bin/python3
""" A function that prints a square
size is the length
size must be int or TypeError
size > 0 or ValueError
size is a float or < 0 then TypeError
"""


def print_square(size):
    """ a function that prints a square """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if float(size) < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print(size * '#')
