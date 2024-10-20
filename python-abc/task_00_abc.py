#!/usr/bin/python3
"""
This module contains the Animal abstract class using the ABC package,and two
subclasess, namely, Dog and Cat
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract Animal class"""
    @abstractmethod
    def sound(self):
        """Abstract method class that must be overriden in its subclasses"""
        pass


class Dog(Animal):
    """Dog subclass of Animal class"""
    def sound(self):
        """Implementation of Animal abstract method sound"""
        return "Bark"


class Cat(Animal):
    """Cat subclass of Animal class"""
    def sound(self):
        """Implementation of Animal abstract method sound"""
        return "Meow"
