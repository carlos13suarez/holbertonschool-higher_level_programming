#!/usr/bin/python3
"""
Module contains Student class
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Constructor method
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public method that returns the dictionary description with
        simple data structure (list, dictionary, string, integer and
        boolean) for JSON serialization of an object.
        """
        try:
            if all(isinstance(elem, str) for elem in attrs):
                selected_attrs = {}
                for elem in attrs:
                    if elem in self.__dict__:
                        selected_attrs[elem] = self.__dict__[elem]
                return selected_attrs
        except Exception:
            return self.__dict__
