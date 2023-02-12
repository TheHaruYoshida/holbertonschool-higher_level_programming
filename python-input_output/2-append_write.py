#!/usr/bin/python3
""" define the append_write function """


def append_write(filename="", text=""):
    """ appends a string and return num of char written"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
