#!/usr/bin/python3
"""This module defines empty class Square that defines a square"""


class Square:
    """Empty class that defines a Square"""
    def __init__(self, size=0):
        """Instation method: create square with a given size attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
