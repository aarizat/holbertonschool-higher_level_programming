#!/usr/bin/python3
"""
Function to divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divide a matrix by a number.

    Args:
        matrix (list): list of list with numbers.
        div (float or int): number to divide each element of the matrix.

    Return:
       new_matrix (list): list of list with all elements of matrix divide by div
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    len_row = len(matrix[0])
    for i in range(len(matrix) - 1):
        if len_row != len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not div:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(n/div, 2) for n in row] for row in matrix]
    return new_matrix
