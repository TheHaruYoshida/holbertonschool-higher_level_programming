#!/usr/bin/python3
""" define the write_file function """


def write_file(filename="", text=""):
    """ writes a string and return num of char written"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
