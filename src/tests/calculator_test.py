import unittest
from services.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
        self.calculator.set_operand1(16)

    def test_hello_world(self):
        self.assertEqual("Hello world", "Hello world")

    def test_add_positive_integer(self):
        self.assertEqual(self.calculator.count_two_operands("+",5), "21.0")

    def test_sub_positive_integer(self):
        self.assertEqual(self.calculator.count_two_operands("-",5), "11.0")

    def test_div_positive_integer(self):
        self.assertEqual(self.calculator.count_two_operands("/",8), "2.0")

    def test_mul_positive_integer(self):
        self.assertEqual(self.calculator.count_two_operands("*",2), "32.0")

    def test_square_root(self):
        self.assertEqual(self.calculator.count_one_operands("sqrt"), "4.0")

    def test_power_of_two(self):
        self.assertEqual(self.calculator.count_one_operands("exp"), "256.0")

    def test_div_zero_returns_error(self):
        self.assertEqual(self.calculator.count_two_operands("/",0), "error div zero")

    def test_calculator_get_operand1_returns_correctly(self):
        self.assertEqual(self.calculator.get_operand1(), "16")

    def test_calculator_set_operand1_returns_correctly(self):
        self.calculator.set_operand1("8")
        self.assertEqual(self.calculator.get_operand1(), "8")
