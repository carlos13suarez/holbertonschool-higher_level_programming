#!/usr/bin/python3
"""
This module contains a function that returns True
if the object is an instance of a class that inherited from a specified class;
otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Description: Function that checks if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class.

    Parameters:
        obj: an object
        a_class: a class

    Returns:
        True if the object is an instance of a class that inherited (directly
        or indirectly) from the specified class.
        Otherwise False.
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
