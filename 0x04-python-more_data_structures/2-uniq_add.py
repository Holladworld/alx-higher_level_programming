#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for element in set(my_list):
        result += element
    return result

