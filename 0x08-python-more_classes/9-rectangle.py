#!/usr/bin/python3
'''Defines a Rectangle class.'''


class Rectangle:
    '''Represent a rectangle.'''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''Initialize a new Rectangle.'''
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        '''set the width of the Rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
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
        '''Return the area of the Rectangle.'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''Return the perimeter of the Rectangle'''
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Return Rectangle with the greater area.
         Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        '''Return a new Rectangle with width and height equal to size.'''
        return (cls(size, size))

    def __str__(self):
        '''Return the printable representation of the Rectangle.
        the rectangle with the # character.'''
        if self.__width == 0 or self.__height == 0:
            return ("")

        string = []
        for s in range(self.__height):
            [string.append(str(self.print_symbol)) for j in range(self.__width)]
            if s != self.__height - 1:
                string.append("\n")
        return ("".join(string))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        string = "Rectangle(" + str(self.__width)
        string += ", " + str(self.__height) + ")"
        return (string)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
