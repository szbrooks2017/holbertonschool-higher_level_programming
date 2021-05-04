#!/usr/bin/python3
""" prints an int with "{:d}".format()"""

def safe_print_integer(value):

    """
    #print int
    #value can be any type
    #returns True if value has been printed(val is an int)
    #else false
    """

    try:
        print("{:d}".format(value))
        return True

    except (ValueError, TypeError):
        return False
