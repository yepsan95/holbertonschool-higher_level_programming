#!/usr/bin/python3
"""Module that defines a square.
"""
class Square:
    """Class square that defines a square.
    """
    def __init__(self, size=0):
        """Constructor '__init__' method.

        Args:
            __size (int): Size of the square.
        """
        self.__size = size
    @property
    def size(self):
        """Getter method.
        """
        return self.__size
    @size.setter
    def size(self, value):
        """Class 'size' method. Returns the size of the square.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    def area(self):
        """Class 'area' method. Returns the area of the square.
        """
        return self.__size ** 2
