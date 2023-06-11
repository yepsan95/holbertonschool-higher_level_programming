#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if x <= 0 or not my_list:
        return 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
        except Exception:
            print()
            return i
    print()
    return i + 1
