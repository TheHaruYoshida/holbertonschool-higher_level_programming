#!/usr/bin/python3
"""Define class MyList"""


class MyList(list):
    """class MyList"""
    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
