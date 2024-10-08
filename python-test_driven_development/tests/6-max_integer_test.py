#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-5]), -5)

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)
        self.assertEqual(max_integer([-1.1, -2.2, -3.3, -4.4]), -1.1)

    def test_mixed_integers_and_floats(self):
        self.assertEqual(max_integer([1, 2.2, 3, 4.4]), 4.4)

    def test_strings(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, "string", 4])

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))


if __name__ == '__main__':
    unittest.main()
