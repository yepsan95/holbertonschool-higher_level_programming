#!/usr/bin/python3
"""
This modules defines a class 'Square' that inherits from 'Rectangle'.
"""
Rectangle = __import__('9-rectangle.py').Rectangle


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

        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square.
        """

        return size ** 2
