#!/usr/bin/python3
"""
This module defines the text_indentation function

Functions:
    text_indentation(text): prints a text with 2 new lines after each of these
    characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Arguments:
        text: String to print.

    Raises:
        TypeError: If text is not a string.

    Returns:
        Nothing.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    newline_flag = False
    for c in text:
        if c in ".?:":
            print(c, end="")
            print("\n")
            newline_flag = True
        elif newline_flag and c == " ":
            continue
        else:
            print(c, end="")
            newline_flag = False
