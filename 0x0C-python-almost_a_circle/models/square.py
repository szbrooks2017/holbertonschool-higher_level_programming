#!/usr/bin/python3
"""class Square inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):

    """ Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ overiding str with new specifications"""
        return "[Rectangle] ({:d})\
                 {}/{} - {}".format(self.id, self.x, self.y, self.size)
