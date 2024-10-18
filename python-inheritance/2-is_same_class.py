#!/usr/bin/python3
"""
This module has a function that returns True if the object is exactly an
instance of the specified class; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Function that returns True if the object is exactly an instance of the
    specified class; otherwise False.
    """
    if type(obj) == a_class:
        return True
    return False
