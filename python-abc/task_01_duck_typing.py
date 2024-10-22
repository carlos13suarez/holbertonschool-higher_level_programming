#!/usr/bin/python3
"""
This module contains the Shape abstract class
and its subclasses Circle and Rectangle
"""


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Shape abstract class"""

    @abstractmethod
    def area(self):
        """Area abstract method that must be overridden"""
        pass

    @abstractmethod
    def perimeter(self):
        """Perimeter abstract method that must be overridden"""
        pass


class Circle(Shape):
    """Circle class that inherits from Shape abstract class"""

    def __init__(self, radius):
        """Instantiation with radius

        Args:
            radius (int): The radius of the circle
        """
        if isinstance(radius, bool):
            raise TypeError

        if not isinstance(radius, int):
            raise TypeError

        if radius <= 0:
            raise ValueError
        self._radius = radius

    def area(self):
        """Returns the area of a circle"""
        return pi * self._radius * self._radius

    def perimeter(self):
        """Returns the perimeter of a circle"""
        return 2 * pi * self._radius


class Rectangle(Shape):
    """Rectangle class that inherits from Shape abstract class"""

    def __init__(self, width, height):
        """Instantiation with width and height

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        if isinstance(width, bool):
            raise TypeError

        if not isinstance(width, int):
            raise TypeError

        if width <= 0:
            raise ValueError

        if isinstance(height, bool):
            raise TypeError

        if not isinstance(height, int):
            raise TypeError

        if height <= 0:
            raise ValueError
        self._width = width
        self._height = height

    def area(self):
        """Returns the area of a rectangle"""
        return self._width * self._height

    def perimeter(self):
        """Returns the perimeter of a rectangle"""
        return 2 * (self._width + self._height)


def shape_info(shape):
    """Function to print the area and the perimeter of a shape

    Arguments:
        shape (Shape class): shape with the methods area() and perimeter()
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
