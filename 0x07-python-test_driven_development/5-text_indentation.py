#!/usr/bin/python3
"""
Print a string on the stdout.
"""


def text_indentation(text):
    """
    Split a text where is found the delimiters ., :, and ?

    Args:
        text (str): text to split.

    Return:
        print on the stdout.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    nb_prev = nb_curr = 0
    for ch in text:
        nb_curr += 1
        if ch in (".", "?", ":"):
            line = text[nb_prev:nb_curr+1]
            c = 0
            for i in line:
                if i != " ":
                    break
                c += 1
            b = 1
            for j in line[::-1]:
                if j != " ":
                    break
                b += 1
            print(line[c:-b+1])
            print("")
            nb_prev = nb_curr
