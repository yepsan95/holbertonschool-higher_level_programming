#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if 97 <= ord(str[i]) <= 122:
            str[i] = str[i] - 32
        print("{}".format(str[i]), end="")
    print("")
