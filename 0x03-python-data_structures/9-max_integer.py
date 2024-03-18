#!/usr/bin/python3

# To determine Max in list
def max_integer(my_list=[]):

    # checking if list is empty
    if len(my_list) == 0:
        return None

    maxx = my_list[0]

    # loop to check max number
    for x in my_list:
        if maxx < x:
            maxx = x
    return maxx
