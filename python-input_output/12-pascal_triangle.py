#!/usr/bin/python3
"""
This module defines a function 'pascal_triangle()'.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal’s triangle of n.

    Args:
        n (int): the height of the Pascal's triangle.
    Returns:
        A list of lists of integers representing the Pascal's triangle.
    """

    if n <= 0:
        return []

    pascal = [[1]]

    i = 1
    while i < n:
        pascal.append([])
        j = 0
        while j <= i:
            if j - 1 >= 0 and j < len(pascal[i - 1]):
                number = pascal[i - 1][j - 1] + pascal[i - 1][j]
            else:
                number = 1
            pascal[i].append(number)
            j += 1
        i += 1

    return pascal
