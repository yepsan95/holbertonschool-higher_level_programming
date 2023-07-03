#!/usr/bin/python3
"""
This module defines the class 'Base'.
"""
import json
import os


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

    @classmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.

        Args:
            json_string (str): JSON string representation of a list of dicts.
        Returns:
            A Python list converted from json_string.
        """

        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns a new instance with all attributes already set.

        Args:
            dictionary (dict): A dictionary of attributes for the new instance.
        Returns:
            A new class instance.
        """

        if dictionary is not None and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a JSON file.

        Returns:
            If the JSON file doesn't exist - An empty list.
            Otherwise - A list of instances.
        """

        filename = cls.__name__ + ".json"
        json_string = ""
        result = []

        if os.path.exists("./{:s}".format(filename)):
            with open(filename, "r", encoding="utf-8") as json_file:
                json_string = json_file.read()

            list_of instances = cls.from_json_string(json_string)
            for instance in list_of_instances:
                result.append(cls.create(**instance))

        return result
