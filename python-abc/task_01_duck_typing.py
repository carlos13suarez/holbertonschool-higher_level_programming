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

    def __init__(self, radius=0):
        """Instantiation with radius

        Args:
            radius (int): The radius of the circle
        """
        self._radius = radius

    def area(self):
        """Returns the area of a circle"""
        return pi * self._radius * self._radius

    def perimeter(self):
        """Returns the perimeter of a circle"""
        return 2 * pi * self._radius


class Rectangle(Shape):
    """Rectangle class that inherits from Shape abstract class"""

    def __init__(self, width=0, height=0):
        """Instantiation with width and height

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
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
