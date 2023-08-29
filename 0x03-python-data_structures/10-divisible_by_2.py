#!/usr/bin/python3
# finds all multiples of 2 in a list.

def divisible_by_2(my_list=[]):
    int_list = []
    if my_list:
        for integer in my_list:
            int_list.append(False if integer % 2 else True)
        return int_list
