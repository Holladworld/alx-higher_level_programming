#!/usr/bin/python3
'''Defines a Rectangle class.'''


class Rectangle:
    """Defining a rectangle."""

    def __init__(self, width=0, height=0):
        '''Initialize a new Rectangle.

        Args:
            width (int): Width of the new rectangle.
            height (int): Height of the new rectangle.
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''sets the width of the Rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Set the height of the Rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        '''Returns perimeter of the Rectangle.'''
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        '''Returns the printable representation of the Rectangle.

        'Represents the rectangle with the # character.'''
        
        if self.__width == 0 or self.__height == 0:
            return ("")

        string = []
        for s in range(self.__height):
            [string.append('#') for j in range(self.__width)]
            if s != self.__height - 1:
                string.append("\n")
        return ("".join(string))
