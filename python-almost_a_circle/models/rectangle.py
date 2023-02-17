#!/usr/bin/python3
""" Defines module that contains class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Defines class rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super(Rectangle, self).__init__(id)

    @property
    def width(self):
        """ get the width """
        return self.__width

    @width.setter
    def width(self, width):
        """ width setter """
        self.__width = width

    @property
    def height(self):
        """ get the height """
        return self.__height

    @height.setter
    def height(self, height):
        """ height setter """
        self.__height = height

    @property
    def x(self):
        """ get the x """
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter """
        self.__x = x

    @property
    def y(self):
        """ get the y """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter """
        self.__y = y
