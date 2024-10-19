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
        """Validates value is a positive integer number"""
        if isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
