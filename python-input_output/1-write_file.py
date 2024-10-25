#!/usr/bin/python3
"""
This module contains a function to write a text file UTF8
"""


def write_file(filename="", text=""):
    """
    Function that write a text file (UTF8) and returns the number of
    characters written

    Args:
        filename: file to write on
        text: text to write into the file
    """
    with open(filename, "w") as file:
        return file.write(text)
