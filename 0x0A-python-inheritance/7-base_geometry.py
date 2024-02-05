#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method that validates value
        Args:
            name: string
            value: value to be checked
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than zero".format(name))
