#!/usr/bin/python3

""" a Square with size, private instance attribute size
    prperty def size(self) to retrieve size
    prperty def size(self, value)
    size is an int else raise typeerror, exception
    if size < 0 raise valueerror, exception
    private instance position, property, property setter
    public instance def area
    public instnace print to stdout with #
    if size = 0 print empty line
"""


class Square:

    """a class that returns the area of a square """

    def __init__(self, size=0, position=(0, 0)):

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if type(position[0]) is not int or position[0] < 0 or\
           type(position[1]) is not int or position[1] < 0 or\
           type(position) is not tuple or len(position) is not 2:
            raise TypeError("position must be tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value[0]) is not int or value[0] < 0 or\
           type(value[1]) is not int or value[1] < 0 or\
           type(value) is not tuple or len(value) is not 2:
            raise TypeError("position must be tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return (self.__size) ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print(' ' * self.__position[0], end='')
            print("#" * self.__size)
