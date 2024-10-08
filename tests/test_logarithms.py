import unittest
from calculator import log, ln, exponential  # Replace 'your_module_name' with the actual module name
import math

class TestLogarithmFunctions(unittest.TestCase):

    # Test logarithm function with different bases
    def test_log(self):
        self.assertEqual(log(100), 2)                  # log10(100) = 2
        self.assertEqual(log(1), 0)                     # log10(1) = 0
        self.assertAlmostEqual(log(8, 2), 3)            # log2(8) = 3
        self.assertAlmostEqual(log(27, 3), 3)           # log3(27) = 3

        with self.assertRaises(ValueError):
            log(0)                                      # Should raise an error for log(0)
        with self.assertRaises(ValueError):
            log(-1)                                     # Should raise an error for log(-1)

    # Test natural logarithm function
    def test_ln(self):
        self.assertAlmostEqual(ln(math.e), 1)           # ln(e) = 1
        self.assertEqual(ln(1), 0)                       # ln(1) = 0

        with self.assertRaises(ValueError):
            ln(0)                                       # Should raise an error for ln(0)
        with self.assertRaises(ValueError):
            ln(-1)                                      # Should raise an error for ln(-1)

    # Test exponential function
    def test_exponential(self):
        self.assertEqual(exponential(0), 1)             # e^0 = 1
        self.assertAlmostEqual(exponential(1), math.e)  # e^1 = e
        self.assertAlmostEqual(exponential(-1), 1 / math.e)  # e^-1 = 1/e

if __name__ == '__main__':
    unittest.main()
