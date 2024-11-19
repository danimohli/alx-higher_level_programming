#!/usr/bin/python3

# raise exception value
def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except NameError:
        raise
