#!/usr/bin/python3
"""
Define student class
"""


class Student:
    """
    Class student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize object attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Return a dictionary representation of a Student instance.
        """
        return self.__dict__
