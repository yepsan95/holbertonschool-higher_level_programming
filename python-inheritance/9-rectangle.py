#!/usr/bin/python3
"""
This module defines the class 'Rectangle' that inherits from 'BaseGeometry'.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines a rectangle. Inherits from 'BaseGeometry'.
    """

    def __init__(self, width, height):
        """
        Initializes a new instance of class 'Rectangle'.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle.
        """

        return self.__width * self.__height

    def __str__(self):
        """
        Returns a human-readable string representation of the object.
        """

        string = "[{}]".format(self.__class__.__name__)
        string += " {}/{}".format(self.__width, self.__height)

        return string
