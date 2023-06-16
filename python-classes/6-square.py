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
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter 'size' method.
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

    @property
    def position(self):
        """Getter 'position' method.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) is False or len(value) != 2 or
                type(value[0]) is not int or type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Class 'area' method. Returns the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Class 'my_print' method. Prints the square with the character '#'
        """
        if self.__size == 0:
            print()
        else:
            if self.__position[1] <= 0:
                for y in range(0, self.__position[1], -1):
                    print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
