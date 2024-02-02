#!/usr/bin/python3

""" 
defines a function
"""

def print_square(size):
    """
    purpose:
    defines a function thar print a square with char
    '#'
    
    parameter:
    size: The length of the square
    
    Raises:
    
    TypeError: if size is not an integer
    
    ValueError: if size is less than 0
    
    TypeError: if size is a float and is less than 0
    """
    
    if  not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(0, size):
        j = 0
        for j in range(0, size):
            print("#", end="")
        print()
