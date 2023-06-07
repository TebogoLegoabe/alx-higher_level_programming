#!/usr/bin/python3
"""
    divides all elements of a matrix.

    Args:
        matrix: can be integer or float
        div: divider

    Raises:
        TypeError: when matrix is not an integer/float
        TypeError: when row of matrix do not have same size
        TypeError: when div is not integer/float
        ZeroDivisionError: when div is zero

"""

def matrix_divided(matrix, div):
    """Divides all numbers of matrix"""
    
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_size = set(len(row) for row in matrix)
    if len(row_size) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return (new_matrix)
