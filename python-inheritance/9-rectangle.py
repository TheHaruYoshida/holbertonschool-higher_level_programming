#!/usr/bin/python3
""" Define class basegeometry """


class BaseGeometry():
    """ Define BaseGeometry class """
    def area(self):
        """ raise exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ a class inherited from BaseGeometry """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return("[Rectangle] {}/{}".format(self.__width, self.__height))

