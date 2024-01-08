#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """ A function that returns integers from a list of lists """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")
            if j != (len(matrix[i]) - 1):
                print(" ", end="")

        print("")
