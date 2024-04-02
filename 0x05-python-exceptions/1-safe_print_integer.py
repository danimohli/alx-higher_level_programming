#!/usr/bin/python3

# safe interger printer function
def safe_print_integer(value):

    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    return True
