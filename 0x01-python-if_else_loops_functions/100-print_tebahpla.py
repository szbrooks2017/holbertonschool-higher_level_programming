#!/usr/bin/python3
for lower in reversed(range(97, 123)):
    if (lower % 2 == 0):
        print("{}".format(chr(lower - 32)), end="")
    else:
        print("{}".format(chr(lower)), end="")
