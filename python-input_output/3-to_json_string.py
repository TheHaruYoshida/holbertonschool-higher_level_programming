#!/usr/bin/python3
""" define the to_json_string function """


import json


def to_json_string(my_obj):
    """ returns the JSON of an object """
    return json.dumps(my_obj)
