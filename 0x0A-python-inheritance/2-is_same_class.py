#/usr/bin/python3

"""Defines available attributes or method of an object ."""

def is_same_class(obj, a_class):
    """ returns True if object is an instance of a class
    otherwise returns False 
    Args:
    obj : the object to check
    a_class(type): The class to compare with
    Returns:
        bool:  True if obj is an instance of a_class. Otherwise, False.
    """
    return isinstance(obj, a_class)
