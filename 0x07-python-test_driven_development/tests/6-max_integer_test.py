#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_output(self):
        self.assertEqual(max_integer([4, 5, 6, 8]), 8)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([10]), 10)
        self.assertEqual(max_integer([-10, -20, -30]), -10)
        self.assertEqual(max_integer([10, 10, 10]), 10)
        self.assertEqual(max_integer([2.5, 1.6, 10.8]), 10.8)

    def test_bool(self):
        self.assertTrue(max_integer([True, False, True]), True)

    def test_str(self):
        self.assertEqual(max_integer(["Hi"]), "Hi")


if __name__ == '__main__':
    unittest.main()
