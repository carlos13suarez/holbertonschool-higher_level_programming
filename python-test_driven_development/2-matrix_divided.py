#!/usr/bin/python3
"""
Module that defines the matrix_divided function that divides the elements of
a matrix by a given number.

Functions:
    matrixdivided(matrix, div)
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Arguments:
        matrix: The matrix whose elements will be divided.
        div: The divisor that'll divide the elements of the matrix.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix is not of the same size.
        TypeError: If div is not a number
        ZeroDivisionError: If div is zero.

        Returns:
            A new matrix with each element divided by div, rounded to 2\
                    decimal places
    """
    # Validate matrix is a list per se
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    # Validate each element of the matrix is a list (list of lists)
    if not all(isinstance(ele, list) for ele in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    # Validate each element of the matrix's rows is either an int or a float
    # (list of lists of integers or floats)
    if not all(isinstance(ele, (int, float)) for row in matrix for ele in
               row):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    # Validate each row of the matrix has the same size
    rows_size = len(matrix[0])
    for row in matrix:
        if len(row) != rows_size:
            raise TypeError("Each row of the matrix must have the same size")

    # Validate div is int or float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Validate div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    rows = len(matrix)
    columns = len(matrix[0])
    div_matrix = [[0 for x in range(columns)] for x in range(rows)]
    for i in range(rows):
        for j in range(columns):
            div_matrix[i][j] = round(matrix[i][j]/div, 2)
    return div_matrix
