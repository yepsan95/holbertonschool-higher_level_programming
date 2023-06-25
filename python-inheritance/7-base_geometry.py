#!/usr/bin/python3
"""
This modules defines a class 'BaseGeometry'.
"""


class BaseGeometry:
    """
    Class BaseGeometry.
    """
    def area(self):
        """
        Raises an exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if value is an integer and greater than 0.

        Args:
            name (str): name of the parameter.
            value (int): value of the parameter.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
