#!/usr/bin/python3
'''This Module contains class BaseGeometry'''


class BaseGeometry:
    ''' A class with public Attribute area (class BaseGeometry)'''
    def __init__(self):
        '''New instance of BaseGeometry'''
        pass

    def area(self):
        '''Raise an exception when called'''
        raise Exception("area() is not implemented")
