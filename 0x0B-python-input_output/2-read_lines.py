#!/usr/bin/python3
"""
Define a function that prints n lines of a text file.
"""


def read_lines(filename="", nb_lines=0):
    """
    Read n lines from a text file and print them to stdout.

    Args:
        filename (str): name of the text file.
        nb_lines (int): number of lines to read, by default is zero.
    Return:
        nothing.
    """
    if filename:
        with open(filename, mode='r', encoding='utf-8') as data:
            if nb_lines <= 0:
                print(data.read(), end='')
            else:
                for _ in range(nb_lines):
                    print(data.readline(), end='')
