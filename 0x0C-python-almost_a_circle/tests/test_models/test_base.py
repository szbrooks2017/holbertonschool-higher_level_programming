#!/usr/bin/python3
""" tests for the base class"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    """tests for base"""

    def test_base_for_ID(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(None)
        self.assertEqual(b2.id, 2)

    def test_if_id_match(self):
        b98 = Base(98)
        self.assertEqual(b98.id, 98)

    def test_from_json(self):
        obj = Base.from_json_string(None)
        self.assertEqual(obj, [])

        obj = Base.from_json_string("[]")
        self.assertEqual(obj, [])

if __name__ == '__main__':
    unittest.main()
