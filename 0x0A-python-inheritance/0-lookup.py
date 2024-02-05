#!/usr/bin/python3

"""
function that returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    func that returns the list of available
    attributes and methods of an object

    Args:
        obj: object passed

    Returns: list of attrs and methodsof obj
    """

    return dir(obj)
