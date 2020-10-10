#!/usr/bin/python3
"""
Define Rectangle class.
"""
from models.base import Base


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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area value of the Rectangle instance.

        Returns:
            [int]: Area of the rectangle.
        """
        return self.__height * self.__width

    def display(self):
        """Print in stdout the Rectangle instance with the # character.
        """
        rect_shape = []
        for _ in range(self.__y):
            print('')
        for _ in range(self.__height):
            rect_shape.append(' ' * self.__x + '#' * self.__width)
        print(*rect_shape, sep='\n')

    def __str__(self):
        """Return representation of a Rectangle instance.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """Update instance attributes.
        """
        attrs = ['id', 'width', 'height', 'x', 'y']
        if 0 < len(args) <= 5:
            for i in range(len(args)):
                super().__setattr__(attrs[i], args[i])
        else:
            for key in kwargs:
                super().__setattr__(key, kwargs[key])

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle
        """
        attrs_dict = {'id': self.id, 'width': self.width,
                      'height': self.height, 'x': self.x, 'y': self.y}
        return attrs_dict

        return a




