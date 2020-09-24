#!/usr/bin/python3
"""
Function to print on the stdout
"""


def say_my_name(first_name, last_name=""):
    """
    Print on the stdout a string.

    Args:
       first_name (str): name
       last_name (str): last name.

    Return:
       str: first_name and last_name concatenated.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
