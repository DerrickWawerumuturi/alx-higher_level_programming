#!/usr/bin/python3

"""
Defines an class
"""
class BaseGeometry:
    """
    define a class 
    """
    def area(self):
        """
        Defines a public instance method
        
        raises:
        exception : area() is not implemented
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """
        Defines a public instance method
        Function:
            validates if the value given is  an integer
            
        Args:
            name (str) : The name of the variable to be checked.
            value (int) : The value of the variable
            
        Raises:
            TypeError:  If the value is not an integer
            ValueError:  If the value is less than zero
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0 :
            raise ValueError("{} must be greater than 0".format(name))
