#!/usr/bin/python3
from sys import stderr

# print to stderr but similar to forth
# (fift start from zero) func
def safe_print_integer_err(value):

    try:
        print('{:d}'.format(value))
    except (TypeError, ValueError) as ra:
        stderr.write('Exception: {}\n'.format(ra))
        return (False)
    return (True)
