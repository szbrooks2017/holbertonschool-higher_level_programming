#!/usr/bin/python3
import sys
if __name__ == '__main__':
    n = len(sys.argv)
    if n == 1:
        print("{}".format("0 arguments."))
    elif n == 2:
        print("{}".format("1 argument:"))
    else:
        print("{} {}".format(n - 1, "arguments:", end=""))
        for i in range(1, n):
            print("{}: {}".format(i, sys.argv[i]))
