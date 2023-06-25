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
