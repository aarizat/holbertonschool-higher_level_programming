#!/usr/bin/python3
"""
Module to create a rectangle class.
"""


class Rectangle:
    """
    The instance of this class creates Rectangle objects.
    """

    def __init__(self, width=0, height=0):
        """Init rectangle objects"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return widht value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of height to value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height to value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print the rectangle with # character"""
        if self.__height == 0 or self.__width == 0:
            return ""
        for _ in range(self.__height - 1):
            print('#' * self.__width)
        print('#' * self.__width, end="")
        return ""

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
