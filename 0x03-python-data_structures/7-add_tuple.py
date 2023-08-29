#!/usr/bin/python3
# function that adds 2 tuples.
# elem is element
def add_tuple(tuple_a=(), tuple_b=()):
    first_elem, second_elem = len(tuple_a), len(tuple_b)
    added_tuple = ((tuple_a[0] if first_elem >= 1 else 0) +
                 (tuple_b[0] if second_elem >= 1 else 0),
                 (tuple_a[1] if first_elem >= 2 else 0) +
                 (tuple_b[1] if second_elem >= 2 else 0))
    return added_tuple
