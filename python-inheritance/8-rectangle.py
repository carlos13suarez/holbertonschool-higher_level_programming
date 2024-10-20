#!/usr/bin/python3
"""
This module contains the class Base Geometry
"""


class BaseGeometry:
    """
    Class BaseGeometry
    """
    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value is a positive integer number

        Arguments:
            name (str): The name of the value
            value (int): The value to be validated
        
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Class Rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
