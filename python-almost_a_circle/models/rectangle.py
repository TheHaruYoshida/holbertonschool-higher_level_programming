#!/usr/bin/python3
""" Defines module that contains class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Defines class rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super(Rectangle, self).__init__(id)

    @property
    def width(self):
        """ get the width """
        return self.__width

    @width.setter
    def width(self, width):
        """ width setter """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ get the height """
        return self.__height

    @height.setter
    def height(self, height):
        """ height setter """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ get the x """
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ get the y """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """defines the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """Prints the rectangle"""
        print('\n'.join(['#' * self.width for _ in range(self.height)]))

    def __str__(self):
        """defines the str update """
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} "
                f"- {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """defines an update """
        if (args is None or args == ()) and kwargs is not None:
            args = [kwargs.get("id"), kwargs.get("width"),
                    kwargs.get("height"), kwargs.get("x"),
                    kwargs.get("y")]
        try:
            self.id = args[0] or self.id
            self.width = args[1] or self.width
            self.height = args[2] or self.height
            self.x = args[3] or self.x
            self.y = args[4] or self.y
        except IndexError:
            return
    def to_dictionary(self):
        """It returns the dictionary of a Rectangle"""
        return dict(x=self.__x, y=self.__y, id=self.id,
                    height=self.__height, width=self.__width)
