#!/usr/bin/python3
"""
Define Base class.
"""
import json
import os


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

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation.

        Args:
             list_objs (JSON object): JSON representation of list_objs.
        """
        filename = cls.__name__ + '.json'
        list_dict = [d.to_dictionary() for d in list_objs]
        objs = cls.to_json_string(list_dict)
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write(objs)

    @staticmethod
    def from_json_string(json_string):
        """ list of the JSON string representation

        Args:
            json_string (str): string representing a list of dictionaries
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create objects.

        Returns:
            [object]: instance object.
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Read json string from a file.
        """
        obj_insts = []
        filename = cls.__name__ + '.json'
        if not os.path.isfile(filename):
            return obj_insts
        with open(filename, mode='r', encoding='utf-8') as f:
            list_dicts = cls.from_json_string(f.read())
            for d in list_dicts:
                obj_insts.append(cls.create(**d))
            return obj_insts

    def save_to_file_csv(cls, list_objs): and def load_from_file_csv(cls):
        pass

