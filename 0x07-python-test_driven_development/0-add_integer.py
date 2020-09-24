#!/usr/bin/python3
"""
Define function for adding two numbers.
"""


def add_integer(a, b=98):
    """Add two integer numbers.

    Args:
        a (int): first integer number
        b (int): second integer number. By default b is iqual to 98.

    Return:
    int: The ineger sum of a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return a + b
