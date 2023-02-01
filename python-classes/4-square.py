#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        self.size = size

    def area(self):
        """Calculates area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """ defines size"""
        return self.__size

    @size.setter
    def size(self, size):
        """ defines size"""
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
