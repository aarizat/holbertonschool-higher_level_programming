#!/usr/bin/python3
"""
Define square class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    init square objects.
    """
    def __init__(self, size):
        """
        init attributes.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """"
        Return the area of a square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Printable square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
