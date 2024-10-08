import unittest
import math
from calculator import sine, cosine, tangent

class TestTrigonometryFunctions(unittest.TestCase):

    # Test sine function
    def test_sine(self):
        self.assertAlmostEqual(sine(0), 0)               # sin(0) = 0
        self.assertAlmostEqual(sine(30), 0.5)            # sin(30) = 0.5
        self.assertAlmostEqual(sine(90), 1)              # sin(90) = 1
        self.assertAlmostEqual(sine(180), 0)             # sin(180) = 0
        self.assertAlmostEqual(sine(270), -1)            # sin(270) = -1

    # Test cosine function
    def test_cosine(self):
        self.assertAlmostEqual(cosine(0), 1)              # cos(0) = 1
        self.assertAlmostEqual(cosine(30), math.sqrt(3)/2)  # cos(30) = √3/2
        self.assertAlmostEqual(cosine(90), 0)             # cos(90) = 0
        self.assertAlmostEqual(cosine(180), -1)           # cos(180) = -1
        self.assertAlmostEqual(cosine(270), 0)            # cos(270) = 0

    # Test tangent function
    def test_tangent(self):
        self.assertAlmostEqual(tangent(0), 0)             # tan(0) = 0
        self.assertAlmostEqual(tangent(45), 1)            # tan(45) = 1

        # Set a threshold for what we consider "infinity"
        threshold = 1e10
        self.assertTrue(tangent(90) > threshold)          # tan(90) should be very large
        self.assertAlmostEqual(tangent(180), 0)           # tan(180) = 0
        self.assertTrue(tangent(270) > threshold)
        
if __name__ == '__main__':
    unittest.main()
