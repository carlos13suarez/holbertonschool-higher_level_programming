#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_list = list()
    for i, v in enumerate(my_list):
        if v == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[i])
    return new_list
