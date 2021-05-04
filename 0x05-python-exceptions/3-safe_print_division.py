#!/usr/bin/python3
def safe_print_division(a, b):
    """
    # a & b are ints
    # results printed in finally:
    # print statment starts with "Inside result:"
    # return the value of hte division else none
    """
    try:
        quotient = a / b
    except ZeroDivisionError:
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))
        return (quotient)
