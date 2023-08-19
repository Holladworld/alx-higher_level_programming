#!/usr/bin/python3

def search_replace(my_list, search, replace):
    def find_search(i):
        return i if i != search else replace
    return list(map(find_search, my_list))
