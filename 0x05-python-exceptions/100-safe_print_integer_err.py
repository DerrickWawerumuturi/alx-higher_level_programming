#!/usr/bin/python3


def safe_print_integer_err(value):
    import sys
    try:
        if type(value) == int:
            print(value)
            return True
    except TypeError as e:
        sys.stderr.write("Exception: {:d}".format(e))
        return False
