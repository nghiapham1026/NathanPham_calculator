import unittest
from calculator import (
    add, subtract, multiply, divide, power,
    log, sine, exponential, factorial, mean, median, mode, standard_deviation
)

class TestCalculator(unittest.TestCase):
    
    # Basic operations tests
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        with self.assertRaises(ValueError):  # Updated to expect ValueError
            divide(10, 0)

    # Advanced operations tests
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)

    # Logarithms tests
    def test_log(self):
        self.assertEqual(log(100), 2)  # Assuming base 10 logarithm
        with self.assertRaises(ValueError):
            log(-1)  # Logarithm of a negative number should raise an error

    # Trigonometry tests
    def test_sine(self):
        self.assertAlmostEqual(sine(0), 0)
        self.assertAlmostEqual(sine(30), 0.5)
        self.assertAlmostEqual(sine(90), 1)

    # Factorial tests
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)

    # Mean tests
    def test_mean(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(mean(data), 3)

    # Median tests
    def test_median(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(median(data), 3)
        data = [1, 2, 3, 4]
        self.assertEqual(median(data), 2.5)

    # Mode tests
    def test_mode(self):
        data = [1, 2, 2, 3, 4]
        self.assertEqual(mode(data), 2)  # Test single mode case
        data = [1, 1, 2, 2]
        self.assertEqual(mode(data), [1, 2])  # Now it returns both modes

    # Standard deviation tests
    def test_standard_deviation(self):
        data = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(standard_deviation(data), 1.41421356237)  # sqrt(2)

if __name__ == '__main__':
    unittest.main()
