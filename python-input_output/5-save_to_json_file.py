#!/usr/bin/python3
"""
This module defines the function 'save_to_json_file()'.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (obj): Object to be encoded to JSON.
        filename: Name of the file to be overwritten.
    """

    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
