#!/usr/bin/python3

""" Attribute same class check """


def is_same_class(obj, a_class):

    """ function Documentation """

    """
    Check if the object is exactly an instance of the specified class.

    Args:
    obj: Any object.
    a_class: The class to compare against.

    Returns:
    True if obj is an instance of a_class, otherwise False.
    """
    return type(obj) == a_class
