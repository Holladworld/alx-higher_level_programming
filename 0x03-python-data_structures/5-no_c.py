#!/usr/bin/python3
# function that removes all characters c and C from a string.
def no_c(my_string):
    new_string = ''
    for character in my_string:
        if character != 'c' and character != 'C':
            new_string += character
    return (new_string)
