def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print("Empty matrix")
        return

    max_length = 0

    # Calculate the maximum length of any integer in the matrix
    for row in matrix:
        for num in row:
            num_length = len(str(num))
            if num_length > max_length:
                max_length = num_length

    # Print the matrix with proper formatting
    for row in matrix:
        for num in row:
            format_str = "{:>" + str(max_length) + "}"
            print(format_str.format(num), end=" ")
        print()  # Move to the next line after each row