#!/usr/bin/python3
"""
This module defines the function 'write_file()'.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8)
    and returns the number of characters written.

    Args:
        filename (str): Name of the file to be overwritten.
        text (str): Text to be written to the file.
    """

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
