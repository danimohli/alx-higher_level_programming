#!/usr/bin/python3

# replace cC function

def no_c(my_string):

    new = []

    # loop incoming str to create new list
    for x in my_string:
        if x != 'c' and x != 'C':
            new.append(x)
    # join list
    new = "".join(new)
    return new
