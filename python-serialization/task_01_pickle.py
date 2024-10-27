#!/usr/bin/python3
"""
Module contains a CustomObject that contains methods to serialize and
deserialize through pickle
"""

import pickle


class CustomObject:
    """Custom Object class"""

    def __init__(self, name, age, is_student):
        """Constructor method"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Method to display the instance attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Using the pickle module, it will serialize the current instance
        of the object and save it to the provided filename.
        """
        try:
            if not filename:
                return None
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Using the pickle module, it will load and return an instance
        of the CustomObject from the provided filename.
        """
        try:
            with open(filename, 'rb') as file:
                data = pickle.load(file)
                return data
        except Exception:
            return None
