#!/usr/bin/python3
'''Module for class student'''


class Student:
    '''Class that defines a student jsonification'''
    def __init__(self, first_name, last_name, age):
        '''Constructor'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """Retrieves a dictionary"""
        if type(attr) is list and all(type(g) is str for g in attr):
            return {h: l for h, l in self.__dict__.items() if h in attr}
        else:
            return self.__dict__.copy()

    def reload_from_json(self, json):
        '''Replaces all attributes of the Student instance'''
        for key, value in json.items():
            self.__dict__[key] = value
