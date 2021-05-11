#!/usr/bin/python3
""" Class BaseGeometry, def area, exception"""


class BaseGeometry:
    """ exception in area"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
