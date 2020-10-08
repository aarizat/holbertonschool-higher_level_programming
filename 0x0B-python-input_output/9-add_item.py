#!/usr/bin/python3
"""
Python script to add all arguments to a Python list, and then save them
to a file.
"""
import os
import sys
save_to_json_f = __import__('7-save_to_json_file').save_to_json_file
load_from_json_f = __import__('8-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    filename = 'add_item.json'
    if os.path.isfile(filename):
        my_list = load_from_json_f(filename)
        my_list.extend(sys.argv[1:])
        save_to_json_f(my_list, filename)
    else:
        save_to_json_f(sys.argv[1:], filename)
