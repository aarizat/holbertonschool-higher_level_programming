#!/usr/bin/python3
"""
Print a square made up # character on the stdout.
"""


def print_square(size):
    """
    Print a square on the stdout.

    Args:
       size (int): size of the square.

    Return:
       nothing: print on the screen a square made up by # character.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print("#" * size)
