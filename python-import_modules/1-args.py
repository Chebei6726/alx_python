import sys

def print_arguments():
    # Get the number of arguments
    num_arguments = len(sys.argv) - 1

    # Print the number of arguments
    print("Number of argument{}: {}".format('s' if num_arguments != 1 else '', num_arguments), end='')

    if num_arguments == 0:
        print(":.", end='\n')
    else:
        print(":", end='\n')

    # Print each argument and its position
    for i, arg in enumerate(sys.argv[1:], 1):
        print("{}: {}".format(i, arg))

if __name__ == "__main__":
    print_arguments()
