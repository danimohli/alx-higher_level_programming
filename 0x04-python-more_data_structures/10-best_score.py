#!/usr/bin/python3

# finding the best heghest value in dicts key
def best_score(a_dictionary):

    value = 0
    key = ""

    # check if a_dictionary is Empty
    if a_dictionary is None:
        return None

    # Loop through dicts to obtain key and value
    for k, v in a_dictionary.items():
        if v > value:
            value = v
            key = k
        elif v == value:
            value = 0
            key = ""
    return key
