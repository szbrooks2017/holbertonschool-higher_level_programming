#!/usr/bin/python3
""" class Rectangle inherits from Base"""
from models.base import Base


class Rectangle(Base):

    """ Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def update(self, *args, **kwargs):
        """ assign an argument to each attribute"""
        attributes = ['id', 'width', 'height', 'x', 'y']

        if args:
            for item in range(len(args)):
                setattr(self, attributes[item], args[item])
        if kwargs:
            for item in kwargs:
                setattr(self, item, kwargs[item])

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ define the area """
        return self.__height * self.__width

    def display(self):
        """ print out the rectangle with #"""
        x = self.x
        y = self.y
        h = self.height
        w = self.width
        string = ((' ' * x) + ('#' * w) for item in range(h))
        print(('\n' * y) + '\n'.join(string))

    def __str__(self):
        """ overriding str to print specific message"""
        x = self.x
        y = self.y
        h = self.height
        w = self.width
        i = self.id
        return "[Rectangle] ({:d}) {}/{} - {}/{}".format(i, x, y, w, h)
