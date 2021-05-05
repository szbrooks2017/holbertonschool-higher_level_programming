#!/usr/bin/python3
"""
a & b must be int/float or TypeError w/exception
a & b must be casted to int if float
return a + b
"""

def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    add_int = a + b
    if type(add_int) is float:
        return int(add_int)
    return add_int
