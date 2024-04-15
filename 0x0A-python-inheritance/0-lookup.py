#!/usr/bin/python3

""" look up function for listing attr of class """


def lookup(obj):
    """ look up function for listing attr of class """
    return [attr for attr in dir(obj) if not
            callable(getattr(obj, attr)) or not attr.startswith("__")]
