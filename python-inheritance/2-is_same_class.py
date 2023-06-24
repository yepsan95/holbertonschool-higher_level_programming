#!/usr/bin/python3
"""
This module defines a function 'is_same_class()'.
"""


def is_same_class(obj, a_class):
    """
    Checks if an obj is exactly an instance of a_class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class that obj should belong.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """

    if type(obj) == a_class:
        return True
    else:
        return False
