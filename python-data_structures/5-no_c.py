#!/usr/bin/python3


def no_c(my_string):
    cp_str = my_string
    cp_str = cp_str.translate({ord('c'): None})
    cp_str = cp_str.translate({ord('C'): None})
    return cp_str
