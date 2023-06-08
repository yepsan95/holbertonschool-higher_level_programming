#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    best = 0
    for k in a_dictionary:
        if a_dictionary[k] > best:
            best = a_dictionary[k]
            best_key = k
    return best_key
