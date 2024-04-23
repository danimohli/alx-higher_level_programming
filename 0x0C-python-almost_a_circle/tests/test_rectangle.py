#!/usr/bin/ython3

import unittest
from models.rectangle import Rectangle
"""test claass"""


class TestRectangle(unittest.TestCase):

    def test_constructor(self):
        # Test constructor with provided id
        rectangle1 = Rectangle(10, 20, id=1)
        self.assertEqual(rectangle1.id, 1)
        self.assertEqual(rectangle1.width, 10)
        self.assertEqual(rectangle1.height, 20)
        self.assertEqual(rectangle1.x, 0)
        self.assertEqual(rectangle1.y, 0)

        # Test constructor with automatic id generation
        rectangle2 = Rectangle(5, 5)
        self.assertEqual(rectangle2.id, 1)  # id should be 1, as it's the second object created

    def test_attributes(self):
        # Test width attribute
        rectangle = Rectangle(10, 20)
        rectangle.width = 15
        self.assertEqual(rectangle.width, 15)

        # Test height attribute
        rectangle.height = 25
        self.assertEqual(rectangle.height, 25)

        # Test x attribute
        rectangle.x = 5
        self.assertEqual(rectangle.x, 5)

        # Test y attribute
        rectangle.y = 10
        self.assertEqual(rectangle.y, 10)

if __name__ == '__main__':
    unittest.main()
