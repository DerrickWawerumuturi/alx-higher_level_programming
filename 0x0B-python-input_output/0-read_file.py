#!/usr/bin/python3

""" define a function
"""


def read_file(filename=""):
    """
    function opens and reads a text file and prints it in stdout
    
    Args:
        filename: name of file to be read
    """
    
    with  open(filename, "r", encoding="UTF8") as file:
        content = file.read()
        print(content, end="")
