#!/usr/bin/python3
"""Module that defines a square.
"""
class Square:
    """Class square that defines a square.
    """
    def __init__(self, size=0):
        """Constructor __init__ method.

        Args:
            __size (int): Size of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
