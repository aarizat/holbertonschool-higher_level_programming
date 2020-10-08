#!/usr/bin/python3
"""
Define a function that returns an object (Python data structure) represented
by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Return an object represented by a JSON string.

    Args:
       my_str (str): string that represent an object python.

    Return:
       Object represented by a JSON string.
    """
    return json.loads(my_str)
