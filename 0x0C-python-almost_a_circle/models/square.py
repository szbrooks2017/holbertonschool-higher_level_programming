#!/usr/bin/python3
"""class Square inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):

    """ Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ overiding str with new specifications"""
        i = self.id
        s = self.width
        x = self.x
        y = self.y
        return "[Square] ({}) {}/{} - {}".format(i, x, y, s)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def to_dictionary(self):
        """ return a dictionary """
        d = {'id': self.id, 'size': self.width,
             'x': self.x, 'y': self.y}
        return d

    def update(self, *args, **kwargs):
        """ updating args and kwargs"""
        attributes = ['id', 'size', 'x', 'y']

        if args:
            for item in range(len(args)):
                setattr(self, attributes[item], args[item])
        if kwargs:
            for item in kwargs:
                setattr(self, item, kwargs[item])
