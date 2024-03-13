#!/usr/bin/python3

def remove_char_at(strng, n):

    new_str = ""
    for i in range(len(strng)):
        if i != n:
            new_str += strng[i]
    return new_str
