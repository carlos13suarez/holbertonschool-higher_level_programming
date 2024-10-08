#!/usr/bin/python3
"""
This module defines the function say_my_name().

Functions:
    say_my_name(first_name, last_name=""): prints My name is <first name>
    <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first name> <last name>'

    Arguments:
        first_name: string of the first name.
        last_name: string of the last name.

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.

    Returns:
        Nothing.
"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
