#!/usr/bin/python3
'''
Class that inherits from baseGeometry
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class Square that inherits from Rectangle'''

    def __init__(self, size):
        '''
        instantiation of Rectangle
        '''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Calculat area'''
        return self.__size ** 2

    def __str__(self):
        '''print information'''
        return "[{}] {:d}/{:d}".format(self.__class__.__name__,
                                       self.__size,
                                       self.__size)
