#!/usr/bin/python3
""" 12-main """


def pascal_triangle(n):
    """ pascal """
    if n <= 0:
        return ([])
    if n == 1:
        return [[1]]
