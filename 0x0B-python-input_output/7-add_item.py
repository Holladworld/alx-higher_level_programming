#!/usr/bin/python3
'''
Module to adds all arguments to a Python
list, load, and then save them to a file
'''


import sys
import json
import os.path
save_json_file = __import__('5-save_to_json_file').save_to_json_file
load_json_file = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"
my_list = []
if os.path.exists(file):
    my_list = load_json_file(file)

for arg in range(1, len(sys.argv)):
    my_list.append(sys.argv[arg])

save_json_file(my_list, file)
