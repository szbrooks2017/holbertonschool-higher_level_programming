#!/usr/bin/python3
"""Unittest for max_int"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ test for max int """

    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_negative(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_none(self):
        self.assertIsNone(max_integer([]))

    def test_single(self):
        self.assertIsNone(max_integer([1]), 1)

if __name__ == '__main__':
    unittest.main()
