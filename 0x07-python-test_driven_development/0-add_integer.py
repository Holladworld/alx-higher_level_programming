#!/usr/bin/python3

'''Defines a simple integer addition function.'''


def add_integer(a, b=98):

    '''Return the integer addition of a and b.
    Args:
        a(int, float): First parameter.
        b(int, float): Second parameter.

    Float arguments are typecasted to ints before addition is performed.
    Returns:
    int: return an integer of sum of a and b parameters.


    Raises:
        TypeError: If either of a or b is a non-integer and non-float.'''


    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
