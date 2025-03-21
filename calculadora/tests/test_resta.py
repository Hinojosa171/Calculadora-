import unittest
from operations.resta import resta

class TestResta(unittest.TestCase):
    def test_resta_positiva(self):
        self.assertEqual(resta(10, 5), 5)

    def test_resta_negativa(self):
        self.assertEqual(resta(-4, 5), -9)

    def test_resta_mixta(self):
        self.assertEqual(resta(5, -3), 8)

if __name__ == "__main__":
    unittest.main()