#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        if type(value) == int:
            print(value)
            return True
    except TypeError as e:
        sys.stderr.write("Exception: {:d}".format(e))
        return False
