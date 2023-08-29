#!/usr/bin/python3
# class Square that defines a square by: (based on 2-square.py)
'''Defines a class Square.'''


class Square:
    """Class Square that reprents a square"""

    def __init__(self, size=0):
        '''initialize new square'''

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return(self.__size ** 2)
