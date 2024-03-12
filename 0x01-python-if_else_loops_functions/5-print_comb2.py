#!/usr/bin/python3

for x in range(0, 100):
    if x < 10:
        print("{}{}, ".format(0, x), end=' ')
    elif x > 9 and x < 99:
        print("{}, ".format(x), end=' ')
    else:
        print("{}".format(x))
