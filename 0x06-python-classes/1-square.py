#!/usr/bin/python3
"""
Define a square class
"""


class Square:
    """Create an instance of a square object

    Attributes:
        size: number.
    """
    def __init__(self, size):
        """ Initialize square object

        Args:
            size (float or int): side of the square
       """
        self.__size = size
