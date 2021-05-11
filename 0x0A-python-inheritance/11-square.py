#!/usr/bin/python3
""" inherit an inherited class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ inception """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__height = size
        self.__width = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__width, self.__height)
