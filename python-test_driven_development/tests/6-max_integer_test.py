#!/usr/bin/python3

import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([-1, 0, 3, -5, 10]), 10)

    def test_duplicates(self):
        self.assertEqual(max_integer([1, 3, 3, 3, 2]), 3)

    def test_max_at_start(self):
        self.assertEqual(max_integer([10, 1, 2, 3]), 10)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)


if __name__ == '__main__':
    unittest.main()
