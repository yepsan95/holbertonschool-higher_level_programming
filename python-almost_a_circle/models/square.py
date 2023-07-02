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

    @property
    def size(self):
        """
        Getter/setter for the size of the Square.
        """

        return self.width

    @size.setter
    def size(self, value):

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute.

        Args:
            *args (ints): A list of the arguments passed to the function
            **kwargs (dict): A dictionary of the arguments passed
            to the function as key/values.
        """
        if args and len(args) != 0:
            try:
                if args[0] is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    self.id = args[0]
            except IndexError:
                return
            try:
                self.size = args[1]
            except IndexError:
                return
            try:
                self.x = args[3]
            except IndexError:
                return
            try:
                self.y = args[4]
            except IndexError:
                return

        elif kwargs and len(kwargs) != 0:
            try:
                if kwargs['id'] is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    self.id = kwargs['id']
            except KeyError:
                pass
            try:
                self.size = kwargs['size']
            except KeyError:
                pass
            try:
                self.x = kwargs['x']
            except KeyError:
                pass
            try:
                self.y = kwargs['y']
            except KeyError:
                pass

    def to_dictionary(self):
        """
        Returns a dictionary representation of a Square.

        Returns:
            Dictionary representation of a Square.
        """

        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y,
                }

    def __str__(self):
        """
        Returns a human-readable string representation of a square.

        Returns:
            Human-readable string representation of a square.
        """

        str = f"[{self.__class__.__name__}] "
        str += f"({self.id}) {self.x}/{self.y} - {self.width}"

        return str
