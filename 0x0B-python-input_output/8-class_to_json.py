#!/usr/bin/python3
""" a function that returns teh dictionary with of a data structure"""


def class_to_json(obj):
    """ obj is an instance of a class"""
    return vars(obj)
