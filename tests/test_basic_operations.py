import unittest
from calculator import add, subtract, multiply, divide

class TestBasicOperations(unittest.TestCase):

    # Test addition
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    # Test subtraction
    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    # Test multiplication
    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)

    # Test division
    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
