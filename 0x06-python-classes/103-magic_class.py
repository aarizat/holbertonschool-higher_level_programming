#!/usr/bin/python3
"""
Define magic class
"""

import dis
import math


class MagicClass:
    """
    Magic class from bytecode python
    """
    def __init__(self, radius):
        """ Initialize attributes
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius
        return

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
dis.dis(MagicClass)
