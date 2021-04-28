#!/usr/bin/python3
def uppercase(str):
    for c in range(len(str)):
        if (ord(str[c]) >= 97) and (ord(str[c]) <= 122):
            alpha = chr(ord(str[c]) - 32)
        else:
            alpha = str[c]
        print("{}".format(alpha), end='')
    print('')
