#!/usr/bin/python3
""" class to json funct """


def class_to_json(obj):
    """ class dict """
    json_dict = {}
    for attr_name in dir(obj):
        if not attr_name.startswith("__") and not
        callable(getattr(obj, attr_name)):
            attr_value = getattr(obj, attr_name)
            if isinstance(attr_value, (list, dict, str, int, bool)):
                json_dict[attr_name] = attr_value
    return json_dict
