#!/usr/bin/python3
"""
This module defines the class 'Base'.
"""


class Base:
    """
    The base class for all other classes in the project.

    Attributes:
        __nb_objects (int): The number of instances of 'Base'.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of 'Base'.

        Args:
            id (int): the id number of the new instance.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
