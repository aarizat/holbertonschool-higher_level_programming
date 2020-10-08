#!/usr/bin/python3
"""
Define a function that returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object.

    Args:
       my_object (list, dict, int, float, str, Bool, None): Object to
       serialize.

    Return:
       The object serialized.
    """
    return json.dumps(my_obj)
