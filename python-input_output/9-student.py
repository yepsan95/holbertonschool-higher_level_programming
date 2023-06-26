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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            Dictionary representation of the Student instance.
        """

        return self.__dict__
