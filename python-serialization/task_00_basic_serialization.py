#!/usr/bin/python3
"""
Module contains two functions to serialize a Python dictionary to a
JSON file and deserialize the JSON file to recreate the Python Dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    with open(filename) as file:
        data = json.load(file)
        return data
