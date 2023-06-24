#!/usr/bin/python3
"""
This module defines the function 'say_my_name()'.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the name and last name of a person.

    Args:
        first_name (str): First name of the person.
        last_name (str): Last name of the person.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {}".format(first_name, last_name), end="")
    if last_name is not "":
        print(" {}".format(last_name), end="")
    print()
