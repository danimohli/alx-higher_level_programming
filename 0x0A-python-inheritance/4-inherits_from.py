#!/usr/bin/python3

""" inheritaotr """


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a
    class that inherited (directly or indirectly)
    from the specified class.

    Args:
    obj: Any object.
    a_class: The class to compare against.

    Returns:
    True if obj is an instance of a subclass of a_class, otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
