#!/usr/bin/python3

"""LockedClass with condition"""


class LockedClass:
    """
    raise error if attribute isn't first_name
    """
    def __setattr__(self, name, value):
        if name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute '{}'"
                                 .format(name))
