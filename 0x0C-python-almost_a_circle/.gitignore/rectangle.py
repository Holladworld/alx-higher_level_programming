#!/usr/bin/python3
""" Rectangle Module """
from models.base import Base

class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor method """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """getter for x"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ Calculate the area of the rectangle """
        return self.width * self.height

    def display(self):

        """ Display the rectangle using '#' character and offsets """        print('\n' * self.y + '\n'.join([' ' * self.x +
                                         '#' * self.width
                                         for i in range(self.height)]))

    def __str__(self):
        """ String representation of the rectangle """
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y,
                   self.width, self.height)


    def update(self, *args, **kwargs):
        """ Update attributes with no-keyword arguments in the specified order """
        attributes = ["id", "width", "height", "x", "y"]
        for atrr, arg in zip(attributes, args):
            setattr(self, atrr, arg)
        for atrr, arg in kwargs.items():
            setattr(self, atrr, arg)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        atrributes = ["id", "width", "height", "x", "y"]
        return {key: getattr(self, key) for key in atrributes}
