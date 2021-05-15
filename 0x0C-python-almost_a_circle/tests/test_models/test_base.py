#!/usr/bin/python3
""" tests for the base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    """tests for base"""

    def test_base(self):
        self.b1 = Base()
