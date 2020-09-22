#!/usr/bin/python3
"""
Define a square class
"""


class Square:
    """Create an instance of a square object

    Attributes:
        size: integer number
    """
    def __init__(self, size=0):
        """ Initialize square object

        Args:
            size (int): side of the square
       """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        return self.__size ** 2
