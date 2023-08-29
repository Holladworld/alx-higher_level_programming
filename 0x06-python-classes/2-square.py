#!/usr/bin/python3
'''Defines a class Square'''


class Square:
    '''Class Square represent  a square
    Private instance attribute: size'''
    def __init__(self, size=0):
        '''initialize new square'''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
