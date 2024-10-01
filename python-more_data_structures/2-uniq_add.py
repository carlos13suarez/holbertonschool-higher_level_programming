#!/usr/bin/python3


def uniq_add(my_list=[]):
    addition = 0
    for f in set(my_list):
        addition += int(f)
    return addition
