#!/usr/bin/python3
"""
define function that creates an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”.

    Args:
       filename (str): name of the json file.
    Return:
       obj: Python object created from the json file.
    """
    if filename:
        with open(filename, mode='r', encoding='utf-8') as data:
            obj = json.loads(data.readline())
        return obj
