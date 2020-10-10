#!/usr/bin/python3
"""
Define Base class.
"""
import json


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize class Base.

        Args:
            id (int): integer number. Default to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            [str]: Json representation.
        """
        if not list_dictionaries:
            return json.dumps(list())
        return json.dumps(list_dictionaries)

