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

    def integer_validator(self, name, value):
        """Validates value is a positive integer number"""
        if isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Circle(Shape):
    """Circle class that inherits from Shape abstract class"""
    def __init__(self, radius):
        """Circle construct"""
        self.integer_validator("radius", radius)
        self.radius = radius

    def area(self):
        """Returns the area of a circle"""
        return 3.14 * (self.radius * self.radius)

    def perimeter(self):
        """Returns the perimeter of a circle"""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Rectangle class that inherits from Shape abstract class"""
    def __init__(self, width, height):
        """Rectancle construct"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of a rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Function to print the area and the perimeter of a shape

    Arguments:
        shape (Shape class): shape with the methods area() and perimeter()
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
