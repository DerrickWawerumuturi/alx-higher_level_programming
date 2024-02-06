#!/usr/bin/python3
""" define a function."""


def append_write(filename="", text=""):
    """
    function takes in a string and appends it to teh end of the file
    and returns the number of characters added.
    
    Args:
        filename: file to add string.
        text: string to be added to the file.
    """
    with open(filename,  "a", encoding="utf-8") as file:
        return file.write(text)
