#!/usr/bin/python3
"""
Define a function to count the number of lines of a file.
"""


def number_of_lines(filename=""):
    """
    Count the number of lines of a file.

    Args:
       filename (str): file name.

    Return:
       number_lines (int): number of lines of filename.
    """
    number_lines = 0
    if filename:
        with open(filename, mode='r', encoding='utf-8') as data:
            for _ in data:
                number_lines += 1
        return number_lines
