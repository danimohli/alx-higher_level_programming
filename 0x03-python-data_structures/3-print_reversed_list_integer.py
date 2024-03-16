#!/usr/bin/python3

# function to print list in reverse
def print_reversed_list_integer(my_list=[]):

    # len of list
    ln = len(my_list) - 1

    # loop using the len

    while ln >= 0:
        print("{:d}".format(my_list[ln]))
        ln -= 1
