#!/usr/bin/python3
def display_combinations():
    output = ""
    for i in range(10):
        for j in range(i + 1, 10):
            output += "{0}{1}, ".format(i, j)
    print(output[:-2])

display_combinations()