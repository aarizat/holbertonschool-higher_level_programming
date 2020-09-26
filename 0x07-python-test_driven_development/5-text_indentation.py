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
    if "?" in text or "." in text or ":" in text:
        ix_prev = 0
        for ix, ch in enumerate(text):
            if ch in (".", "?", ":"):
                sentence = text[ix_prev:ix+1].split("\n")
                for s in sentence:
                    print(s.strip(" "))
                print("")
                ix_prev = ix + 1
                continue
        print(text[ix_prev:].strip(" "), end="")
    else:
        print(text.strip(" "), end="")
