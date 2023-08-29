#!/usr/bin/python3
# function that replaces an element in a list at a specific
# position without modifying the original list (like in C)
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if idx < len(my_list) and idx >= 0:
        new_list[idx] = element
        return (new_list)
    return (my_list)
