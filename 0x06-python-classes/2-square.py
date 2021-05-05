#!/usr/bin/python3

""" a Square with size, private instance attriute size
    size is an int else raise typeerror, exception
    if size < 0 raise valueerror, exception
"""


class Square:

    """a class that creates a single attribute"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
