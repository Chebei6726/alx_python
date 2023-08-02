def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print("Empty matrix")
        return

    for row in matrix:
        for num in row:
            print("{:d} ".format(num), end="")
        print()

