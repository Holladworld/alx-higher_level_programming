#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda row: list(map(lambda new_matrix: new_matrix ** 2, row)), matrix))
