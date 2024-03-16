#!/usr/bin/python3

# function to change elemnt at index specify
def replace_in_list(my_list, idx, element):

    # take the lenght of list
    # and check the range specified

    ln = len(my_list) - 1

    if idx < 0 or idx > ln:
        return my_list

    # change element of list
    my_list[idx] = element
    return my_list
