"""
Define square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize square class

        Args:
            size (int): value to square side.
            x (int): integer number.Defaults to 0.
            y (int): integer numer. Defaults to 0.
            id (int): integer number.Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Square representation.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """Retrieve the width value.

        Returns:
            [int]: Side of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """Set the values.

        Args:
            value (int): value to set to width and height.
        """
        self.width = value
        self.height = value
