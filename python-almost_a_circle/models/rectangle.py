#!/usr/bin/python3
"""
This module defines a class 'Rectangle'.
"""


class Rectangle(Base):
    """
    Class Rectangle that inherits from Base.
    """

    def __init__(self, width, heigth, x=0, y=0, id=None):
        """
        Initializes a new instance of Rectangle.

        Args:
            width (int): Width of the new rectangle.
            height (int): Height of the new rectangle.
            x (int): Position of the new rectangle on the X axis.
            y (int): Position of the new rectangle on the Y axis.
            id (int): Id number of the object.
        """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__ = id

    @property
    def width(self):
        """
        Getter for width property.

        Returns:
            Value of width private instance attribute.
        """

        return self.__width

    @width.setter
    def width(self, width):
        """
        Setter for width property.

        Args:
            width (int): Width of the new rectangle.
        """

        self.__width = width

    @property
    def height(self):
        """
        Getter for height property.

        Returns:
            Value of height private instanceattribute.
        """

        return self.__height

    @height.setter
    def height(self, height):
        """
        Setter for height property.

        Args:
            height (int): Height of the new rectangle.
        """

        self.__height = height

    @property
    def x(self):
        """
        Getter for x property.

        Returns:
            Value of x private instance attribute.
        """

        return self.__x

    @x.setter
    def x(self, x):
        """
        Setter for x property.

        Args:
            x (int): Position of the new rectangle on the X axis.
        """

        self.__x = x

    @property
    def y(self):
        """
        Getter for y property.

        Returns:
            Value of x private instance attribute.
        """

        return self.__y

    @y.setter
    def y(self, y):
        """
        Setter for y property.

        Args:
            y (int): Position of the new rectangle on the Y axis.
        """

        self.__y = y
