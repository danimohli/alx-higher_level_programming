#!/usr/bin/python3

# function to print list in reverse
def print_reversed_list_integer(my_list=[]):

    my_list.reverse()
    # loop using the len
    for x in range(len(my_list)):
        print("{}".format(my_list[x]))
