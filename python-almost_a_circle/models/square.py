#!/usr/bin/python3
""" Defines a class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the square"""
    def __init__(self, size, x=0, y=0, id=None):
        """ initialization for the square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ the str method"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} "
                f"- {self.width}")

    @property
    def size(self):
        """ size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """ size setter"""
        if type(size) is not int:
            raise TypeError("width must be an integer")
        elif size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ Defines the update, this time working fine"""
        if args and len(args) > 0:
            attr = ["id", "size", "x", "y"]
            i = 0
            for argv in args:
                setattr(self, attr[i], argv)
                i += 1
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ It returns the dictionary of a Rectangle """
        new = {}
        new["id"] = self.id
        new["size"] = self.size
        new["x"] = self.x
        new["y"] = self.y
        return new
