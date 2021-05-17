#!/usr/bin/python3
""" tests for the base class"""
import io
import os
import unittest
import unittest.mock
from models import rectangle
from models.base import Base
Rectangle = rectangle.Rectangle


class TestRectangle(unittest.TestCase):

    """ tests for Rectangle"""

    def test_load_from_file(self):
        filename = 'Rectangle.json'
        if os.path.exists(filename):
            os.remove(filename)
        self.assertEqual(Rectangle.load_from_file(), [])
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists(filename))

    def test_save_to_file(self):
        filename = "Rectangle.json"
        if os.path.exists(filename):
            os.remove(filename)
        Rectangle.save_to_file(None)
        with open(filename, 'r') as f:
            self.assertEqual(f.read(), '[]')

        if os.path.exists(filename):
            os.remove(filename)
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists(filename))

        if os.path.exists(filename):
            os.remove(filename)
        Rectangle.save_to_file([Rectangle(1, 1, 0, 0, 32)])
        self.assertTrue(os.path.exists(filename))

    def test_create_rec(self):
        r = {"id": 1, "width": 1, "height": 1, "x": 0, "y": 0}
        rcreate = Rectangle.create(**r)
        self.assertEqual("[Rectangle] (1) 0/0 - 1/1", str(rcreate))

    def test_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 7)
        d = r.to_dictionary()
        self.assertEqual({'x': 1, 'y': 9, 'id': 7,
                          'height': 2, 'width': 10}, d)

    def test_rectangle_exists(self):
        r = Rectangle(3, 4, 5, 6)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    def test_rectangle_width_height_x_exists(self):
        r = Rectangle(3, 4, 5)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)

    def test_rectangle_width_height_exists(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)

    def test_width_height_value(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 1)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)

    def test_update(self):
        r = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")

        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/1")

        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/1")

        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/3")

        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/0 - 2/3")

        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2, 3, 4)
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2, 3, 4)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3, 4)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4)

    def test_area(self):
        r = Rectangle(10, 10)
        self.assertEqual(r.area(), 100)

    def test_area2(self):
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def test_value_type(self):
        with self.assertRaises(TypeError):
            r = Rectangle(2, 3, "4")
        with self.assertRaises(TypeError):
            r = Rectangle(2, 3, 3, "4")
        with self.assertRaises(TypeError):
            r = Rectangle(2, "4", 3, 4)
        with self.assertRaises(TypeError):
            r = Rectangle("2", 3, 3, 4)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display(self, mock_stdout):
        r = Rectangle(1, 1)
        r.display()
        self.assertEqual(mock_stdout.getvalue(), "#\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display2(self, mock_stdout):
        r1 = Rectangle(1, 1, 1, 1)
        r1.display()
        self.assertEqual(mock_stdout.getvalue(), "\n #\n")

if __name__ == '__main__':
    unittest.main()
