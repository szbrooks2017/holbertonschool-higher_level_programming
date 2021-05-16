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
