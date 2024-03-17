#!/usr/bin/python3

# function to print list in reverse
def print_reversed_list_integer(my_list=[]):

    if my_list is None:
        print(' ')
        return my_list

    # len of lisit
    my_list.reverse()
    ln = len(my_list)

    # loop using the len

    for x in range(ln):
        print("{:d}".format(my_list[x]))
