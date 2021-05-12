#!/usr/bin/python3
""" function that reads a text file and prints to stdout"""


def read_file(filename=""):
    """ reads a text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
