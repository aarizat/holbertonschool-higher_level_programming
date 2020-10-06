#!/usr/bin/python3
"""
Define a customize integer class
"""


class MyInt(int):
    """
    Customized integer class
    """
    def __eq__(self, other):
        """
        Return false when two int object are diferents.
        """
        return False

    def __ne__(self, other):
        """
        Return True when two int objects are the same.
        """
        return True
