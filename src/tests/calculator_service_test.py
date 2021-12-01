import unittest
from services.calculator_service import CalculatorService

class TestCalculatorService(unittest.TestCase):

    def setUp(self):
        self.calculator = CalculatorService()
        self.calculator.set_operand1("16")

    def test_add_positive_integer(self):
        self.assertEqual(self.calculator.count_two_operands("+",5),"21.0")

    def test_sub_positive_integer(self):
        self.assertEqual(self.calculator.count_two_operands("-",5),"11.0")

    def test_div_positive_integer(self):
        self.assertEqual(self.calculator.count_two_operands("/",8),"2.0")

    def test_mul_positive_integer(self):
        self.assertEqual(self.calculator.count_two_operands("*",2),"32.0")

    def test_square_root(self):
        self.assertEqual(self.calculator.count_one_operands("sqrt"),"4.0")

    def test_power_of_two(self):
        self.assertEqual(self.calculator.count_one_operands("exp"),"256.0")

    def test_div_zero_returns_error(self):
        self.assertEqual(self.calculator.count_two_operands("/",0),"error div zero")

    def test_sqrt_neg_returns_error(self):
        self.calculator.set_operand1("-10")
        self.assertEqual(self.calculator.count_one_operands("sqrt"),
                            "error sqrt not defined for negative")

    def test_calculator_get_operand1_returns_correctly(self):
        self.assertEqual(self.calculator.get_operand1(),"16")

    def test_calculator_set_operand1_returns_correctly(self):
        self.calculator.set_operand1("8")
        self.assertEqual(self.calculator.get_operand1(),"8")

    def test_calculator_memory_zero_when_started(self):
        self.assertEqual(self.calculator.get_memory(),"0")

    def test_calculator_set_memory_returns_correctly(self):
        self.calculator.set_memory("9.9")
        self.assertEqual(self.calculator.get_memory(),"9.9")

    def test_calculator_count_two_opersands_if_operand1_space(self):
        self.calculator.set_operand1("")
        self.assertEqual(self.calculator.count_two_operands("+","2"),"2.0")

    def test_calculator_count_one_opersands_if_operand1_space(self):
        self.calculator.set_operand1("")
        self.assertEqual(self.calculator.count_one_operands("exp"),"0.0")
