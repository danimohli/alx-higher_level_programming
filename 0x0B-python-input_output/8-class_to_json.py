#!/usr/bin/python3
""" 
move class to json 

"""


def class_to_json(obj):
    """
    json claass 

    """

    json_dict = {}

    # loop obj
    for attr_name in dir(obj):
        if not attr_name.startswith("__") and not
        callable(getattr(obj, attr_name)):
            attr_value = getattr(obj, attr_name)

            """
            an if state ment

            """
            if isinstance(attr_value, (list, dict, str, int, bool)):
                json_dict[attr_name] = attr_value
    return json_dict
