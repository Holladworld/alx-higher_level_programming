#!/usr/bin/python3

# prints all integers of a list, in reverse order
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for integer in reversed(my_list):
            print("{:d}".format(integer))
