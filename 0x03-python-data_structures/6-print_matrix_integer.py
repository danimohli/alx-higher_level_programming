#!/usr/bin/python3

# print matrix out
def print_matrix_integer(matrix=[[]]):

    if matrix == []:
        print(' ')

    for x in matrix:
        for y in range(len(x)):
            if y < len(x) - 1:
                print("{:d} ".format(x[y]), end='')
            else:
                print("{:d}".format(x[y]))
