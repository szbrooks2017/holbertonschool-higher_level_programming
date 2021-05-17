#!/usr/bin/python3
""" tests for the base class"""
import io
import unittest
import unittest.mock
from models import square
from models.base import Base
Square = square.Square


class TestSquare(unittest.TestCase):
    """ tests for Rectangle"""

    def test_dictionary(self):
        s = Square(1)
        d = s.to_dictionary()
        self.assertEqual({'id': 1, 'width': 1, 'height': 1, 'x': 0, 'y': 0}, d)

    def test_square_exists(self):
        s = Square(3, 3, 5)
        self.assertEqual(s.width, 3)
        self.assertEqual(s.height, 3)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 5)

    def test_square_width_height_x_exists(self):
        s = Square(3, 3, 3)
        self.assertEqual(s.width, 3)
        self.assertEqual(s.height, 3)
        self.assertEqual(s.x, 3)

    def test_square_width_height_exists(self):
        s = Square(3, 3)
        self.assertEqual(s.width, 3)
        self.assertEqual(s.height, 3)

    def test_width_height_value(self):
        with self.assertRaises(ValueError):
            s = Square(0, 1)

    def test_update(self):
        s = Square(1, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")

        s.update(1, 2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 2")

        s.update(1, 2, 3)
        self.assertEqual(str(s), "[Square] (1) 3/0 - 2")

        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            s = Square(-1, 2, 3)
        with self.assertRaises(ValueError):
            s = Square(1, -2, 3)
        with self.assertRaises(ValueError):
            s = Square(1, 2, -3)

    def test_area(self):
        s = Square(10, 10)
        self.assertEqual(s.area(), 100)

    def test_area2(self):
        s = Square(2, 2, 0, 0)
        self.assertEqual(s.area(), 4)

    def test_str(self):
        s = Square(1, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")

    def test_args(self):
        with self.assertRaises(TypeError):
            s = Square(1, 1, 1, 1, 1, 1, 1, 1)

    def test_value_type(self):
        with self.assertRaises(TypeError):
            s = Square(1, 1, "4")
        with self.assertRaises(TypeError):
            s = Square(1, "1", 3)
        with self.assertRaises(TypeError):
            s = Square("1", 1, 3)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display(self, mock_stdout):
        s = Square(1)
        s.display()
        self.assertEqual(mock_stdout.getvalue(), "#\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display2(self, mock_stdout):
        s1 = Square(1, 1, 1)
        s1.display()
        self.assertEqual(mock_stdout.getvalue(), "\n #\n")

if __name__ == '__main__':
    unittest.main()
