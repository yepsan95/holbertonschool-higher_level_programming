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
        Raises:
            TypeError: If width or height is not an int.
            ValueError: If width or height are <= 0.
            TypeError: If x or y is not an int.
            ValueError: If x or y are < 0.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Getter for width property.

        Returns:
            Value of width private instance attribute.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width property.

        Args:
            value (int): Width of the new rectangle.
        """

        self.__width = value

    @property
    def height(self):
        """
        Getter for height property.

        Returns:
            Value of height private instanceattribute.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height property.

        Args:
            value (int): Height of the new rectangle.
        """

        self.__height = value

    @property
    def x(self):
        """
        Getter for x property.

        Returns:
            Value of x private instance attribute.
        """

        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x property.

        Args:
            value (int): Position of the new rectangle on the X axis.
        """

        self.__x = value

    @property
    def y(self):
        """
        Getter for y property.

        Returns:
            Value of x private instance attribute.
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y property.

        Args:
            value (int): Position of the new rectangle on the Y axis.
        """

        self.__y = value
