#!/usr/bin/python3
import json

"""
This module defines a function 'to_json_string()'.
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj (obj): Object whose representation is to be printed as JSON.
    Returns:
        JSON representation of my_obj.
    """

    return json.dumps(my_obj)
