#!/usr/bin/python3
"""
defines a class that inherites """
class Square(Rectangle):
    """ Square class inherits from Rectangle """

    def __init__(self, size):
        """ Initializes a Square instance """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Computes the area of the square """
        return self.__size * self.__size

    def __str__(self):
        """ Returns the square description """
        return "[Square] {}/{}".format(self.__size, self.__size)
