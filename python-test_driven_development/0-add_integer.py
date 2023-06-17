#!/usr/bin/python3
"""
This module defines a function 'add_integer()'that adds 2 numbers
and returns the result.
The DocTest script for this module is located in the ./tests directory
and it's named '0-add_integer.txt'.
"""


def add_integer(a, b=98):
    """
    Adds 2 integers and returns the result.
    The arguments can be either integers or floats.
    It takes at least 1 argument and 2 at the most.
    If only one argument is provided, the second argument is set to 98 by default.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
