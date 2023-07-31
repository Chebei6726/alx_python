import sys

def print_arguments(argv):
    num_args = len(argv)

    if num_args == 0:
        print("Number of argument{}: .".format('s' if num_args != 1 else ''))
    else:
        print("Number of argument{}: {}:".format('s' if num_args != 1 else '', num_args))

        for i, arg in enumerate(argv, 1):
            print("{}: {}".format(i, arg))

if __name__ == "__main__":
    args = sys.argv[1:]
    print_arguments(args)
