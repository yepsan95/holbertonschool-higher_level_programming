#!/usr/bin/python3
"""
This module defines the class 'Base'.
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the  JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances who inherits Base.
        """

        filename = cls.__name__ + ".json"
        with open(filename, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_dicts = [e.to_dictionary() for e in list_objs]
                json_file.write(Base.to_json_string(list_dicts))
