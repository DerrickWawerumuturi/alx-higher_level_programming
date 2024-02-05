#!/usr/bin/python3
"""
func to check if obj is exactly of given class
"""


def is_same_class(obj, a_class):

    """
    func to check if obj is exactly of given class

    Args:
        obj: object to be checked
        a_class: class

    Returns: True or False
    """

    if type(obj) is a_class:
        return True
    else:
        return False
