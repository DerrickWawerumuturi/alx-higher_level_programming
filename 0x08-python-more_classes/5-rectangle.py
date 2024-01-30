#!/usr/bin/python3

""" 
defined a class 
"""


class Rectangle:
    """
     Class  Rectangle is initialized
    """
    
    
    def __init__(self, width = 0, height = 0):
        """
        Parameters:
        width: is the first parameter which should be an integer
        height: is the second paramter which should be an int
        Default: 0
        """    
        
        self._width = width
        self._height = height
    
    
    
    
    @property
    def width(self):
        return self._width
    """
    width  method is defined as a attribute 
    returns the width
    """
    
    @width.setter
    def width(self, value):
        """
       Method sets the height of the rectangle
       args: value
       if the Value is not an int: a TypeError is raised
       if the value is less than 0: a ValueError is raised
       Value = width
        """
        
        
        if isinstance(value, int) == False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value
        
    @property
    def height(self):
        """
        A height method is defined as a attribute
        returns the heigth given
        """
        return self._height
    
    @height.setter
    def height(self, value):
        """
        Method sets the value to the height
        
        args: value
        
        If the value is not an int : a TypeError is raised
        If the value is less than 0: a ValueError is raised
        
        value = Height
        """
        
        
        if  not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value
            
    """
    define a method called area
    Returns: the area(width * height) of the rectangle
    """
    def area(self):
        return self._width * self._height
    
    def perimeter(self):
        if self._width or self._height == 0:
            return 0
        else:
            return 2(self._height) + 2(self._width)
        
    def __str__(self):
        rect = ""
        if self._height or self._width == 0:
            return rect
        for i in range(self._height):
            rect += ("#" * self._width + '\n')
        return rect[:-1]
    
    def __repr__(self):
        return "Rectangle({}, {})".format(self._width, self._height)
    
    def __del__(self):
        print("BYe rectangle...")
