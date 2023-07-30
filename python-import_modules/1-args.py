import sys

def print_arguments():
    # Manually set the arguments as a list
    args_list = ['Hello', 'Holberton', 'School', '98', 'Battery', 'street']
    num_arguments = len(args_list)

    # Print the number of arguments
    print("Number of argument{}: {}".format('s' if num_arguments != 1 else '', num_arguments), end='')

    if num_arguments == 0:
        print(":.", end='\n')
    else:
        print(":", end='\n')

    # Print each argument and position
    for i, arg in enumerate(args_list, 1):
        print("{}: {}".format(i, arg))

if __name__ == "__main__":
    print_arguments()