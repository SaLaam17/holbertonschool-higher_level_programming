#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Return a new matrix where div divides all elements of the given matrix.

    Args:
        matrix: The matrix to divide.
        div: The number to divide the matrix elements by.

    Returns:
        A new matrix with elements divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows of the matrix are not of the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is zero.
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError(
            "matrix must be a matrix(list of lists) of integers/floats")

    if not all(isinstance(element, (int, float)) for row in matrix
               for element in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = list(
        map(lambda row: list(map(lambda x: round(x / div, 2), row)), matrix))
    return new_matrix
