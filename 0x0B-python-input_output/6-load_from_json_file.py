#!/usr/bin/python3
""" create an object from a json file"""
import json


def load_from_json_file(filename):
    """ creates an obj from a json"""
    with open(filename) as jfile:
        return json.loads(jfile.read())
