#!/usr/bin/python3
'''Module for class student'''


class Student:
    '''Class that defines a student
    Attributes:
        Public instance attributes:
            first_name
            last_name
            age
        Method:
        first_name, last_name and age: def __init__(self, first_name,
        last_name, age):
        def to_json(self, attrs=None): that retrieves a
        dictionary representation of a Student
        instance (same as 8-class_to_json.py):
    '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        '''Retrieves a dictionary representation of student'''
        if type(attr) is list and all(type(i) is str for i in attr):
            return {k: res for k, res in self.__dict__.items() if k in attr}
        else:
            return self.__dict__
