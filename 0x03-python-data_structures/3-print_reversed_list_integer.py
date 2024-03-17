#!/usr/bin/python3

# function to print list in reverse
def print_reversed_list_integer(my_list=[]):

    # len of list
    ln = len(my_list) - 1

    # loop using the len

    for x in range(ln, 0, -1):
        print("{:d}".format(my_list[x]))
