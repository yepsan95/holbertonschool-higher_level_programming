#!/usr/bin/python3
"""
This module defines a class 'Rectangle'.
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle that inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
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

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

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

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

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

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
        Getter for y property.

        Returns:
            Value of y private instance attribute.
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y property.

        Args:
            value (int): Position of the new rectangle on the Y axis.
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        Returns the area value of the Rectangle instance.

        Returns:
            Area of the Rectangle instance.
        """

        return self.__width * self.__height

    def display(self):
        """
        Prints the Rectangle instance in stdout with the character '#'.:w
        """

        for n in range(self.__y):
            print()
        for i in range(self.__height):
            for m in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute.

        Args:
            *args (ints): A list of the arguments passed to the function
            **kwargs (dict): A dictionary of the arguments passed
            to the function as key/values.
        """

        if args and len(args) != 0:
            if args[0] is None:
                self.__init__(self.width, self.height, self.x, self.y)
            try:
                self.id = args[0]
            except IndexError:
                return
            try:
                self.width = args[1]
            except IndexError:
                return
            try:
                self.height = args[2]
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
            if kwargs['id'] is None:
                self.__init__(self.width, self.height, self.x, self.y)
            try:
                self.id = kwargs['id']
            except KeyError:
                pass
            try:
                self.width = kwargs['width']
            except KeyError:
                pass
            try:
                self.height = kwargs['height']
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

    def __str__(self):
        """
        Returns a human-readable string representation of an object.

        Returns:
            Human-readable string representation of an object.
        """

        string = f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y}"
        string += f"{ - self.width}/{self.height}"

        return string
