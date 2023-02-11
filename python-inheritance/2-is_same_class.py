#!/usr/bin/python3
""" Define class Is_same_class """


def is_same_class(obj, a_class):
    """ returns whether object is exactly an instance of the specified class"""
    return type(obj) is a_class
