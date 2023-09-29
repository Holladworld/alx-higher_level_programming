#!/usr/bin/python3
'''
Module for lookup function
'''

def lookup(obj):
    '''
    Args:
        obj: Initial object
        Return: List of available attributes and methods of an object
        '''
    return dir(obj)
