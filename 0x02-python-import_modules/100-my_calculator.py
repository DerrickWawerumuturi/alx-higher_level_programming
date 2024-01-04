#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

def calculator(a, ops, b):
    operators = ["+", "-", "*", "/"]
    if ops not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if ops == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif ops == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif ops == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif ops == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))


if __name__ == "__main__":
    import sys
    argvLen = len(sys.argv)
    if argvLen != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    ops = sys.argv[2]
    b = int(sys.argv[3])

    calculator(a, ops, b)
