#!/usr/bin/python3
"""
Pascal triangle.
"""


def pascal_triangle(n):
    """
    Pascal triangle.
    """
    if n <= 0:
        return []
    p_t = [[1]]
    for i in range(2, n+1):
        p_t.append([sum(p_t[i-2][0:1])])
        for k in range(0, i-1):
            p_t[i-1].append(sum(p_t[i-2][k:k+2]))
    return p_t
