#!/usr/bin/python3
'''
Module for class Rectangle
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''class Rectangle with public instance methods that inherits from BaseGeometry'''
    def __init__(self, width, height):
        '''new instance of Rectangle'''
        '''
        Args:
            width: width of a rectangle
            height: height of a rectangle
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
