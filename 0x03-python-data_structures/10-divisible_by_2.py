#!/usr/bin/python3

# finding division of two
def divisible_by_2(my_list=[]):

    # new list to save result on
    result = []

    for x in my_list:
        if x % 2 == 0:
            result.append(True)
        result.append(False)
    return result
