import unittest
from calculator import power, sqrt, factorial

class TestAdvancedOperations(unittest.TestCase):

    # Test power function
    def test_power(self):
        self.assertEqual(power(2, 3), 8)  # 2^3
        self.assertEqual(power(5, 0), 1)  # Any number to the power of 0 is 1
        self.assertEqual(power(3, 2), 9)  # 3^2

    # Test square root function
    def test_sqrt(self):
        self.assertEqual(sqrt(4), 2)          # sqrt(4) = 2
        self.assertEqual(sqrt(0), 0)          # sqrt(0) = 0
        self.assertAlmostEqual(sqrt(2), 1.41421356, places=5)  # sqrt(2) ≈ 1.41421356

        with self.assertRaises(ValueError):
            sqrt(-1)  # Should raise an error for negative input

    # Test factorial function
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)  # 5! = 120
        self.assertEqual(factorial(0), 1)    # 0! = 1
        self.assertEqual(factorial(1), 1)    # 1! = 1

        with self.assertRaises(ValueError):
            factorial(-1)  # Should raise an error for negative input

if __name__ == '__main__':
    unittest.main()