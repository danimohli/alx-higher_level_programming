#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    k_to_del = [k for k, v in a_dictionary.items() if v == value]
    for k in k_to_del:
        del a_dictionary[k]
    return a_dictionary
