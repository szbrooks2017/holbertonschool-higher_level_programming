#!/usr/bin/python3
""" A function that prints a name
first & last name must be strings otherwise TypeError
Exception message differs from first and last
"""


def say_my_name(first_name, last_name=""):

    """ a function that prints a name """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {0} {1}".format(first_name, last_name))
