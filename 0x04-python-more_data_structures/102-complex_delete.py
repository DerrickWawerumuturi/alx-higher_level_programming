#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = {key: value for key, value in a_dictionary.items() if value != value}

    a_dictionary.clear()
    a_dictionary.update(new_dict)
