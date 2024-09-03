#!/usr/bin/python3

# import sys for stderr output function
import sys


# print to stderr but similar to
def safe_print_integer_err(value):

    try:
        print('{:d}'.format(value))
    except (ValueError, TypeError) as te:
        sys.stderr.write('Exception: {}\n'.format(te))
        return (False)
    return (True)
