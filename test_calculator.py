"""
Unit tests for Calculator class
This file demonstrates collaborative testing
"""

import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        """Set up test calculator instance"""
        self.calc = Calculator()
    
    def test_add(self):
        """Test addition"""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
    
    def test_subtract(self):
        """Test subtraction"""
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(5, 10), -5)
    
    def test_multiply(self):
        """Test multiplication"""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
    
    def test_divide(self):
        """Test division"""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
    
    def test_divide_by_zero(self):
        """Test division by zero raises error"""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
    
    def test_power(self):
        """Test power operation"""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 2), 25)


if __name__ == "__main__":
    unittest.main()
