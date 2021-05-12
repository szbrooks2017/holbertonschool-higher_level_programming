#!/usr/bin/python3
""" a function that writes a string to a text file, returns characters"""


def write_file(filename="", text=""):
    """ write a string to UTF8, return characters"""
    with open(filename, 'w', encoding='utf8') as jfile:
        jfile.write(text)
        count = len(text)
        return count
