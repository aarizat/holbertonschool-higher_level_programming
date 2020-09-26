#!/usr/bin/python3

"""
Multiply two matrices using numpy module.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list): list of lists.
        m_b (list) : list of lists.
    """
    return np.matmul(m_a, m_b)
