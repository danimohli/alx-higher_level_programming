#!/usr/bin/python3

# del list item usin index
def delete_at(my_list=[], idx=0):

    # check if num is within range
    # of list index

    if idx > len(my_list) - 1 or idx < 0:
        return my_list

    del my_list[idx]

    return my_list
