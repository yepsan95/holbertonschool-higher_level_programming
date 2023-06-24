#!/usr/bin/python3
"""
Module that defines function 'is_kind_of_clas()'.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of a_class or any of its superclasses.

    Args:
        obj (any): Object to be checked.
        a_class (type): The class that object should belong to
        (or any of its superclasses).
    Returns:
    If obj is an instance of a_class or any of its superclasses - True.
    Otherwise - False.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
