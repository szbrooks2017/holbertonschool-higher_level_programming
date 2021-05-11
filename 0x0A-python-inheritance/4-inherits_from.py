#!/usr/bin/python3
""" A function that checks if it is a subclass"""


def inherits_from(obj, a_class):
    """ return true if the object is an instance"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
