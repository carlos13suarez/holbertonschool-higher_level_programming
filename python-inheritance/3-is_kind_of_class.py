#!/usr/bin/python3
"""
This module contains a function that returns True if the object is an
instance of, or if the object is an instance of a class that inherited from,
the specified class; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Description: Function that checks if the object is an instance of a class

    Parameters:
        obj: an object
        a_class: a class

    Returns:
        True if the object is an instance of, or if the object is an instance
        of a class that inherited from, the specified class.
        Otherwise False
    """
    return isinstance(obj, a_class)