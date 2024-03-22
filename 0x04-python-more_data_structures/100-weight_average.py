#!/usr/bin/python3

# Look for average function
def weight_average(my_list=[]):

    if len(my_list) == 0:
        return 0

    score = 0
    people = 0

    for x in my_list:
        score += (x[0] * x[1])
        people += x[1]

    return score / people
