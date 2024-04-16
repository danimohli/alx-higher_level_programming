#!/usr/bin/python3
"""module to read file"""


def read_file(filename=""):
    """ read file"""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
    # except FileNotFoundError:
    # print(f"File '{filename}' not found.")
