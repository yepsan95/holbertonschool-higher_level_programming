#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        print("{}".format(number % 10))
        return (number % 10)
    else:
        print("{}".format(((number * -1) % 10)))
        return (((number * -1) % 10) * -1)
