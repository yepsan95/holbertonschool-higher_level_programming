#!/usr/bin/python3
"""
This script adds all arguments to a Python list, and then save them to a file.
"""
import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    arg_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    arg_list = []

for i in range(1, len(sys.argv)):
    arg_list.append(sys.argv[i])

save_to_json_file(arg_list, "add_item.json")
