#!/usr/bin/python3

# function that replace element
# without changing the original

def new_in_list(my_list, idx, element):

    new = []
    if my_list:
        # compare len with idx
        if idx < 0 or idx > len(my_list) or my_list is None:
            return my_list

        new = my_list[:]
        new[idx] = element

    return new
