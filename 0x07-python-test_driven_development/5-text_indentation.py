#!/usr/bin/python3
""" print a text with 2 new lines afer . ? :
text must be string or typeerror
no space at teh beginning of the printed line
"""


def text_indentation(text):
    """ a function that prints a text with new lines """

    idx = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for idx in text:
        if idx == ' ' and starting == 1:
            continue

        if idx == '.' or idx == '?' or idx == ':':
            print("{}{}".format(idx, '\n'))
            starting = 1
        else:
            print(idx, end="")
            starting = 0
