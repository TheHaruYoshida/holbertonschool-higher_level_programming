#!/usr/bin/python3
""" Define function inherits_from"""


def inherits_from(obj, a_class):
    """checks if object is a subclass"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
