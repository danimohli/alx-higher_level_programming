#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or
    if it's an instance of a class that inherited from,
    the specified class.

    Args:
    obj: Any object.
    a_class: The class to compare against.

    Returns:
    True if obj is an instance of a_class or its subclass, otherwise False.
    """
    return isinstance(obj, a_class)
