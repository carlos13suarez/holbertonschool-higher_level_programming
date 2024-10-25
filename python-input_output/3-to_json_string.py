#!/usr/bin/python3
"""
Module with a function that returns the JSON representation of an object
(string)
"""

import json


def to_json_string(my_obj):
    """
    Function that returns the JSON representation of an object (string)

    my_obj (string): the object whose JSON representation will be returned
    """
    return json.dumps(my_obj)
