#!/usr/bin/python3
""" write to file """


def write_file(filename="", text=""):
    """write file"""
    with open(filename, "w", encoding="utf-8") as file:
        num_chars_written = file.write(text)
        return num_chars_written
