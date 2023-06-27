#!/usr/bin/python3
"""Module that defines a square.
"""


class Square:
    """Class square that defines a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Constructor '__init__' method.

        Args:
            __size (int): Size of the square.
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter 'size' property getter.

        Returns:
            Value of private instance attribute size.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """Class 'size' property setter. Returns the size of the square.

        Args:
            value (int): size of the square.
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter 'position' method.

        Returns:
            Value of private instance attribute position.
        """

        return self.__position

    @position.setter
    def position(self, value):
        """Setter 'position' method.

        Args:
            value (int): Position of the square.
        """
        if type(value) is not tuple or len(value) != 2 \
                or type(value[0]) is not int \
                or type(value[1]) is not int \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Class 'area' method. Returns the area of the square.

        Returns:
            Area of the square.
        """

        return self.__size ** 2

    def my_print(self):
        """Class 'my_print' method. Prints the square with the character '#'.
        """

        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
