#!/usr/bin/python3
'''
Contain the class BaseGeometry and subclass Rectangle'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Square that inherits from Rectangle
    Args:
        size: size of square
    '''
    def __init__(self, size):
        '''instantiation of square

        Args:
            size: size of the square
        '''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
