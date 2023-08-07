def square_matrix_simple(matrix=[]):
    result_matrix = []

    # Iterate through each row in the input matrix
    for row in matrix:
        squared_row = []
        for element in row:
            # Square the element and append to the squared_row
            squared_row.append(element ** 2)
            result_matrix.append(squared_row)

    return result_matrix
#Test function

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)
