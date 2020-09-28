#!/usr/bin/python3
"""
Module to create a rectangle class.
"""


class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    """
    The instance of this class creates Rectangle objects.
    """

    def __init__(self, width=0, height=0):
        """Init rectangle objects"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            print(self.print_symbol * self.__width)
        print(self.print_symbol * self.__width, end="")
        return ""

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message every time that a rectangle object is eliminated"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare the area of two rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area() or rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Convert a rectangle to square"""
        return cls(size, size)
