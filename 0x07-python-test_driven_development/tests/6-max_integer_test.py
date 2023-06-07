#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class MaxIntegerTest(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_integer([]))

    def test_list_with_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_list_with_multiple_elements(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-5, 0, 10, -3, 8]), 10)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([5, 5, 5, 5, 5]), 5)

    def test_large_numbers(self):
        self.assertEqual(max_integer([9999999999, 10000000000, 8888888888]), 10000000000)

if __name__ == '__main__':
    unittest.main()
