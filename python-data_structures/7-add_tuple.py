#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)

    if len(list_a) == 1:
        list_a.append(0)
    if len(list_a) == 0:
        list_a.append(0)
        list_a.append(0)

    if len(list_b) == 1:
        list_b.append(0)
    if len(list_b) == 0:
        list_b.append(0)
        list_b.append(0)

    addition = []
    for i in range(2):
        addition.append(list_a[i] + list_b[i])
    addition = tuple(addition)
    return addition
