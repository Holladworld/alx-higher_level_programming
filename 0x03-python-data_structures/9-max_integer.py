#!/usr/bin/python3
# function that finds the biggest integer of a list.
def max_integer(my_list=[]):
    int_list = my_list
    if int_list:
        int_list.sort(reverse=True)
        return (int_list[0])
    return (None)
