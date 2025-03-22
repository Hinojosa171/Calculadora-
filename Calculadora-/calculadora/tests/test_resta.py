import unittest
import sys
import os

# Add the parent directory to sys.path to allow imports from src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.operations.resta import resta

class TestResta(unittest.TestCase):
    def test_resta_positiva(self):
        self.assertEqual(resta(10, 5), 5)

    def test_resta_negativa_positiva(self):
        self.assertEqual(resta(-4, 5), -9)

    def test_resta_positiva_negativa(self):
        self.assertEqual(resta(5, -3), 8)

    def test_resta_negativa_negativa(self):
        self.assertEqual(resta(-5, -3), -2)

    def test_resta_cero(self):
        self.assertEqual(resta(0, 5), -5)
        self.assertEqual(resta(5, 0), 5)
        self.assertEqual(resta(0, 0), 0)

if __name__ == "__main__":
    unittest.main()