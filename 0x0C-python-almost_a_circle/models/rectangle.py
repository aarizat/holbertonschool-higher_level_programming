#!/usr/bin/python3
"""
Define Rectangle class.
"""


class Rectangle(Base):
    """Rectangle class

    Args:
        Base (cls): base class.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize class attributes.

        Args:
            width (int): with of the rectangle.
            height (int):  height of the rectangle.
            x (int): integer number.
            y (int): integer number.
            id (int): integer number. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        """Retrieve with argument.

        Returns:
            [int]: width of the rectangle.
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """Set the value to width

        Args:
            value (int): value to set to width
        """
        self.__width = value
        
    @property
    def height(self):
        """Retrieve height attribute.

        Returns:
            [int]: height value
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """Set the value to height

        Args:
            value (int): Value to assign to height.
        """
        self.__height = value

    @property
    def x(self):
        """Retrieve "x" attribute.

        Returns:
            [int]: the "x" value.
        """
        return self.__x
    
    @x.setter
    def x(self, value):
        """Set the value to "x".

        Args:
            value (int): The "x" value.
        """
        self.__x = value

    @property
    def y(self):
        """Retrieve "y" attribute.

        Returns:
            [int]: The "y" value
        """
        return self.__y
    
    @y.setter
    def y(self, value):
        """Set "y" value.

        Args:
            value (int): the value to assign to "y".
        """
        self.__y = value