#!/usr/bin/python3

# function that output nth of x
def safe_print_list_integers(my_list=[], n=0):

    x = 0
    for i in range(n):
        try:
            print("{:d}".format(my_list[i]), end="")
            x += 1
        except (TypeError, ValueError):
            print('', end='')
    print("")
    return (x)
