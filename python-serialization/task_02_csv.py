#!/usr/bin/python3
"""
Module to convert csv file to json using serialization techniques
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Function that takes the CSV filename as its parameter and writes the
    JSON data to data.json.
    """
    try:
        with open(csv_filename, newline='') as csvfile, \
                open('data.json', 'w') as jsonfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)
            json.dump(data, jsonfile, indent=4)
        return True
    except Exception:
        return False
