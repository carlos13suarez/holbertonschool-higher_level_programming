#!/usr/bin/python3
"""
Module that contains a function that writes an Object to a text file, using a
JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file, using a JSON representation

    Args:
        my_obj (python file): object whose JSON representation will be written
        into the filename
        filename: file where to store the object's JSON representation
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
