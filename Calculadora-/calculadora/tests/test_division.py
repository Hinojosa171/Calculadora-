import unittest
import sys
import os

# Add the parent directory to sys.path to allow imports from src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.operations.division import division

class TestDivision(unittest.TestCase):
    def test_division_positiva(self):
        self.assertEqual(division(10, 2), 5)

    def test_division_negativa_positiva(self):
        self.assertEqual(division(-10, 2), -5)

    def test_division_positiva_negativa(self):
        self.assertEqual(division(10, -2), -5)

    def test_division_negativa_negativa(self):
        self.assertEqual(division(-10, -2), 5)

    def test_division_cero_dividendo(self):
        self.assertEqual(division(0, 5), 0)

    def test_division_cero_divisor(self):
        self.assertIsNone(division(10, 0))

if __name__ == "__main__":
    unittest.main()