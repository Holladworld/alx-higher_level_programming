#!/usr/bin/python3
'''Module for save_to_json_file method'''


import json


def save_to_json_file(my_obj, filename):
    '''this method writes an Object to a
    text file, using a JSON representation'''
    with open(filename, "w") as Json_file:
        json.dump(my_obj, Json_file)
