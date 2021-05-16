#!/usr/bin/python3
""" tests for the base class"""
import unittest
from models import rectangle
from models.base import Base
Rectangle = rectangle.Rectangle


class TestRectangle(unittest.TestCase):
    """ tests for Rectangle"""

    def test_rectangle_exists(self):
        r = Rectangle(3, 4, 5, 6)
        r = Rectangle(2, 3, 3, 3, 4)

    def test_width_height_value(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 1)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2, 3, 4)
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2, 3, 4)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3, 4)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4)

    def test_value_type(self):
        with self.assertRaises(TypeError):
            r = Rectangle(2, 3, "4")
        with self.assertRaises(TypeError):
            r = Rectangle(2, 3, 3, "4")
        with self.assertRaises(TypeError):
            r = Rectangle(2, "4", 3, 4)
        with self.assertRaises(TypeError):
            r = Rectangle("2", 3, 3, 4)

if __name__ == '__main__':
    unittest.main()
