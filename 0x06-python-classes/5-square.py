#!/usr/bin/python3
# class Square that defines a square by: (based on 4-square.py)
'''Defines a class Square'''


class Square:
    '''Class Square that defines a square
    Attributes:
       size (int): size of a square'''

    def __init__(self, size=0):
        '''initalize new size'''
        self.size = size

    @property
    def size(self):
        '''set current size of square'''
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return (self.__size**2)

    def my_print(self):
        '''print the square with character "#" '''
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
