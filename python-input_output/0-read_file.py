#!/usr/bin/python3
""" define the read_file function """


def read_file(filename=""):
    """reads the file and print full their content """
    with open(filename) as f:
        data = f.read()
    print("{}".format(data), end="")
