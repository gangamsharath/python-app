import unittest
import calc

class CaclTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(-1,-1), -2)

    def test_sub(self):
        self.assertEqual(calc.subtract(5,3), 2)

    def test_mul(self):
        self.assertEqual(calc.multiply(2,3), 6)

    def test_div(self):
        self.assertEqual(calc.divide(6,2), 3)
        with self.assertRaises(ZeroDivisionError):
            calc.divide(6,0)

if __name__ == "__main__":
    unittest.main()
