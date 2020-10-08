#!/usr/bin/python3
"""
Define function that writes an Object to a text file, using a JSON
representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation.

    Args:
        my_obj(object): Python object to serielize.
        filename(str): File name to write the serialized object.
    Return:
        Nothing.
    """
    if filename:
        with open(filename, mode='w', encoding='utf-8') as data:
            data.write(json.dumps(my_obj))
