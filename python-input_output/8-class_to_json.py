#!/usr/bin/python3
"""
Module contains a function that returns the dictionary description
for JSON serialization of an object:
"""


def class_to_json(obj):
    """
    Function that returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean) for JSON
    serialization of an object.

    Args:
        obj: instance of list, dictionary, string, integer and boolean
        class.
    """
    return obj.__dict__
