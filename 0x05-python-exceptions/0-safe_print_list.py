#!/usr/bin/python3
""" a function that prints x of a list """


def safe_print_list(my_list=[], x=0):

    count = 0
    for count in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break

    print()
    return count
