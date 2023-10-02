#!/usr/bin/python3
'''Module container for class_to_json method'''


def class_to_json(obj):
    '''
    Method that returns the dictionary description
    with simple data structure for SON serialization of an object
    '''
    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    else:
        return {}
