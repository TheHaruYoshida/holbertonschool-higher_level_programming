#!/usr/bin/python3
class Square:
    """ Defines a class Square"""
    def __init__(self, size=0):
	     """ initializes the Square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Retruns the area"""
        return (self.__size ** 2)

    @property
    def size(self):
        """ returns the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ prints the # square"""
        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
