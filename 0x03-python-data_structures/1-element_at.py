#!/usr/bin/python3
#  function that retrieves an element from a list like in C.

def element_at(my_list, idx):
    return (my_list[idx] if idx >= 0 and idx < len(my_list) else None)
