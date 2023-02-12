#!/usr/bin/python3
""" Define class Square """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class square to define a square """
    def __init__(self, size):
        self.__size = size
        super().__init__(size, size)
        self.integer_validator("size", size)

    def area(self):
        return self.__size**2

    def __str__(self):
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
