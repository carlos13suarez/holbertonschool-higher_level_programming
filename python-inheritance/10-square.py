#!/usr/bin/python3
"""
This module contains the class Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle class"""
    def __init__(self, size):
        """Instantiation with size

        Args:
            size (int): The size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size
