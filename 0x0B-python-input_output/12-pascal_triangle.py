#!/usr/bin/python3
'''
Module for pascal_triangule method
'''


def pascal_triangle(n):
    '''
    Returns a list of integers
        Args:
        n (int): number pf lists and digits
        Return: list of lists
    '''
    if n <= 0:
        return []

    if n == 1:
        return [[1]]

    pascal = [[1], [1, 1]]

    for rows in range(1, n-1):
        column = [1]
        for lists in range(0, len(pascal[rows])-1):
            column.extend([pascal[rows][lists] + pascal[rows][lists+1]])
        column += [1]
        pascal.append(column)
    return pascal
