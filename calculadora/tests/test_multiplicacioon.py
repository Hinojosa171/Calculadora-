import unittest
from operations.multiplicacion import multiplicacion

class TestMultiplicacion(unittest.TestCase):
    def test_multiplicacion_positiva(self):
        self.assertEqual(multiplicacion(3, 4), 12)

    def test_multiplicacion_negativa(self):
        self.assertEqual(multiplicacion(-3, 4), -12)

    def test_multiplicacion_mixta(self):
        self.assertEqual(multiplicacion(-3, -4), 12)

if __name__ == "__main__":
    unittest.main()