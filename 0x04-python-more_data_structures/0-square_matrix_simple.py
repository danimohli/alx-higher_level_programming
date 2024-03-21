#!/usr/bin/python3

# function to find square root of matrix of list

def square_matrix_simple(matrix=[]):

    # copy matrix to modify
    n_matrix = [n[:] for n in matrix]

    for a in range(len(n_matrix)):
        for b in range(len(n_matrix[a])):
            n_matrix[a][b] = n_matrix[a][b] ** 2
    return n_matrix
