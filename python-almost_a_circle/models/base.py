#!/usr/bin/python3
""" defines module that contains base class """


import json


class Base:
    """ Defines class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string """
        Jsong = "[]"
        if (list_dictionaries is not None and
                list_dictionaries):
            Jsong = "["
            for i in list_dictionaries:
                Jsong += json.dumps(i)
            Jsong += "]"
        return Jsong

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation into file"""
        if list_objs is None:
            dict_objs = []
        else:
            dict_objs = [lists.to_dictionary() for lists in list_objs]
        with open(f"{cls.__name__}.json", mode='w', encoding='utf-8') as f:
            f.write(cls.to_json_string(dict_objs))
