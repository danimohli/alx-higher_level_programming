#!/usr/bin/python3

# divide two interger and output result
# using finally section of exception

def safe_print_division(a, b):

    num = 0
    try:
        num = a / b
    except (TypeError, ZeroDivisionError):
        num = None
    finally:
        print('Inside result: {}'.format(num))
        return (num)
