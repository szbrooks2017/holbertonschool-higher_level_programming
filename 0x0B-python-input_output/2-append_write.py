#!/usr/bin/python3
""" append a string to the end of a text file"""


def append_write(filename="", text=""):
    """ append to the end, and return numbers of characters"""
    with open(filename, 'a', encoding="utf8") as jfile:
        jfile.write(text)

    return len(text)
