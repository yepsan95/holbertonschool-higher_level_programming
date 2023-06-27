#!/usr/bin/python3
"""
This module defines a class 'MyList' that inherits from 'list'.

"""


class MyList(list):
    """
    Subclass of 'list'.
    """

    def print_sorted(self):
        """
        Prints the list, but sorted (ascending order).
        """

        if issubclass(MyList, list):
            print(sorted(self))
