#!/usr/bin/python3

from models.base import Base  # Importing the Base class
"""# models/rectangle.py"""


class Rectangle(Base):
    """REc class inherit Base"""

    """ init object """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        """ @ property """
        @property
        def width(self):
            return self.__width

        """ setter """
        @width.setter
        def width(self, value):
            self.__width = value

        """property"""
        @property
        def height(self):
            return self.__height

        """setter"""
        @height.setter
        def height(self, value):
            self.__height = value

        """proprt"""
        @property
        def x(self):
            return self.__x

        """setter"""
        @x.setter
        def x(self, value):
            self.__x = value

        """prprr"""
        @property
        def y(self):
            return self.__y

        """setter"""
        @y.setter
        def y(self, value):
            self.__y = value
