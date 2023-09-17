#!/usr/bin/python3
'''This Module contains a Rectangle class'''

from models.base import Base


class Rectangle(Base):
    '''class Rectangle represent rectangle that is inherits from Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor, initialize attribute of the object'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

#List of setter/getter of width functions
    @property
    def width(self):
        '''Get the width of a rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set the width'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

#List of height of rectangle setter 
    @property
    def height(self):
       ''' '''
        return self.__height

    @height.setter
    def height(self, value):
        """set the valueof  height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """set value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        '''set value of x'''
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''set value of  x'''
        return self.__y

    @y.setter
    def y(self, value):
        '''set value of y'''
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''Defines the area of rectangle - Public method: returns the area value'''
        return self.width * self.height

    def display(self):
        '''prints in stdout the Rectangle instance with the character #.
        public method: display the rectangleusing #'''
        print('\n' * self.y + '\n'.join([' ' * self.x +
                                         '#' * self.width
                                         for i in range(self.height)]))

    def __str__(self):
        '''Defines a format for the string  representation of a Rectangle'''
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y,
                   self.width, self.height)

    def update(self, *args, **kwargs):
        '''Assigns an argument to each attribute'''

        attributes = ["id", "width", "height", "x", "y"]
        for a, arg in zip(attributes, args):
            setattr(self, a, arg)
        for a, arg in kwargs.items():
            setattr(self, a, arg)

    def to_dictionary(self):
        '''Returns the dictionary representation of a Rectangle'''

        atrributes = ["id", "width", "height", "x", "y"]
        return {obj: getattr(self, obj) for obj in atrributes}
