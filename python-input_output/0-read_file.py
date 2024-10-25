#!/usr/bin/python3
"""
This module contains a function to read a text file UTF8
"""

def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename: file to read and print its content
    """
    with open(filename) as file:
        content = file.read()
        print(content, end="")
