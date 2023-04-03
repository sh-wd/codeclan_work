import unittest
from src.compare import compare

class TestCompare(unittest.TestCase):
    def test_comparing_3_to_1_return_greater_than(self):
        expected_value = "3 is greater than 1"
        actual_value = compare(3, 1)
        self.assertEqual(expected_value, actual_value)

    def test_comparing_1_to_3_returns_less_than(self):
        expected_value = "1 is less than 3"
        actual_value = compare(1, 3)
        self.assertEqual(expected_value, actual_value)

    def test_comparing_1_to_1_returns_equals(self):
        expected_value = "1 is equal to 1"
        actual_value = compare(1, 1)
        self.assertEqual(expected_value, actual_value)

    def test_comparing_int_to_string_returns_less_than(self):
        expected_value = "1 is less than 2"
        actual_value = compare(1, "2")
        self.assertEqual(expected_value, actual_value)