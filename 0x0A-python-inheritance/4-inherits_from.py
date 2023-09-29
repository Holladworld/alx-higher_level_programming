#!/usr/bin/python3
''' 
Module for function inherits_from
'''


def inherits_from(obj, a_class):
    '''
    if object is an instance of a class that inherited from the specified class
    Args:
        obj: Object initiated
        a_class: class to be inherited
        Return: True if the object is an instance of a class that inherited (directly or indirectly) from the specified class;
        otherwise False
        '''
    return issubclass(type(obj), a_class) and type(obj) is not a_class
