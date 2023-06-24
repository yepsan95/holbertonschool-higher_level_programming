#!/usr/bin/python3
"""
Module that defines a function 'inherits_from()'
"""


def inherits_from(obj, a_class):
    """
    Checks if obj is an instance of a class that inherited from
    (directly or indirectly) from a_class.

    Args:
        obj (any): Object to be checked.
        a_class (type): The superclass from which  obj should inherit.
    Returns:
        If obj is an instance of a class that inherited from a_class - True.
        Otherwise - False.
    """

    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
