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

    def to_json(self, attrs=None):
        """
        Return a dictionary representation of a Student instance.
        """
        if isinstance(attrs, list):
            type_str = [isinstance(attr, str) for attr in attrs]
            if all(type_str):
                _dict = {}
                for key in attrs:
                    if key in self.__dict__:
                        _dict[key] = self.__dict__[key]
                return _dict
        return self.__dict__
