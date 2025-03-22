import unittest
import sys
import os

# Add the parent directory to sys.path to allow imports from src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.operations.multiplicacion import multiplicacion

class TestMultiplicacion(unittest.TestCase):
    def test_multiplicacion_positiva(self):
        self.assertEqual(multiplicacion(3, 4), 12)

    def test_multiplicacion_negativa_positiva(self):
        self.assertEqual(multiplicacion(-3, 4), -12)

    def test_multiplicacion_positiva_negativa(self):
        self.assertEqual(multiplicacion(3, -4), -12)

    def test_multiplicacion_negativa_negativa(self):
        self.assertEqual(multiplicacion(-3, -4), 12)

    def test_multiplicacion_cero(self):
        self.assertEqual(multiplicacion(0, 5), 0)
        self.assertEqual(multiplicacion(5, 0), 0)
        self.assertEqual(multiplicacion(0, 0), 0)

if __name__ == "__main__":
    unittest.main()