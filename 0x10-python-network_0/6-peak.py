#!/usr/bin/python3
"""
Implementation function
"""


def find_peak(list_of_integers):
    """
    finds a peak in a list of unsorted integers.
    """
    L = len(list_of_integers)
    M = L // 2
    if not list_of_integers:
        return
    if L == 1 or L == 2:
        return max(list_of_integers)
    if (list_of_integers[M - 1] < list_of_integers[M] and
            list_of_integers[M] > list_of_integers[M + 1]):
        return list_of_integers[M]
    elif list_of_integers[M] < list_of_integers[M - 1]:
        return find_peak(list_of_integers[:M])
    else:
        return find_peak(list_of_integers[M + 1:])
