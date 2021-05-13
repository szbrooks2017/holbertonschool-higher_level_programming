#!/usr/bin/python3
""" adds all arguments to a python list and then save them to a file"""
import json
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

# load from json returns an obj from a json file

try:
    newlist = load_from_json_file('add_item.json')
except:
    newlist = []
newerlist = newlist + argv[1:]
# save to json returns an obj to a file
save_to_json_file(newerlist, 'add_item.json')
