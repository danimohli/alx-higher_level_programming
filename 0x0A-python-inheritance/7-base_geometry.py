#!/usr/bin/python3
""" type validator """


class BaseGeometry:
    """ exception and validator """
    def area(self):
        """
        Compute the area of the geometry.

        Raises:
        Exception: Indicating that the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate if the value is an integer and greater than 0.

        Args:
        name: A string representing the name of the value.
        value: The value to be validated.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
