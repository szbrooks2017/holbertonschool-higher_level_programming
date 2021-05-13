#!/usr/bin/python3
""" function that returns an obj to python from json"""
import json


def from_json_string(my_str):
    """ return a python obj"""
    pfile = json.loads(my_str)
    return pfile
