#!/usr/bin/python3
"""
function that returns a string “BestSchool” n times the number of the iteration
"""


def magic_string():
    """
    “BestSchool” n times the number of the iteration 
    """
    magic_string.n = getattr(magic_string, "n", 0) + 1
    return ", ".join(["BestSchool"] * magic_string.n)
