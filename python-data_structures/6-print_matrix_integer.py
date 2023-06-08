#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for l in matrix:
        for i in l:
            final = " "
            if i == l[len(l) - 1]:
                final = "\n"
            print("{}".format(i), end=final)
