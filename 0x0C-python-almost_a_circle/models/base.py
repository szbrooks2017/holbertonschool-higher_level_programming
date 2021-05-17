#!/usr/bin/python3
""" Class is Base: in it there is a private class attribute
    a class constructor ( __init__)
    this class is the base of all other classes in the project.
    the goal is to manage id attribute in all future classes to
    avoid duplicating the same code
"""
import json


class Base:

    """ create constructor if id is not none, assign id with this value """
    __nb_objects = 0
    newValue = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns a json object from a list of dicts"""
        jfile = []
        if list_dictionaries is None:
            list_dictionaries = jfile
        jfile = json.dumps(list_dictionaries)
        return jfile

    @classmethod
    def save_to_file(cls, list_objs):
        """saves to json file"""
        filename = cls.__name__ + '.json'
        obj = []
        if list_objs is not None:
            for item in list_objs:
                obj.append(cls.to_dictionary(item))
        with open(filename, 'w') as jfile:
            jfile.write(cls.to_json_string(obj))
