#!/usr/bin/python3

# To determine Max in list
def max_integer(my_list=[]):

    maxx = my_list[0]
    x = 0

    # checking if list is empty
    if len(my_list) == 0:
        return None

    # loop to check max number
    while x < len(my_list):
        if maxx <= my_list[x]:
            maxx = my_list[x]
        x += 1
    return maxx
