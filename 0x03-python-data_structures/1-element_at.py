#!/usr/bin/python3

# function to retrive element
# my_list the given list
# idx index of element to retrive

def element_at(my_list, idx):

    # taken the len of list
    ln = len(my_list) - 1
    # checking if index is within range

    if idx < 0 or idx > ln:
        return None
    return my_list[idx]
