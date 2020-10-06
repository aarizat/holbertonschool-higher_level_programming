#!/usr/bin/python3
"""
Fuction to add attributes
"""


def add_attribute(obj, name, value):
    """
    Add an attribute to object if it's possible.

    Args:
       obj (object): object
       name (str): name of the attribute to add to object.
       value (str): value to set in the attribute.

    Return:
       nothing.
    """
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    obj.__dict__[name] = value
