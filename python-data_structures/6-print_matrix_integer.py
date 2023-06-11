#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for list in matrix:
        final = " "
        for i in list:
            if i == list[-1]:
                final = ""
            print("{:d}".format(i), end=final)
        print("")
