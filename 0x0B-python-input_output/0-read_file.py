#!/usr/bin/python3
"""
Define a function to read and print the content of a text file.
"""


def read_file(filename=""):
    """
    Read a text file and print its content on the stdout

    Args:
       filename (str): Path of the text file.

    Return:
        nothing.
    """
    if filename:
        with open(filename, mode='r', encoding="utf-8") as data:
            print(data.read(), end='')
