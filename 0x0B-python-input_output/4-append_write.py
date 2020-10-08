#!/usr/bin/python3
"""
Define a function to append a string at the end of a text file.
"""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file.

    Args:
       filename (str): name of the text file
       text (str): String to append.

    Return:
       nb_appended (int): number of bytes appended.
    """
    if filename:
        with open(filename, mode='a', encoding='utf-8') as data:
            nb_appended = data.write(text)
        return nb_appended
