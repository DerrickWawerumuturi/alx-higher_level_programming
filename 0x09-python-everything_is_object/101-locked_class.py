#!/usr/bin/python3
""" define locked class
"""

class LockedClass:
    """
    prevent object instantation of any attr
    other than first_name """
    __slots__  = ["first_name"]
