import unittest
from operations.suma import suma

class TestSuma(unittest.TestCase):
    def test_suma_positiva(self):
        self.assertEqual(suma(5, 3), 8)

    def test_suma_negativa(self):
        self.assertEqual(suma(-5, -3), -8)

    def test_suma_mixta(self):
        self.assertEqual(suma(5, -9), -4)

if __name__ == "__main__":
    unittest.main()