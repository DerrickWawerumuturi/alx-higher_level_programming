#!/usr/bin/python3
"""We write a fxn that finds a peak in a list of unsorted ints"""


def find_peak(list_of_integers):
    """It helps find the peak number"""
    if len(list_of_integers) > 0:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
