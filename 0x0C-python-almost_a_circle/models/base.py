#!/usr/bin/python3
""" Class is Base: in it there is a private class attribute
    a class constructor ( __init__)
    this class is the base of all other classes in the project.
    the goal is to manage id attribute in all future classes to
    avoid duplicating the same code
""""

class Base:
    """ create constructor if id is not none, assign id with this value """
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None
            self.id = id
        __nb_objects += newValue
        self.newValue = id
