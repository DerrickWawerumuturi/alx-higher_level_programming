#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module adds all arguments to a Python list, and then save them to a file.

Example:
    $ ./7-add_item.py Best School

"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
try:
    load = load_from_json_file("add_item.json")
except Exception:
    load = []
save_to_json_file(load + [v for v in sys.argv[1:]], "add_item.json")
