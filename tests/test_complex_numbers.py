import unittest
from calculator import add_complex, subtract_complex  # Replace 'your_module_name' with the actual module name

class TestComplexNumbers(unittest.TestCase):

    # Test addition of complex numbers
    def test_add_complex(self):
        self.assertEqual(add_complex(complex(1, 2), complex(3, 4)), complex(4, 6))  # (1+2j) + (3+4j) = (4+6j)
        self.assertEqual(add_complex(complex(0, 0), complex(0, 0)), complex(0, 0))  # (0+0j) + (0+0j) = (0+0j)
        self.assertEqual(add_complex(complex(-1, -1), complex(1, 1)), complex(0, 0))  # (-1-1j) + (1+1j) = (0+0j)

    # Test subtraction of complex numbers
    def test_subtract_complex(self):
        self.assertEqual(subtract_complex(complex(3, 4), complex(1, 2)), complex(2, 2))  # (3+4j) - (1+2j) = (2+2j)
        self.assertEqual(subtract_complex(complex(0, 0), complex(0, 0)), complex(0, 0))  # (0+0j) - (0+0j) = (0+0j)
        self.assertEqual(subtract_complex(complex(1, 1), complex(-1, -1)), complex(2, 2))  # (1+1j) - (-1-1j) = (2+2j)

if __name__ == '__main__':
    unittest.main()
