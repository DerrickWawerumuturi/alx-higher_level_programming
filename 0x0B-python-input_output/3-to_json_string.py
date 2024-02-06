#!/usr/bin/python3
import json

""" defines a json module """

def to_json_string(my_obj):
    """ function returns the json representation oa file object
    """

    return json.dump(my_obj)
