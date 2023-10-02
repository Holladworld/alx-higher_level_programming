#!/usr/bin/python3
'''
Module for to_json_string Method
'''


import json


def to_json_string(my_obj):
    '''
    Method that returns the JSON
    representation of an object (string)
    '''
    return json.dumps(my_obj)
