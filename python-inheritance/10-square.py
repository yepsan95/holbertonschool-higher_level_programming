#!/usr/bin/python3
"""
This modules defines a class 'Square' that inherits from 'Rectangle'.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines a Square. Inherits from 'Rectangle'.
    """

    def __init__(self, size):
        """
        Initializes the square.

        Args:
            size (int): Size of the square.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
