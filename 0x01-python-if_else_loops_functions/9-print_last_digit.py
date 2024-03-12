#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        number *= -1

    ls_dig = number % 10
    print("{:d}".format(ls_dig), end="")
    return ls_dig
