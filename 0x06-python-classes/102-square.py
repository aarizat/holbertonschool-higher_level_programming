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
        if not isinstance(size, (int, float)):
            raise TypeError("size must be an number")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be an number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def __eq__(self, square):
        return self.area() == square.area()

    def __lt__(self, square):
        return self.area() < square.area()

    def __le__(self, square):
        return self.area() <= square.area()

    def __ne__(self, square):
        return self.area() != square.area()

    def __gt__(self, square):
        return self.area() > square.area()

    def __ge__(self, square):
        return self.area() => square.area()
