#!/usr/bin/python3
import json
""" define a json to string module
"""

def load_from_json_file(filename):
    """ loads json to file"""
    with open(filename, "r", encoding="utf-8") as file:
        jsonfile = file.read()
        
        myobj = json.loads(jsonfile)
        
        return  myobj
