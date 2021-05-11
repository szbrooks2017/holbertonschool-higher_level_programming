#!/usr/bin/python3
""" a class that inehrits from list"""


class MyList(list):
    """print the list but sorted"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
