#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    """
    #my_list can contain any type
    #all ints print on same line with \ n other types must be skipped
    #x represents the number of elements to access in my_list
    #x can be bigger than the length - exception
    #Return the real number of ints printed
    """
    count = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (IndexError, ValueError, TypeError):
            continue

    print()
    return count
