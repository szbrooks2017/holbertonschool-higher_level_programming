#!/usr/bin/python3

""" a Square with size, private instance attribute size
    prperty def size(self) to retrieve size
    prperty def size(self, value)
    size is an int else raise typeerror, exception
    if size < 0 raise valueerror, exception
    public instance def area
"""


class Square:

    """a class that creates a single attribute"""

    def __init__(self, size=0):

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        square_area = self.__size * self.__size
        return square_area
