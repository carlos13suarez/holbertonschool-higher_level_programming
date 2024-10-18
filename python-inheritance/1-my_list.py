#!/usr/bin/python3
"""
This module contains the class MyList
"""


class MyList(list):
    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
