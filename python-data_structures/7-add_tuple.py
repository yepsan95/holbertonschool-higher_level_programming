#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    b = 0
    if len(tuple_a) > 0:
        a = a + tuple_a[0]
    if len(tuple_b) > 0:
        a = a + tuple_b[0]
    if len(tuple_a) > 1:
        b = b + tuple_a[1]
    if len(tuple_b) > 1:
        b = b + tuple_b[1]
    tuple = (a, b)

    return tuple
