#!/usr/bin/python3
"""
Module contains the pascal_triangle function
"""


def pascal_triangle(n):
    """
    Function that returns a list of lists of integers representing the
    Pascal’s triangle of n

    Args:
        n (int): size of the pascal triangle

    Returns:
        An empty list if n <= 0, else the pascal triangle
    """
    pascal_list = []
    for i in range(n):
        row_builder = []
        for j in range(i+1):
            if j == 0 or j == i:
                row_builder.append(1)
            else:
                row_builder.append(prev_row[j] + prev_row[j-1])
        pascal_list.append(row_builder)
        prev_row = row_builder
    return pascal_list
