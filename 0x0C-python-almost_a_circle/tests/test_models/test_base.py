#!/usr/bin/python3
""" tests for the base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    """tests for base"""

    def setUp(self)
        pass

    def test_base_for_ID(self):
        b1 = Base()
        self.assertTrue(b1.id, 1)

    def test_if_id_match(self):
        base98 = Base(98)
        self.assertEqual(base98.id, 98)

if __name__ == '__main__':
    unittest.main()
