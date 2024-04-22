#!/usr/bin/python3

import unittest
from models.base import Base
"""Test case"""


class TestBase(unittest.TestCase):
    """for testin"""

    def test_id_assigned_when_provided(self):
        # Test that id is assigned correctly when provided
        base = Base(id=1)
        self.assertEqual(base.id, 1)

    def test_id_generated_correctly(self):
        # Test that id is generated correctly when not provided
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)


if __name__ == '__main__':
    unittest.main()
