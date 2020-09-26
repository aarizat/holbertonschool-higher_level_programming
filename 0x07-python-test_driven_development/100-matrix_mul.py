#!/usr/bin/python3
"""
Function to multply two matrix.
"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list): list of lists.
        m_b (list): list of lists.

    Return:
        r (list): list of lists.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
    if not len(m_a) or not len(m_a[0]):
        raise ValueError("m_a can't be empty")
    if not len(m_b) or not len(m_b[0]):
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    len_row_ma = len(m_a[0])
    for i in range(len(m_a) - 1):
        if len_row_ma != len(m_a[i+1]):
            raise TypeError("each row of m_a must be of the same size")
    len_row_mb = len(m_b[0])
    for i in range(len(m_b) - 1):
        if len_row_mb != len(m_b[i+1]):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    r = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                r[i][j] += m_a[i][k] * m_b[k][j]
    return r
