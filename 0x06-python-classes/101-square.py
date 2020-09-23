#!/usr/bin/python3
"""
Define a square class
"""


class Square:
    """Create an instance of a square object

    Attributes:
        size: integer number
        position: tuple
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize square object

        Args:
            size (int): side of the square
            position (tuple): init position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (len(value) != 2 or not isinstance(value[0], int) or not
                isinstance(value[1], int) or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        if self.__size == 0:
            print("", end="")
        else:
            print("\n" * self.position[1], end="")
            for _ in range(self.__size - 1):
                print(" " * self.__position[0] + "#" * self.__size)
            print(" " * self.__position[0] + "#" * self.__size, end="")
        return ""
