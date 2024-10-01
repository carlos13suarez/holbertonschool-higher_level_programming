#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    columns = len(matrix[0])
    squared_matrix = [[0 for x in range(columns)] for x in range(rows)]
    for i in range(rows):
        for j in range(columns):
            squared_matrix[i][j] = matrix[i][j]**2
    return squared_matrix
