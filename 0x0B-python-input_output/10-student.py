#!/usr/bin/python3
"""elabo... on class std json"""


class Student:
    """inti"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            attrs = [attr for attr in dir(self) if not attr.startswith("__")
                     and not callable(getattr(self, attr))]

        json_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)
        return json_dict
