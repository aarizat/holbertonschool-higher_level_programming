#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test cases to max integer into a list.
    """

    def test_output(self):
        self.assertEqual(max_integer([4, 5, 6, 8]), 8)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([10]), 10)
        self.assertEqual(max_integer([-10, -20, -30]), -10)
        self.assertEqual(max_integer([10, 10, 10]), 10)
        self.assertEqual(max_integer([2.5, 1.6, 10.8]), 10.8)
        self.assertEqual(max_integer([2, 1.6, 10.8, 20]), 20)
        self.assertEqual(max_integer([4, 5, 50, 6, 8]), 50)

    def test_bool(self):
        self.assertTrue(max_integer([True, False, True]), True)

    def test_str(self):
        self.assertEqual(max_integer(["Hi", "Hello"]), "Hi")
        self.assertEqual(max_integer("Hi"), "i")
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
        unittest.main()
