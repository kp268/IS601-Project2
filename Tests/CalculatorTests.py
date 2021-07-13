import unittest
from Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiply(3, 6), 18)
        self.assertEqual(self.calculator.result, 18)

    def test_division(self):
        self.assertEqual(self.calculator.divide(4, 2), 2)
        self.assertEqual(self.calculator.result, 2)

    def test_square(self):
        self.assertEqual(self.calculator.square(9), 81)
        self.assertEqual(self.calculator.result, 81)

    def test_squareroot(self):
        self.assertEqual(self.calculator.squareroot(36), 6)
        self.assertEqual(self.calculator.result, 6)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtract(8, 8), 0)
        self.assertEqual(self.calculator.result, 0)

    def test_addition(self):
        self.assertEqual(self.calculator.add(7, 3), 10)
        self.assertEqual(self.calculator.result, 10)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
