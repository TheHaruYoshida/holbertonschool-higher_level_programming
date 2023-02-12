#!/usr/bin/python3
""" define the class_to_json function """


def class_to_json(obj):
    """ returns the dictionary description for JSON obj """
    return obj.__dict__
