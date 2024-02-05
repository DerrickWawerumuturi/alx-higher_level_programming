#!/usr/bin/python3

def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a class that inherited from a_class.
    
    Args:
        obj: The object to check.
        a_class: The class to check against.
    
    Returns :
    True if the object is an instance of a class that inherited
    otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
