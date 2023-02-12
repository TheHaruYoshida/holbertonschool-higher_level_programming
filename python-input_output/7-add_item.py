#!/usr/bin/python3
""" adds all arguments to a python list, an save into a file """
from sys import argv
"""import argv"""

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""import load_from_jason_file function"""

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""import save_to_json_file"""

filename = "add_item.json"
try:
    s_data = load_from_json_file(filename)
    s_data += argv[1:]
    save_to_json_file(s_data, filename)
except FileNotFoundError:
    s_data = argv[1:]
    save_to_json_file(s_data, filename)
