#!/usr/bin/python3
"""
#mylist1 and 2 can contain any type
list length can be bigger than both lists
return  a new list with all divisions
if 2 elements cant be divided results = 0
if an element is not an int/float print wrong type
if division cant be done print division by 0
if mylist 1 or 2 is too short print out of range
"""

def list_division(my_list_1, my_list_2, list_length):

    reslist = []

    for i in range(list_length):
        res = 0
        try:
            res = (my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            reslist.append(res)
    return reslist
