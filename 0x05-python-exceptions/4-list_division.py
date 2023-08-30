#!/usr/bin/python3
# function that divides element by element 2 lists.

def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for num in range(list_length):
        output = 0
        try:
            output = my_list_1[num] / my_list_2[num]
        except TypeError:
            print("wrong type")
            output = 0
        except ZeroDivisionError:
            print("division is 0")
            output = 0
        except IndexError:
            print("out of range")

        finally:
            new_list.append(output)
    return (new_list)
