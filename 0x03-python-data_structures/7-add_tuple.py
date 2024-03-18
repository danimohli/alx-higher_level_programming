#!/usr/bin/python3

# add tuple function
# argument must be two (2)

def add_tuple(tuple_a=(), tuple_b=()):

    # convert to list and take len
    tuple_a = list(tuple_a)
    a = len(tuple_a)

    tuple_b = list(tuple_b)
    b = len(tuple_b)

    # checking tuple to determine empthy tuple
    if a == 1:
        tuple_a.append(0)
    elif a == 0:
        tuple_a.append(0)
        tuple_a.append(0)
    elif a > 2:
        del tuple_a[2:]

    if b == 1:
        tuple_b.append(0)
    elif b == 0:
        tuple_b.append(0)
        tuple_b.append(0)
    elif b > 2:
        del tuple_b[2:]

    new_tuple = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return new_tuple
