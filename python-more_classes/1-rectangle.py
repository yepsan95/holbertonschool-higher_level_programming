#!/usr/bin/python3
"""
This modules defines a class 'Rectangle'.
"""


class Rectangle:
    """
    Defines a rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle.

        Args:
            widht (int): Width of the new rectangle.
            height (int): Height of the new rectangle.
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Property getter for private instance attribute 'width'

        Returns:
            Value of the 'width' attribute.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Property setter for private instance attribute 'width'.

        Args:
            value (int): width of the new rectangle.
        """

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Property getter for private instance attribute 'height'

        Returns:
            Value of the 'height' attribute.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Property setter for private instance attribute 'height'.

        Args:
            value (int): height of the new rectangle.
        """

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
