#!/usr/bin/python3
"""class Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size):
        """constructor method"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """method to get area of Square"""

        return super().area()

    def __str__(self):
        """method to print readable str"""

        return "[Square] {}/{}".format(self.__size, self.__size)
