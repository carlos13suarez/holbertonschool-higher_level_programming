#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if idx > (len(my_list) - 1) or idx < 0:
        return my_list
    for item, value in enumerate(my_list):
        if item == idx:
            del my_list[item]
            return my_list
