"""
This module defines the `add_integer` function, which adds two numbers.

The arguments must be integers or floats. If float, it'll be casted to int.
If not any of these, it raises a TypeError.

Functions:
    add_integr(a, b=98)
"""


def add_integer(a, b=98):
    """
    Return the sum of two decimal numbers in binary digits.
    Floats are cast to int.

        Parameters:
            a (int, float): A number
            b (int, float): A number

        Returns:
            a + b (int): Sum of the numbers a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
