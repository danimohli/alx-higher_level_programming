#!/usr/bin/python3
""" python class project"""

import json
import os


class Base:
    """ class base"""

    __nb_objects = 0
    """ Private class attribute"""

    def __init__(self, id=None):
        if id is not None:
            self.id = id
            """Assign id if provided"""
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' Converts list of dictionaries to JSON string'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Writes JSON string representation of list_objs to a file'''
        if list_objs is None:
            list_objs = []

        '''Get the class name dynamically'''
        class_name = cls.__name__
        ''' Prepare the filename using the class name'''
        filename = "{}.json".format(class_name)

        '''Convert list of objects to JSON string'''
        json_string = cls.to_json_string([obj.to_dictionary()
                                         for obj in list_objs])

        '''Write JSON string to file'''
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        '''Converts JSON string to list of dictionaries'''
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Returns an instance with all attributes already set'''
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)
        else:
            raise NotImplementedError("only implemented for Rect & Sqr cls")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        '''Returns a list of instances from file'''

        filename = "{}.json".format(cls.__name__)

        '''Check if the file exists'''
        if not os.path.exists(filename):
            return []

        '''Read the contents of the file and convert to list of dictionaries'''
        with open(filename, 'r') as file:
            json_string = file.read()
            dictionaries = cls.from_json_string(json_string)

        '''Create instances from the dictionaries and return as a list'''
        return [cls.create(**dictionary) for dictionary in dictionaries]
