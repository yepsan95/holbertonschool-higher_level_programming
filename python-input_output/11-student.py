#!/usr/bin/python3
"""
This module defines a clas Student.
"""


class Student():
    """
    Defines a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes an instance of Student.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): If attrs is a list of strings,
            only attribute names contained in this list must be retrieved.

        Returns:
            Dictionary representation of the Student instance.
        """

        if (type(attrs) == list and
                all(type(e) == str for e in attrs)):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}

        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json (dict): The attributes to be setted to the Student instance.
            Each key will be the attribute name, and their respective values
            will be the values of the attributes.
        """

        for k, v in json.items():
            setattr(self, k, v)
