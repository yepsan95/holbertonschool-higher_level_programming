#!/usr/bin/python3
import json
"""
This module defines the function 'from_json_string()'.
"""


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): String to be decoded from JSON.
    Returns:
        Decoded str from JSON.
    """

    return json.loads(my_str)
