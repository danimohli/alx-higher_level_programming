#!/usr/bin/python3

""" function same class reff """


def is_same_class(obj, a_class):

    """ function Documentation """

    """ Check if the object is exactly an instance of the specified class.

    Args:
    obj: Any object.
    The class to compare against.

    Returns:
    True if obj is an instance of a_class, otherwise False. """
    return type(obj) == a_class
