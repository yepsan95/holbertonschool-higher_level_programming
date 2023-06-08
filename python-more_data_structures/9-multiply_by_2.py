#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary.copy()
    for k in b_dictionary:
        b_dictionary[k] = b_dictionary[k] * 2
    return b_dictionary
