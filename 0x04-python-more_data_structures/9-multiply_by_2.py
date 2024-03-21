#!/usr/bin/python3

# multiply dicts value
def multiply_by_2(a_dictionary):

    # Create an empty dictionary
    dicts = {}

    # loop over key-value pairs of the original dict
    for k, v in a_dictionary.items():
        # Multiply each value by 2 and store it in the new dicts
        dicts[k] = v * 2
    return dicts
