#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = 0
    for i in set(my_list):
        unique += i
    return unique
