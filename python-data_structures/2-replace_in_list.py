#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    if (idx < 0) or (idx > (len(my_list) - 1)):
        return my_list
    for i, v in enumerate(my_list):
        if i == idx:
            my_list[idx] = element
    return my_list
