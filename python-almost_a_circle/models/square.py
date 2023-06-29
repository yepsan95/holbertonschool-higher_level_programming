#!/usr/bin/python3
"""
This module defines a class 'Square' that inherits from 'Rectangle'.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines a square. Inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new instance of Rectangle.

        Args:
            size (int): Size of the new rectangle.
            x (int): Position of the new rectangle on the X axis.
            y (int): Position of the new rectangle on the Y axis.
            id (int): Id number of the object.
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a human-readable string representation of a square.

        Returns:
            Human-readable string representation of a square.
        """

        return f"[{self.__class__.__name__}] ({id}) {x}/{y} - {width}"
