#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    i = 0
    while i < len(matrix):
        new_matrix.append([])
        j = 0
        while j < len(matrix[i]):
            new_matrix[i].append(matrix[i][j] ** 2)
            j = j + 1
        i = i + 1
    return new_matrix
