#!/usr/bin/python3
def weight_average(my_list=[]):
    num = 0
    base_num = 0
    for tup in my_list:
        num += tup[0] * tup[1]
        base_num += (tup[1])
    return float(num / base_num)
    if not my_list:
        return (0)
    
