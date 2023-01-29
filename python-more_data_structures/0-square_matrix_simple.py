#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_square = []
    for x in range(0, len(matrix)):
        square = [y*y for y in matrix[x]]
        new_square.append(square)
    return (new_square)
