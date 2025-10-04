# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """This method runs before every test case. Creates a calculator instance."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method with normal and edge cases."""
        self.assertEqual(self.calc.add(2, 3), 5)       # positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)      # negative + positive
        self.assertEqual(self.calc.add(-2, -3), -5)    # two negatives
        self.assertEqual(self.calc.add(0, 0), 0)       # adding zeros

    def test_subtraction(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)   # normal subtraction
        self.assertEqual(self.calc.subtract(3, 5), -2)  # result negative
        self.assertEqual(self.calc.subtract(0, 0), 0)   # zero subtraction
        self.assertEqual(self.calc.subtract(-5, -3), -2) # negatives

    def test_multiplication(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)   # normal case
        self.assertEqual(self.calc.multiply(-2, 3), -6) # negative * positive
        self.assertEqual(self.calc.multiply(0, 5), 0)   # multiply by zero
        self.assertEqual(self.calc.multiply(-2, -3), 6) # negative * negative

    def test_division(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(6, 3), 2)     # normal division
        self.assertEqual(self.calc.divide(-6, 3), -2)   # negative / positive
        self.assertEqual(self.calc.divide(5, 2), 2.5)   # non-integer result
        self.assertIsNone(self.calc.divide(10, 0))      # division by zero
        self.assertEqual(self.calc.divide(0, 5), 0)     # zero divided by number

if __name__ == "__main__":
    unittest.main()
