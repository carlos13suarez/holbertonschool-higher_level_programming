#!/usr/bin/python3
"""
This module contains a that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    Function that appends a text file (UTF8) and returns the number of
    characters written

    Args:
        filename: file to append on
        text: text to append into the file
    """
    with open(filename, "a") as file:
        return file.write(text)
