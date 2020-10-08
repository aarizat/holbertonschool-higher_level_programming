#!/usr/bin/python3
"""
Define a function that writes to text file.
"""


def write_file(filename="", text=""):
    """
    Write a string to text file.

    Args:
       filename (str): text file to write the string, if it doesn't exist, will
       be created.
    Return:
       nb_written (int): number of bytes written in the text file.
    """
    if filename:
        with open(filename, mode='w', encoding='utf-8') as data:
            nb_written = data.write(text)
        return nb_written
