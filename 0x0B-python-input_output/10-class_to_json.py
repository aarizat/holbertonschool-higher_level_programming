#!/usr/bin/python3
"""
Define function that returns the dictionary description with simple data
structure (list, dictionary, string, integer and boolean) for JSON
serialization of an object.
"""


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure.

    Args:
        obj(object): Python object.
    Return:
       dict with the information about the object.
    """
    return obj.__dict__
