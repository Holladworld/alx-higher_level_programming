#!/usr/bin/python3
# function that prints all integers of a list, in reverse order.

def print_reversed_list_integer(my_list=[]):
    if my_list:
        for integer in my_list[::-1]:
            print("{}".format(integer))
