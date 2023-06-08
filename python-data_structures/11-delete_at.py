#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    new_list = my_list.copy()
    my_list.clear()
    i = 0
    while i < len(new_list):
        if i != idx:
            my_list.append(new_list[i])
        i += 1
    return my_list
