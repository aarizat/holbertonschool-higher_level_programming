#!/usr/bin/python3
"""
Define function to insert a line of text to a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
     Inserts a line of text to a file, after each line containing a specific
     string.

    Args:
        filename(str): Name of the text file
        search_string(str): String to find.
        new_string(str): String to apend.
    Return:
       Nothing.
    """
    if filename:
        with open(filename, mode='r+', encoding='utf-8') as data:
            lines = data.readlines()
            for ix, line in enumerate(lines):
                if search_string in line:
                    lines[ix] = lines[ix] + new_string
            data.seek(0)
            for line in lines:
                data.write(line)
