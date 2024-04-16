#!/usr/bin/python3
"""multi inheritors"""


class BaseGeometry:
    """BaseGeometry"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle"""

    def __init__(self, width, height):
        super().__init__()
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"


if __name__ == "__main__":
    # Testing the Rectangle class
    rectangle = Rectangle(3, 4)
    print(rectangle)  # Output: [Rectangle] 3/4
    print(rectangle.area())  # Output: 12
    try:
        rectangle = Rectangle(-3, 4)  # Should raise ValueError
    except ValueError as e:
        print(e)  # Output: width must be greater than 0
    try:
        rectangle = Rectangle(3, "4")  # Should raise TypeError
    except TypeError as e:
        print(e)  # Output: height must be an integer
