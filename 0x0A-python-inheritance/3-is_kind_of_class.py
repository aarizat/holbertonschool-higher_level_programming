#!/usr/bin/python3
"""
Function to Check  if an object is an is instance of, or if the oject
is an instance of a class that inherits from.
"""


def is_kind_of_class(obj, a_class):
    """
    Check  if an object is an is instance of, or if the oject
    is an instance of a class that inherits from.

    Args:
        obj (object): obj to check
        a_class (class): base class

    Return:
        Boolean (True or False): True if the object is a instance, Otherwise
        False.
    """
    return isinstance(obj, a_class)
