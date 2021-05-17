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

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + '.json.'
        try:
            obj = from_json_string(filename)
        except:
            obj = []

        create(cls, **dictionary)

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

    @staticmethod
    def from_json_string(json_string):
        """ returns list from json string"""
        if json_string is None:
            return []
        pfile = json.loads(json_string)
        return pfile

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes set"""
        if cls.__name__ is "Rectangle":
            dummy = cls(2, 3)
        if cls.__name__ is "Square":
            dummy = cls(2)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances"""
        filename = cls.__name__ + '.json'
        obj = []
        try:
            with open(filename, 'r') as f:
                obj = cls.from_json_string(f.read())
                for i, e in enumerate(obj):
                    obj[i] = cls.create(**obj[i])
            return obj
        except:
            return obj
