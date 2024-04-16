#!/usr/bin/python3
"""append file"""


def append_write(filename="", text=""):
    """ add to file"""
    with open(filename, "a", encoding="utf-8") as file:
        num_chars_added = file.write(text)
        return num_chars_added
