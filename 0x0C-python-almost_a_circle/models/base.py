#!/usr/bin/python3

""" Define a class 
"""


class Base:
    """Create a private class attribute """
    __nb_objects = 0

    """define a class constructor 

    args:
        id: default is None
    """

    def __init__(self, id=None):
        if id is Not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
