#!/usr/bin/python3

# function that print nth x of list

def safe_print_list(my_list=[], x=0):

    if x == 0:
        return 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end='')
        print()
    except IndexError:
        print()
        return i

    return i+1
