#!/usr/bin/python3
"""
Module with a script that adds arguments
to a Python list saved in a file
"""

import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


file = 'add_item.json'
if os.path.exists(file):
    # if it exists, called it, otherwise
    # make a new one
    thd = load_from_json_file(file)
else:
    with open(file, 'w') as f:
        thd= []
        save_to_json_file([], file)

for arg in range(1, len(sys.argv)):
    thd.append(sys.argv[arg])
    save_to_json_file(thd, file)
