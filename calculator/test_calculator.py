import unittest
from calculator import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_factorial(self):
        self.assertEqual(calculator.factorial(5), 120)
    
        self.assertEqual(calculator.factorial(0), 1)

if __name__ == '__main__':
    unittest.main()
