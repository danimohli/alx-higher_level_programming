#!/usr/bin/python3

# To determine Max in list
def max_integer(my_list=[]):

    maxx x = 0, 0

    # checking if list is empty
    if len(my_list) == 0:
        return None

    # loop to check max number
    while x < len(my_list):
        if maxx < my_list[x]:
            maxx = my_list[x]
        x++
    return maxx
