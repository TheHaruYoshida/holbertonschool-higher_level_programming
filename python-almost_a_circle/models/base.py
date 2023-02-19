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
