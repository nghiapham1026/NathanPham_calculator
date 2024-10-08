import unittest
from calculator import mean, median, mode, standard_deviation  # Replace 'your_module_name' with the actual module name

class TestStatistics(unittest.TestCase):

    # Test mean function
    def test_mean(self):
        self.assertEqual(mean([1, 2, 3, 4, 5]), 3)  # Mean of 1, 2, 3, 4, 5
        self.assertEqual(mean([10, 20, 30]), 20)     # Mean of 10, 20, 30
        self.assertEqual(mean([-1, 0, 1]), 0)        # Mean of -1, 0, 1

        with self.assertRaises(ValueError):
            mean([])  # Should raise an error for empty dataset

    # Test median function
    def test_median(self):
        self.assertEqual(median([1, 2, 3, 4, 5]), 3)         # Odd number of elements
        self.assertEqual(median([1, 2, 3, 4]), 2.5)          # Even number of elements
        self.assertEqual(median([5, 3, 1, 2, 4]), 3)         # Unsorted input

        with self.assertRaises(ValueError):
            median([])  # Should raise an error for empty dataset

    # Test mode function
    def test_mode(self):
        self.assertEqual(mode([1, 2, 3, 2, 1]), 1)           # Single mode
        self.assertEqual(mode([1, 2, 2, 3, 3]), [2, 3])      # Multiple modes
        self.assertEqual(mode([1, 1, 1, 2, 2]), 1)           # Mode with one clear winner

        with self.assertRaises(ValueError):
            mode([])  # Should raise an error for empty dataset

    # Test standard deviation function
    def test_standard_deviation(self):
        self.assertAlmostEqual(standard_deviation([1, 2, 3]), 0.816496580927726)  # Std of 1, 2, 3
        self.assertEqual(standard_deviation([1, 1, 1]), 0)                       # All identical values

        with self.assertRaises(ValueError):
            standard_deviation([])  # Should raise an error for empty dataset

if __name__ == '__main__':
    unittest.main()
