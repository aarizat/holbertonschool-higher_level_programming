#!/usr/bin/python3
"""
Function to check if an obj is an instance from one.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is instance from other.

    Args:
        obj (object): object to check
        a_class (class): base class.

    Return:
        Boolean (True or false) : True if obj is instance from a_class, false
        otherwise.
    """
    return type(obj) is a_class
