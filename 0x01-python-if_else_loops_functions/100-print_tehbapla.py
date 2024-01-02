#!/usr/bin/python3
a = 122
state = "lower"
output = ""

while a >= 97:
    if state == "lower":
        output += chr(a)
        state = "upper"
    elif state == "upper":
        output += chr(a-32)
        state = "lower"
    a = a - 1
print("{}".format(output), end="")
