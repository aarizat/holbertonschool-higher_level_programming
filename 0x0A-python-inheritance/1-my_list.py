#!/usr/bin/python3
"""
Class inherits from list class.
"""


class MyList(list):
    """
    Class that inherits from list class.
    """
    def print_sorted(self):
        """
        Print a list object sorted.
        """
        sorted_list = sorted(self.copy())
        print(sorted_list)
