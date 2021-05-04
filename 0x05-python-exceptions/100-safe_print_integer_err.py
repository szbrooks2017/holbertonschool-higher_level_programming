#!/usr/bin/python3
import sys
"""
print int with newline
value is any type
teturn true if value = int
else return false print stderr/Exception:
"""
def safe_print_integer_err(value):

    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        print("Exception: ".format(file=sys.stderr))
        return False
