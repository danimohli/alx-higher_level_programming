#!/usr/bin/python3
""" load from json """

import json


def load_from_json_file(filename):
    '''json load'''

    with open(filename, "r") as file:
        return json.load(file)
