#!/usr/bin/python3
"""
This module contains the class Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""
    def __init__(self, width, height):
        """Instantiation with width and height

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """String representation of Rectangle object"""
        return f"[Rectangle] {self.__width}/{self.__height}"
