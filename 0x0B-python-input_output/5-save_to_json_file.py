#!/usr/bin/python3
""" write an obj to a txt file using json"""
import json


def save_to_json_file(my_obj, filename):
    """ write () an obj to a file, with json"""
    with open(filename, "w", encoding='utf-8') as jfile:
        jobject = json.dumps(my_obj)
        tfile = jfile.write(jobject)
    return tfile
