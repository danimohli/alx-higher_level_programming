#!/usr/bin/python3

# function to print list in reverse
def print_reversed_list_integer(my_list=[]):

    my_list.reverse()
    # loop using the len
    for x in range(len(my_list)):
        if str(my_list[x]) >= '0' and str(my_list[x]) <= '9':
            print("{:d}".format(my_list[x]))
        else:
            print("{:s}".format(my_list[x]))
