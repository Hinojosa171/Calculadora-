import unittest
from operations.division import division

class TestDivision(unittest.TestCase):
    def test_division_positiva(self):
        self.assertEqual(division(10, 2), 5)

    def test_division_negativa(self):
        self.assertEqual(division(-10, 2), -5)

    def test_division_mixta(self):
        self.assertEqual(division(10, -2), -5)

    def test_division_cero(self):
        self.assertIsNone(division(10, 0))

if __name__ == "__main__":
    unittest.main()