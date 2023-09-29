#!/usr/bin/python3
'''Module for class Rectangle. It inherited from baseGometry'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''crepresentation of rectangle '''
    def __init__(self, width, height):
        '''
        Intialization of Rectangle

        Args:
            width: breadth of a rectangle
            height: lengt of a rectangle
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Return area of rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''String representation of rectangle method'''
        return "[{}]{:d}/{:d}".format(Rectangle.__name__, self.__width,
                                      self.__height)
