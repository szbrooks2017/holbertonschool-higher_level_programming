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

        self.size = size
        self.position = position

        if type(position) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(size) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if min(value) <= 0 and len(value) < 2:
            raise TypeError("position must be tuple of 2 positive integers")
        if not isinstance(value, int):
            raise TypeError("position must be tuple of 2 positive integers")
        if isinstance(value[1], int) is not True:
            raise TypeError("position must be tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        square_area = self.__size * self.__size
        return square_area

    def my_print(self):
        if self.__size is 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
