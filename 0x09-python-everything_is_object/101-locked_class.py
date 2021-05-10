#!/usr/bin/python3
""" this is a class that uses slots"""


class LockedClass:
    """ prevent the user from dynamically creating
    a new instance"""

    __slots__ = ['first_name']
