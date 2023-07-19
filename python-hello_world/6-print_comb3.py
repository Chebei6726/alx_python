#!/usr/bin/python3
def digits_combinations():
    combinations = [f"{i}{j}" for i in range(10) for j in range(10)]
    return combinations

def display_combinations_with_commas(combinations):
    print(', '.join(combinations))

def main():
    combinations = digits_combinations()
    print (display_combinations_with_commas(combinations))

main()