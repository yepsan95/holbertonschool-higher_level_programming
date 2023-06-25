#!/usr/bin/python3
"""
This module defines the function 'load_from_json_file()'.
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file.

    Args:
        filename (str): Name of the JSON file.
    Returns:
        Object created from the JSON file.
    """

    with open(filename, "r") as json_file:
        return json.loads(json_file)
