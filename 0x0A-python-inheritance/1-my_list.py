#!/usr/bin/python3
'''
Module for class MyList inherited from list
'''


class MyList(list):

    '''MyList that inherits from list'''
    def print_sorted(self):
        '''Method for print sorted list'''
        print(sorted(self))
