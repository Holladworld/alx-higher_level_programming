#!/usr/bin/python3
'''Module for load_from_json_file method'''

import json


def load_from_json_file(filename):
    '''This method that creates an Object from a “JSON file”'''
    with open(filename, "r", encoding="utf-8") as Json_file:
        obj = json.load(Json_file)
        return obj
