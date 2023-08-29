#!/usr/bin/python3
#  class Square that defines a square by: (based on 3-square.py)
'''Defines a class Square'''


class Square:
    '''Class Square that represent a square

    Argument:
        size (int): size of new class square'''
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        '''curent size of square'''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''initialize a new sqaure'''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''Return current area of square'''
        return (self.__size**2)
