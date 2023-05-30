#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        c = str[i]
        if 97 <= ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
