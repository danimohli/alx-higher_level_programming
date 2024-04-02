#!/usr/bin/python3

# import sys for stderr output function
import sys

# print to stderr but similar to forth
# (fift start from zero) func
defsafe_print_integer_err(value):
    try:
        print('{:d}'.format(value))
    except (TypeError, ValueError) as ra:
        sys.stderr.write('Exception: {}\n'.format(ra))
        return (False)
    return (True)
