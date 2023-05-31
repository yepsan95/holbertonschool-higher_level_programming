#!/usr/bin/python3
if __name__ == '__main__':

    from sys import argv as argv

    args = "argument"
    if len(argv) == 1:
        args = args + "s."
    elif len(argv) == 2:
        args = args + ":"
    elif len(argv) > 2:
        args = args + "s:"
    print("{} {}".format(len(argv) - 1, args))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
