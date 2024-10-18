#!/usr/bin/python3
"""
This module has a function that returns True if the object is exactly an
instance of the specified class; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Function that checks if an object is an instance of a given class.

    Paremeters:
        obj: an instance
        a_class: a class

    Returns: True if the object is exactly an instance of the specified class;
    otherwise False.
    """
    if type(obj) is a_class:
        return True
    return False
