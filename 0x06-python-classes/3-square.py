#!/usr/bin/python3

""" define a class Square """

class Square:
    """ define instant method """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """define area method """
    def area(self):
        return (self.__size * self.__size)

