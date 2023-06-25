#!/usr/bin/python3
"""
This module defines the function 'append_write()'.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    and returns the number of characters added.

    Args:
        filename (str): Name of the file to append the text.
        text (str): Text to be appendede to the file.
    Returns:
        Number of character added.
    """

    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
