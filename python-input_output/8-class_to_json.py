#!/usr/bin/python3
"""
This module defines the function 'class_to_json()'.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object

    Args:
        obj (obj): Object to be described.
    Returns:
         Returns the dictionary description with simple data structure
         (list, dictionary, string, integer and boolean).
    """

    return obj.__dict__
