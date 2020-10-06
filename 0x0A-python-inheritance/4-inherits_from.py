#!/usr/bin/python3
"""
 function that returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited from
    specified class.

    Args:
        obj (object): object to check
        a_class (class): base class

    Return:
        Boolean (True or False): True if the object is an instance of a class
        Fase otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
