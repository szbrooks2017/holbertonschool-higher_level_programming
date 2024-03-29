#!/usr/bin/python3
""" matrix divides by div """


def matrix_divided(matrix, div):
    """
    -matrix must be a list/int/float
    -each row must be the same size
    -div must be int/float
    -div can't be 0
    -round elements by 2
    -return new matrix
    """
    # check div type and isn't 0
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # check matrix type
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of\
         integers/floats")

    # check row type then row length
    row_length = len(matrix[0])
    for row in matrix:
        if not isinstance(row, (int, float, list)):
            raise TypeError("matrix must be a matrix (list of lists) of\
             integers/floats")
    for row in range(len(matrix)):
        if row_length != len(matrix[row]):
            raise TypeError("Each row of the matrix must have the same size")
    divided = [[round(element / div, 2) for element in row] for row in matrix]
    return divided
