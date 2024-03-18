#!/usr/bin/python3

# function that replace element
# without changing the original

def new_in_list(my_list, idx, element):

    new = []
    # compare len with idx

    if idx < 0 or idx > len(my_list):
        return my_list

    new = my_list[:]
    new[idx] = element

    return new
