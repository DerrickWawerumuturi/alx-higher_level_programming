#!/usr/bin/python3
"""script that adds all arguments to a Python list,
and then save them to a file"""

"""importing sys and os.path"""
import sys
import os.path

saveToJsonFile = __import__('5-save_to_json_file').save_to_json_file
loadFromJsonFile = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
args_list = []
# if filename exsits
if os.path.exists(filename):
    if os.path.getsize(filename) == 0:
        args_list = []
    else:
        args_list = loadFromJsonFile(filename)
for i in range(1, len(sys.argv)):
    args_list.append(sys.argv[i])
saveToJsonFile(args_list, filename)
