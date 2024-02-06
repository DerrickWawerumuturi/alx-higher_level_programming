#!/usr/bin/python3

""" define a function
"""


def write_file(filename="", text=""):
    
    """
    function wites the content of a text into the file and returns the 
    number of characters written
    
    Args:
        filename: file to write to
        text: content to write in file 
    """
    with open(filename, "w", encoding="UTF8") as file:
        return file.write(text)
