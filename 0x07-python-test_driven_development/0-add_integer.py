#!/usr/bin/python3
"""function that add two integers
Args:
    a (int): first parameter
    b (int): second parameter
"""


def add_integer(a, b=98):
    """function that add two integers
    Returns:
        int: Sum of a and b
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

