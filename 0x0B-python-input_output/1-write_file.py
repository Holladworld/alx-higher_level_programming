#!/usr/bin/python3
'''
Module for write_file  method
'''


def write_file(filename="", text=""):
   '''Method that write a string to a text file'''
   with open(filename, "w", encoding="utf-8") as my_file_1:
        files = my_file_1.write(text)
        return (files)
