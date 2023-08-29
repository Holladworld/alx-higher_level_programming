#!/usr/bin/python3
# function that prints x elements of a list.
def safe_print_list(my_list=[], x=0):
    num = 0
    for element in range(x):
        try:
            print("{}".format(my_list[element]), end="")
        except IndexError:
            break
        else:
            num += 1
    print("")
    return (num)
