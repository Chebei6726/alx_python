#!/usr/bin/python3
def two_number_combinations():
    combinations = [f"{i}{j}" for i in range(10) for j in range(10)]
    print(', '.join(combinations))

two_number_combinations()