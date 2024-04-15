#!/usr/bin/python3
""" define inheritor from """


def inherits_from(obj, a_class):
    """check sub class & check for obj of same class"""

    return issubclass(type(obj), a_class) and type(obj) != a_class
