import unittest
from dummy import add_numbers

class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-1, -2), -3)

    def test_add_positive_and_negative(self):
        self.assertEqual(add_numbers(1, -2), -1)

    def test_add_zeros(self):
        self.assertEqual(add_numbers(0, 0), 0)

if __name__ == "__main__":
    unittest.main()