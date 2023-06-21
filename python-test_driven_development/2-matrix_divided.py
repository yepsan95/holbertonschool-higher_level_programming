#!/usr/bin/python3
"""
This module defines the function matrix_divided() that divides
all the elements of a matrix (list of lists) by a number.
The DocTest file for this module is in the 'tests' directory.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.
    All the elements of the matrix should be either integers or floats.
    Returns a new matrix.
    """
    type_error = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(type_error)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    if type(matrix[0]) is not list:
        raise TypeError(type_error)
    list_len = len(matrix[0])
    for i in range(len(matrix)):
        if list_len != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        list_len = len(matrix[i])
        new_matrix.append([])
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) is not int and \
                    type(matrix[i][j]) is not float:
                raise TypeError(type_error)
            new_matrix[i].append(round(matrix[i][j] / div, 2))

    return new_matrix
