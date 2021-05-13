#!/usr/bin/python3
""" return the json representation of an object"""


import json
def to_json_string(my_obj):
    """ return json"""
    jfile = json.dumps(my_obj)
    return jfile
