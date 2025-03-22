import unittest
import sys
import os

# Add the parent directory to sys.path to allow imports from src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.operations.suma import suma

class TestSuma(unittest.TestCase):
    def test_suma_positiva(self):
        self.assertEqual(suma(5, 3), 8)

    def test_suma_negativa(self):
        self.assertEqual(suma(-5, -3), -8)

    def test_suma_mixta_positivo_negativo(self):
        self.assertEqual(suma(5, -9), -4)

    def test_suma_mixta_negativo_positivo(self):
        self.assertEqual(suma(-5, 3), -2)

    def test_suma_cero(self):
        self.assertEqual(suma(0, 5), 5)
        self.assertEqual(suma(5, 0), 5)
        self.assertEqual(suma(0, 0), 0)

if __name__ == "__main__":
    unittest.main()