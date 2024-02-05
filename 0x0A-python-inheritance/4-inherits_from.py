#!/usr/bin/python3
""" method that checks if obj is an instance of a_class
"""


def inherits_from(obj, a_class):
    """ method that checks if obj is an instance of a_class

    Args:
        obj: object
        a_class: class 

    Returns: True or False
    """
    
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
