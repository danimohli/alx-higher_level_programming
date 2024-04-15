#!/usr/bin/python3
""" excecption raise """


class BaseGeometry:
    """Compute the area of the geometry."""

    def area(self):
        """
        Compute the area of the geometry.

        Raises:
        Exception: Indicating that the method is not implemented.
        """
        raise Exception("area() is not implemented")
