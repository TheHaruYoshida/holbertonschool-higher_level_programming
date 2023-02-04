#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class Tester(unittest.TestCase):


    def test_a_max_integer(self):
        self.assertEqual(max_integer([5, -2, 100, 3]), 100)

    def test_an_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_repeated_numbers(self):
        self.assertEqual(max_integer([1000, 1000, 1000]), 1000)

    def test_max_operated_integer(self):
        self.assertEqual(max_integer([-3, -5 * -5, 12, -1]), 25)

    def test_neg_numbers(self):
        self.assertEqual(max_integer([-10, -5, -2, -1]), -1)

    def test_float_numbers(self):
        self.assertEqual(max_integer([50, 51, 50, 49]), 51)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_zero_number(self):
        self.assertEqual(max_integer([0, 0]), 0)

    def test_one_number_in_a_list(self):
        self.assertEqual(max_integer([1]), 1)

    def test_string_number_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([0, '1'])

    def test_tuple_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([10, (20, 30)])

    def test_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'keyblade1': 1, 'keyblade2': 2})

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(1)
