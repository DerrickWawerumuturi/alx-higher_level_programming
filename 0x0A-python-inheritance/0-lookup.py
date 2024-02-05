#/usr/bin/python3

"""Defines available attributes or method of an object ."""


def lookup(obj):
    """Returns a list of available attributes"""
    return (dir(obj))
