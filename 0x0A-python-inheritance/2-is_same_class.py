#!/usr/bin/python3
'''
Module for function is_same_class
'''


def is_same_class(obj, a_class):
    '''
    Checks if object is an instance of specified class
        Args:
            obj: inital object
            a_class: class to confirm with oobject
            Return:True if the object is exactly an instance
    of the specified class; otherwise False.
    '''
    return type(obj) is a_class
