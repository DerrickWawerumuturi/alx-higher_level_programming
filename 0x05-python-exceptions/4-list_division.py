#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    result = 0
    try:
        for i in range(list_length):
            try:
                result = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                print("division by 0")
                result = 0
            except TypeError:
                print("wrong type")
                result = 0
            except IndexError:
                print("out of range")
            finally:
                result_list.append(result)
    except IndexError:
        print("out of range")

    return result_list