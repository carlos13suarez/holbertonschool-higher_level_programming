#!/usr/bin/python3
"""
This module contains the class MyList
"""


class MyList(list):
    """Class MyList that inherits from list class"""
    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
