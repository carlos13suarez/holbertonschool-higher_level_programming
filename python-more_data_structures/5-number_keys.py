#!/usr/bin/python3


def number_keys(a_dictionary):
    num_k = 0
    for i, v in enumerate(a_dictionary):
        num_k = i + 1
    return num_k
