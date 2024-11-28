#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_positive_value(self):
        self.assertEqual(max_integer([9, 6, 10, 2]), 10)
        self.assertEqual(max_integer([100, 0, 10.0, 78, 101]), 101)

    def test_negative_value(self):
        self.assertEqual(max_integer([-29, -76, -81, 0, -5]), 0)
        self.assertEqual(max_integer([-23, -1, -4, -1]), -1)

    def test_float_value(self):
        self.assertEqual(max_integer([1.00, 0, 10.0, 78.4, 10.1]), 78.4)
        self.assertEqual(max_integer([-7.29, -7.6, -8.1, -4.5, -5.8]), -4.5)
